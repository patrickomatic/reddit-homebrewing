import datetime, smtplib, typedmodels, logging

from django.conf import settings
from django.contrib.auth.models import User
from django.core.cache import cache
from django.core.mail import EmailMultiAlternatives
from django.db import models
from django.db.models import Q
from django.forms.models import model_to_dict
from django.template.loader import render_to_string

from homebrewit.signup.models import UserProfile


logger = logging.getLogger(__name__)

class ContestYearManager(models.Manager):
    def expire_get_all_year_summary_cache(self):
        cache.delete('get_all_year_summary_query')
        
    def get_all_year_summary(self):
        data = cache.get('get_all_year_summary_query')
        if not data: 
            data = self.__uncached_get_all_year_summary()
            cache.set('get_all_year_summary_query', data, 60 * 60 * 24 * 30)

        return data

    def __uncached_get_all_year_summary(self):
        contest_data = {}

        for style in BeerStyle.objects.top_level_styles():
            year = style.contest_year.contest_year

            top_entry = Entry.objects.get_top_n(style, 1)
            if top_entry and top_entry[0].winner:
                winner_data = {
                    'winner': top_entry[0].user.username + ": " + unicode(top_entry[0].score),
                    'id': top_entry[0].id,
                }
            else:
                winner_data = None

            data = {
                'n_entries': style.n_entries(),
                'n_judged': style.n_judged(),
                'n_received': style.n_received(),
                'winner': winner_data,
                'style': style,
            }

            if year in contest_data:
                contest_data[year].append(data)
            else:
                contest_data[year] = [data]

        return [(year, contest_data[year]) for year in sorted(contest_data.iterkeys(), reverse=True)]


    def get_current_contest_year(self):
        try:
            return self.filter(allowing_entries=True)[0]
        except IndexError:
            return None


class ContestYear(models.Model):
    contest_year = models.PositiveSmallIntegerField(unique=True, db_index=True, default=datetime.datetime.now().year)
    allowing_entries = models.BooleanField(default=False)
    finished_judging = models.BooleanField(default=False)
    prize_description = models.TextField(null=True, blank=True)

    objects = ContestYearManager()

    class Meta:
        ordering = ('-contest_year',)

    def __unicode__(self):
        return unicode(self.contest_year)


class BeerDetail(typedmodels.TypedModel):
    beer_style = models.ForeignKey('BeerStyle', related_name='beer_details', db_index=True)
    description = models.TextField()
    must_specify = models.BooleanField()

    def __unicode__(self):
        return "%s: %s" % (self.beer_style, self.description)


class BeerDetailChoice(models.Model):
    name = models.TextField()
    multiple_choice_beer_detail = models.ForeignKey('BeerDetail', related_name='choices', db_index=True)

    def __unicode__(self):
        return self.name

class MultipleChoiceBeerDetail(BeerDetail):
    pass

class TextBeerDetail(BeerDetail):
    pass


class EntryBeerDetail(models.Model):
    entry = models.ForeignKey('Entry', related_name='entry_beer_details', db_index=True)
    beer_detail = models.ForeignKey('BeerDetail', db_index=True)
    value = models.TextField()


class BeerStyleManager(models.Manager):
    # TODO: apparently these are chainable in django 1.7
    def for_year(self, year):
        styles = self.raw("""
            SELECT c1.* 
            FROM contest_beerstyle c1 
                 LEFT OUTER JOIN contest_beerstyle c2 ON c2.id = c1.parent_style_id 
                 JOIN contest_contestyear cy ON cy.id = c1.contest_year_id
            WHERE NOT EXISTS 
                (SELECT 1 FROM contest_beerstyle WHERE parent_style_id = c1.id) 
                AND cy.contest_year = %s
            ORDER BY c2.parent_style_id;
        """, [int(year)])

        results, last_parent_style = [], None
        for style in styles:
            if style.parent_style and style.parent_style != last_parent_style:
                results.append(style.parent_style)

            last_parent_style = style.parent_style
            results.append(style)
            
        return results

    def top_level_styles_for_year(self, year):
        return self.filter(parent_style__isnull=True, contest_year__contest_year=int(year))

    def top_level_styles(self):
        return self.filter(parent_style__isnull=True)


class BeerStyle(models.Model):
    name = models.TextField()
    contest_year = models.ForeignKey('ContestYear', related_name='beer_styles', db_index=True)
    judge = models.ForeignKey(User, null=True, blank=True, db_index=True)
    parent_style = models.ForeignKey('BeerStyle', related_name='subcategories', null=True, blank=True, db_index=True)

    objects = BeerStyleManager()

    def can_enter(self):
        return not self.has_subcategories()

    def has_subcategories(self):
        return self.subcategories.exists()

    def is_subcategory(self):
        return parent_style is not None

    def n_entries(self):
        return Entry.objects.filter(style=self).count() + Entry.objects.filter(style__parent_style=self).count()

    def n_judged(self):
        return Entry.objects.filter(style=self, score__isnull=False).count() + Entry.objects.filter(style__parent_style=self, score__isnull=False).count()

    def n_received(self):
        return Entry.objects.filter(style=self, received_entry=True).count() + Entry.objects.filter(style__parent_style=self, received_entry=True).count()

    def __unicode__(self):
        return self.name

 
class EntryManager(models.Manager):
    def get_top_n(self, style, n):
        return self.filter(Q(style=style) | Q(style__parent_style=style)).filter(score__isnull=False).order_by('-score')[:n]

    def get_top_3(self, style): 
        return self.get_top_n(style, 3)

    def get_top_2(self, style): 
        return self.get_top_n(style, 2)

    def get_all_winners(self, contest_year=None):
        if contest_year is None:
            contest_year = ContestYear.objects.get_current_contest_year()

        return set([entry.user for entry in Entry.objects.filter(winner=True, 
                                        style__contest_year=contest_year)])

    def for_beer_style(self, beer_style):
        return Entry.objects.filter(Q(style=beer_style) | Q(style__parent_style=beer_style))

    
    def judge_entries(self, year):
        # calculate the score of each entry for the year
        for entry in self.filter(style__contest_year__contest_year=year):
            total, num = 0, 0

            if entry.bjcp_judging_results.exists():
                # if this is one using the bjcp judging result,
                # then we're not worried about multiple judges
                # and don't have to do an average
                entry.score = entry.overall_rating()
                entry.save()
            else:
                # get the average of each judge who judged this entry
                results = JudgingResult.objects.filter(entry=entry)

                if results:
                    for result in results:
                        num += 1
                        total += result.overall_rating()

                    entry.score = total / num
                    entry.save()


        # now for each style, assign winners
        for style in BeerStyle.objects.filter(contest_year__contest_year=year):
            place = 1
            for entry in Entry.objects.get_top_3(style):
                entry.winner = True
                entry.rank = place
                entry.save()
                place += 1


class Entry(models.Model):
    style = models.ForeignKey('BeerStyle', db_index=True)
    beer_name = models.TextField(null=True, blank=True)
    special_ingredients = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User)
    winner = models.BooleanField(default=False)
    rank = models.PositiveSmallIntegerField(db_index=True, null=True, blank=True)
    score = models.PositiveIntegerField(null=True, blank=True)
    mailed_entry = models.BooleanField(default=False)
    received_entry = models.BooleanField(default=False)

    objects = EntryManager()

    class Meta:
        ordering = ('style', 'score')


    def is_bjcp_judging_result(self):
        return not JudgingResult.objects.filter(entry_id=self.id).exists()

    def is_cider_entry(self):
        return self.is_bjcp_judging_result() and hasattr(self.bjcp_judging_results.first(), 'bjcpciderjudgingresult')

    def send_shipping_email(self):
        if not self.style.judge:
            logger.error("Attempted to send email for style without judge: entry.id=%s" % self.id)
            return

        if not self.user.email:
            logger.error("Email isn't set for %s" % self.user.username)
            return

        try:
            judge_profile = self.style.judge.get_profile()
        except UserProfile.DoesNotExist:
            logger.error("Attempted to send email for style without judge's address set: entry.id=%s" % self.id)
            return

        try:
            contest_year = self.style.contest_year.contest_year

            email_vars = model_to_dict(judge_profile)
            email_vars.update({
                'username': self.user.username,
                'contest_year': contest_year,
                'style': unicode(self.style.name),
            })

            # convert any Nones to ""
            for k, v in email_vars.iteritems():
                if v is None: email_vars[k] = ""


            msg = EmailMultiAlternatives("Shipping info for the %d Reddit Homebrew Contest" % contest_year, 
                    render_to_string('emails/shipping_info.txt', email_vars), settings.POSTMARK_SENDER, [self.user.email])
            msg.attach_alternative(render_to_string('emails/shipping_info.html', email_vars), "text/html")
            msg.send()
                
            self.mailed_entry = True
            self.save()
        except smtplib.SMTPException as e:
            logger.error("Error sending shipping email: %s" % e)
            raise e

    def get_description(self):
        rating = self.overall_rating()

        if not rating: return ""

        if rating > 44:
            return "Outstanding (%d / 50)" % rating
        elif rating > 37:
            return "Excellent (%d / 50)" % rating
        elif rating > 29:
            return "Very Good (%d / 50)" % rating
        elif rating > 20:
            return "Good (%d / 50)" % rating
        elif rating > 13:
            return "Fair (%d / 50)" % rating
        else:
            return "Problematic (%d / 50)" % rating

    def get_rating_description(self):
        if self.is_bjcp_judging_result():
            return self.get_description()
        else:
            return JudgingResult.rating_description_str(self.score)


    def overall_rating(self):
        results, total_points = self.bjcp_judging_results.all(), 0
        if len(results) == 0: return None

        for r in results: total_points += r.overall_rating()
        return float(total_points) / len(results)


    def __unicode__(self):
        s = unicode(self.style)

        if self.beer_name:
            s = s + " / " + self.beer_name 

        s = s + " (" + self.user.username + ")"

        return s


def integer_range(max_int):
    return [(x, str(x)) for x in xrange(1, max_int + 1)]


class BJCPJudgingResult(models.Model):
    entry = models.ForeignKey(Entry, db_index=True, related_name='bjcp_judging_results')
    judge = models.ForeignKey(User, db_index=True)
    judge_bjcp_id = models.TextField(null=True, blank=True)

    stylistic_accuracy = models.PositiveSmallIntegerField(choices=integer_range(5), help_text='1 = not to style, 5 = classic example')
    technical_merit = models.PositiveSmallIntegerField(choices=integer_range(5), help_text='1 = significant flaws, 5 = flawless')
    intangibles = models.PositiveSmallIntegerField(choices=integer_range(5), help_text='1 = lifeless, 5 = wonderful')


    def overall_rating(self):
        if hasattr(self, 'bjcpbeerjudgingresult'):
            return self.bjcpbeerjudgingresult.overall_rating()
        elif hasattr(self, 'bjcpciderjudgingresult'):
            return self.bjcpciderjudgingresult.overall_rating()

    def __unicode__(self):
        return "%s {entry: %s, judge: %s}" % (self.id, self.entry, self.judge)


class BJCPBeerJudgingResult(BJCPJudgingResult):
    acetaldehyde = models.BooleanField(default=False, help_text='Green apple-like aroma and flavor.')
    alcoholic = models.BooleanField(default=False, help_text='The aroma, flavor, and warming effect of ethanol and higher alcohols.  Sometimes described as "hot."')
    astringent = models.BooleanField(default=False, help_text='Puckering, lingering, harshness and/or dryness in the finish/aftertaste.')
    diacetyl = models.BooleanField(default=False, help_text='Artifical butter, butterscotch or coffee aroma and flavor.  Sometimes perceived as a slickness on the tongue.')
    dms = models.BooleanField(default=False, help_text='At low levels a sweet, cooked or canned corn-like aroma and flavor.', verbose_name='DMS (dimethyl sulfide)')
    estery = models.BooleanField(default=False, help_text='Aroma and/or flavor of any ester (fruits, fruit flavorings or roses)')
    grassy = models.BooleanField(default=False, help_text='Aroma/flavor of fresh-cut grass or green leaves.')
    light_struck = models.BooleanField(default=False, help_text='Similar to the aroma of a skunk.')
    metallic = models.BooleanField(default=False, help_text='Tinny, coiny, copper, iron or blood-like flavor.')
    musty = models.BooleanField(default=False, help_text='Stale, musty or moldy aromas/flavors.')
    oxidized = models.BooleanField(default=False, help_text='Any one or combinations of winy/vinous, cardboard, papery, or sherry-like aromas and flavors.')
    phenolic = models.BooleanField(default=False, help_text='Spicy (clove, pepper), smokey, plastic adhesive strip and/or medicinal (chlorophenolic.)')
    solvent = models.BooleanField(default=False, help_text='Aromas and flavors of higher alcohols (fusel alcohols.)  Similar to acetone or lacquer thinner aromas.')
    sour_acidic = models.BooleanField(default=False, help_text='Tartness in aroma and flavor.  Can be sharp and clean (lactic acid) or vinegar-like (acetic acid.)', verbose_name='Sour/Acidic')
    sulfur = models.BooleanField(default=False, help_text='The aroma of rotten eggs or burning matches.')
    vegetal = models.BooleanField(default=False, help_text='Cooked, canned or rotten vegetable aroma and flavor (cabbage, onion, celery, asparagus, etc.)')
    yeasty = models.BooleanField(default=False, help_text='A bready, sulfury or yeast-like aroma or flavor.')

    aroma_description = models.TextField()
    aroma_score = models.PositiveSmallIntegerField(choices=integer_range(12))

    appearance_description = models.TextField()
    appearance_score = models.PositiveSmallIntegerField(choices=integer_range(3))

    flavor_description = models.TextField()
    flavor_score = models.PositiveSmallIntegerField(choices=integer_range(20))

    mouthfeel_description = models.TextField()
    mouthfeel_score = models.PositiveSmallIntegerField(choices=integer_range(5))

    overall_impression_description = models.TextField()
    overall_impression_score = models.PositiveSmallIntegerField(choices=integer_range(10))


    def overall_rating(self):
        return self.aroma_score + self.appearance_score \
                + self.flavor_score + self.mouthfeel_score \
                + self.overall_impression_score


class BJCPCiderJudgingResult(BJCPJudgingResult):
    acetaldehyde = models.BooleanField(default=False, help_text='Green apple candy aroma/flavor')
    acetified = models.BooleanField(default=False, help_text='(Volatile Acidity, VA) Ethyl acetate (solvent, nail polish) or acetic acid (vinegar, harsh in back of throat).')
    acidic = models.BooleanField(default=False, help_text='Sour-tart flavor.  Typically from one of several acids: malic, lactic, or citric. Must be in balance.')
    alcoholic = models.BooleanField(default=False, help_text='The warm effect of ethanol/higher alcohols.')
    astringent = models.BooleanField(default=False, help_text='A drying sensation in the mouth similar to chewing on a teabag. Must be in balance if present.')
    bitter = models.BooleanField(default=False, help_text='A sharp taste that is unpleasant at high levels.')
    diacetyl = models.BooleanField(default=False, help_text='Butter of butterscotch aroma or flavor.')
    farmyard = models.BooleanField(default=False, help_text='Manure-like (cow or pig) or barnyard (horse stall on a warm day).')
    fruity = models.BooleanField(default=False, help_text='The aroma and flavor of fresh fruits that may be appropriate in some styles and not others.')
    metallic = models.BooleanField(default=False, help_text='Tinny, coiny, copper, iron or blood-like flavor.')
    mousy = models.BooleanField(default=False, help_text='Taste evocative of the smell of a rodent\'s den/cage.')
    oaky = models.BooleanField(default=False, help_text='A taste or aroma due to an extend length of time in a barrel or on wood chips. "Barrel character."')
    oily_ropy = models.BooleanField(default=False, help_text='A sheen in visual appearance, as an unpleasant viscous character proceeding in a ropy character.', verbose_name='Oily/Ropy')
    oxidized = models.BooleanField(default=False, help_text='Any one or combinations of winy/vinous, cardboard, papery, or sherry-like aromas and flavors.')
    phenolic = models.BooleanField(default=False, help_text='Plastic, band-aid and/or medicinal')
    spicy_smoky = models.BooleanField(default=False, help_text='Spice, cloves, smoky, ham.', verbose_name='Spicy/Smoky')
    sulfite = models.BooleanField(default=False, help_text='Rotten eggs, from fermentation problems')
    sweet = models.BooleanField(default=False, help_text='BAsic taste of sugar.  Must be in balance if present.')
    thin = models.BooleanField(default=False, help_text='Watery, lacking body or "stuffing."')
    vegetal = models.BooleanField(default=False, help_text='Cooked, canned or rotten vegetable aroma and flavor (cabbage, onion, celery, asparagus, etc.)')

    aroma_description = models.TextField()
    aroma_score = models.PositiveSmallIntegerField(choices=integer_range(10))

    appearance_description = models.TextField()
    appearance_score = models.PositiveSmallIntegerField(choices=integer_range(6))

    flavor_description = models.TextField()
    flavor_score = models.PositiveSmallIntegerField(choices=integer_range(24))

    overall_impression_description = models.TextField()
    overall_impression_score = models.PositiveSmallIntegerField(choices=integer_range(10))


    def overall_rating(self):
        return self.aroma_score + self.appearance_score \
                + self.flavor_score + self.overall_impression_score


class JudgingResult(models.Model):
    judge = models.ForeignKey(User)
    judge_bjcp_id = models.TextField(null=True, blank=True)

    entry = models.ForeignKey(Entry)

    aroma_description = models.TextField()
    aroma_score = models.PositiveSmallIntegerField(choices=integer_range(12))

    appearance_description = models.TextField()
    appearance_score = models.PositiveSmallIntegerField(choices=integer_range(3))

    flavor_description = models.TextField()
    flavor_score = models.PositiveSmallIntegerField(choices=integer_range(20))

    mouthfeel_description = models.TextField()
    mouthfeel_score = models.PositiveSmallIntegerField(choices=integer_range(5))

    overall_impression_description = models.TextField()
    overall_impression_score = models.PositiveSmallIntegerField(choices=integer_range(10))

    stylistic_accuracy = models.PositiveSmallIntegerField(choices=integer_range(5), help_text='1 = not to style, 5 = classic example')

    technical_merit = models.PositiveSmallIntegerField(choices=integer_range(5), help_text='1 = significant flaws, 5 = flawless')

    intangibles = models.PositiveSmallIntegerField(choices=integer_range(5), help_text='1 = lifeless, 5 = wonderful')


    @classmethod
    def rating_description_str(self, rating):
        if rating > 54:
            return "Outstanding (%d / 65)" % rating
        elif rating > 44:
            return "Excellent (%d / 65)" % rating
        elif rating > 34:
            return "Very Good (%d / 65)" % rating
        elif rating > 24:
            return "Good (%d / 65)" % rating
        elif rating > 14:
            return "Fair (%d / 65)" % rating
        else:
            return "Problematic (%d / 65)" % rating


    def overall_rating(self):
        return self.aroma_score + self.appearance_score \
                + self.flavor_score + self.mouthfeel_score \
                + self.overall_impression_score + self.stylistic_accuracy \
                + self.technical_merit + self.intangibles


    def get_description(self):
        return JudgingResult.rating_description_str(self.overall_rating())

    def save(self):
        # update the entry's score
        self.entry.score = self.overall_rating()
        self.entry.save()

        models.Model.save(self)


    def __unicode__(self):
        return "%s (score: %s)" % (self.entry, self.overall_rating())
