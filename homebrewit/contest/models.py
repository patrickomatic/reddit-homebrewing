import datetime

from django.db import models
from django.contrib.auth.models import User


def rating_description_str(rating):
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


class ContestYear(models.Model):
	contest_year = models.PositiveSmallIntegerField(unique=True, db_index=True, default=datetime.datetime.now())

	class Meta:
		ordering = ('-contest_year',)

	def __unicode__(self):
		return unicode(self.contest_year)


class BeerStyle(models.Model):
	name = models.CharField(max_length=255)
	contest_year = models.ForeignKey('ContestYear')

	def __unicode__(self):
		return "%s (contest year: %s)" % (self.name, self.contest_year)


class EntryManager(models.Manager):
	def get_top_n(self, style, n):
		return Entry.objects.filter(style=style)[:n]

	def get_top_3(self, style): 
		return self.get_top_n(style, 3)

	def get_top_2(self, style): 
		return self.get_top_n(style, 2)

	# XXX is the datetime keyword ineficient? when does it get executed?
	def get_all_winners(self, contest_year=datetime.datetime.now().year):
		return set([entry.user for entry in Entry.objects.filter(winner=True, 
										style__contest_year__contest_year=contest_year)])


class Entry(models.Model):
	beer_name = models.CharField(max_length=255, null=True, blank=True)
	special_ingredients = models.CharField(max_length=5000, blank=True, null=True)
	style = models.ForeignKey('BeerStyle', db_index=True)
	user = models.ForeignKey(User)
	winner = models.BooleanField(default=False)
	rank = models.PositiveSmallIntegerField(db_index=True, null=True, blank=True)
	score = models.PositiveIntegerField(null=True, blank=True)

	objects = EntryManager()

	class Meta:
		ordering = ('style', '-score')


	def get_rating_description(self):
		return rating_description_str(self.score)

	def __unicode__(self):
		return "%s: %s" % (self.user.username, self.style)


def integer_range(max_int):
	return [(x, str(x)) for x in xrange(1, max_int + 1)]


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


	def overall_rating(self):
		return self.aroma_score + self.appearance_score \
				+ self.flavor_score + self.mouthfeel_score \
				+ self.overall_impression_score + self.stylistic_accuracy \
				+ self.technical_merit + self.intangibles


	def get_description(self):
		return rating_description_str(self.overall_rating())


	def __unicode__(self):
		return "%s (score: %s)" % (self.entry, self.overall_rating())
