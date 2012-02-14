import datetime, smtplib

from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db import models
from django.db.models import Max
from django.forms.models import model_to_dict


class ContestYearManager(models.Manager):
	def get_current_contest_year(self):
		return ContestYear.objects.aggregate(Max('contest_year'))['contest_year__max']


class ContestYear(models.Model):
	contest_year = models.PositiveSmallIntegerField(unique=True, db_index=True, default=datetime.datetime.now().year)
	allowing_entries = models.BooleanField(default=False)
	finished_judging = models.BooleanField(default=False)

	objects = ContestYearManager()


	class Meta:
		ordering = ('-contest_year',)

	def __unicode__(self):
		return unicode(self.contest_year)


class BeerStyle(models.Model):
	name = models.CharField(max_length=255)
	contest_year = models.ForeignKey('ContestYear')
	judge = models.ForeignKey(User, null=True, blank=True)

	def __unicode__(self):
		return "%s (%s)" % (self.name, self.contest_year)


class EntryManager(models.Manager):
	def get_top_n(self, style, n):
		return Entry.objects.filter(style=style).filter(score__isnull=False).order_by('-score')[:n]

	def get_top_3(self, style): 
		return self.get_top_n(style, 3)

	def get_top_2(self, style): 
		return self.get_top_n(style, 2)

	def get_all_winners(self, contest_year=ContestYear.objects.get_current_contest_year):
		return set([entry.user for entry in Entry.objects.filter(winner=True, 
										style__contest_year__contest_year=contest_year)])

	
	def judge_entries(self, year):
		# calculate the score of each entry for the year
		for entry in Entry.objects.filter(style__contest_year__contest_year=year):
			total, num = 0, 0

			# get the average of each judge who judged this entry
			# XXX this needs to generate BJCPJudgingResults
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
	bjcp_judging_result = models.ForeignKey('BJCPJudgingResult', null=True, blank=True)
	beer_name = models.CharField(max_length=255, null=True, blank=True)
	special_ingredients = models.CharField(max_length=5000, blank=True, null=True)
	user = models.ForeignKey(User)
	winner = models.BooleanField(default=False)
	rank = models.PositiveSmallIntegerField(db_index=True, null=True, blank=True)
	score = models.PositiveIntegerField(null=True, blank=True)
	mailed_entry = models.BooleanField(default=False)
	received_entry = models.BooleanField(default=False)

	objects = EntryManager()

	class Meta:
		ordering = ('style', 'score')


	def send_shipping_email(self):
		if not self.style.judge:
			return

		if not self.user.email:
			# XXX logging.warn
			print >>sys.stderr, "Email isn't set for ", self.user.username
			return

		try:
			contest_year = self.style.contest_year.contest_year

			email_vars = model_to_dict(self.style.judge.get_profile())
			email_vars.update({
				'username': self.user.username,
				'contest_year': contest_year,
				'style': unicode(self.style.name),
			})

			# convert any Nones to ""
			for k, v in email_vars.iteritems():
				if v is None: email_vars[k] = ""

			send_mail("Shipping info for the %d Reddit Homebrew Contest" % contest_year, 
				""" 
Hey %(username)s,

Thanks for entering the %(contest_year)s %(style)s category.  When
sending your samples, we request two 12oz bottles including your
reddit username and the style of the samples.  You can send them to:

%(name)s
%(address_1)s
%(address_2)s
%(city)s, %(state)s %(zip_code)s

For tips on how to package your shipment, check out <a href="http://www.reddit.com/r/beertrade/comments/atztu/trading_and_packaging_tips/" title="this /r/beertrade thread">this /r/beertrade thread</a>.  If you have any questions or problems, please <a href="http://www.reddit.com/message/compose?to=%%23Homebrewing" title="contact the moderators">contact the moderators</a>.

As always, we appreciate your participation and look forward to a great competition.  May be the best brew win!
				""" % email_vars, 'do.not.reply@reddithomebrewing.com', 
					[self.user.email], fail_silently=False)

			self.mailed_entry = True
			self.save()
		except smtplib.SMTPException as e:
			# XXX use logger
			print >>sys.stderr, "Error sending shipping email: ", e


	def get_rating_description(self):
		if self.judging_result:
			return self.judging_result.get_description()
		else:
			return JudgingResult.rating_description_str(self.score)


	def __unicode__(self):
		return "%s: %s" % (self.user.username, self.style)


def integer_range(max_int):
	return [(x, str(x)) for x in xrange(1, max_int + 1)]


class BJCPJudgingResult(models.Model):
	judge = models.ForeignKey(User)
	judge_bjcp_id = models.CharField(max_length=255, null=True, blank=True)

	aroma_description = models.CharField(max_length=5000)
	aroma_score = models.PositiveSmallIntegerField(choices=integer_range(12))

	appearance_description = models.CharField(max_length=5000)
	appearance_score = models.PositiveSmallIntegerField(choices=integer_range(3))

	flavor_description = models.CharField(max_length=5000)
	flavor_score = models.PositiveSmallIntegerField(choices=integer_range(20))

	mouthfeel_description = models.CharField(max_length=5000)
	mouthfeel_score = models.PositiveSmallIntegerField(choices=integer_range(5))

	overall_impression_description = models.CharField(max_length=5000)
	overall_impression_score = models.PositiveSmallIntegerField(choices=integer_range(10))

	stylistic_accuracy = models.PositiveSmallIntegerField(choices=integer_range(5), help_text='1 = not to style, 5 = classic example')

	technical_merit = models.PositiveSmallIntegerField(choices=integer_range(5), help_text='1 = significant flaws, 5 = flawless')

	intangibles = models.PositiveSmallIntegerField(choices=integer_range(5), help_text='1 = lifeless, 5 = wonderful')


	def overall_rating(self):
		return self.aroma_score + self.appearance_score \
				+ self.flavor_score + self.mouthfeel_score 


	def get_description(self):
		rating = self.overall_rating()

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


# XXX need to save the score 
#	def save(self):
#		# update the entry's score
#		self.entry.score = self.overall_rating()
#		self.entry.save()
#
#		models.Model.save(self)


	def __unicode__(self):
		return "%s (score: %s)" % (self.entry, self.overall_rating())


class JudgingResult(models.Model):
	judge = models.ForeignKey(User)
	judge_bjcp_id = models.CharField(max_length=255, null=True, blank=True)

	entry = models.ForeignKey(Entry)

	aroma_description = models.CharField(max_length=5000)
	aroma_score = models.PositiveSmallIntegerField(choices=integer_range(12))

	appearance_description = models.CharField(max_length=5000)
	appearance_score = models.PositiveSmallIntegerField(choices=integer_range(3))

	flavor_description = models.CharField(max_length=5000)
	flavor_score = models.PositiveSmallIntegerField(choices=integer_range(20))

	mouthfeel_description = models.CharField(max_length=5000)
	mouthfeel_score = models.PositiveSmallIntegerField(choices=integer_range(5))

	overall_impression_description = models.CharField(max_length=5000)
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
