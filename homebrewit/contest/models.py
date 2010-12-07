import datetime

from django.db import models
from django.contrib.auth.models import User


class BeerStyle(models.Model):
	name = models.CharField(max_length=255)

	def __unicode__(self):
		return self.name


class Entry(models.Model):
	style = models.ForeignKey('BeerStyle', db_index=True)
	user = models.ForeignKey(User)
	winner = models.BooleanField(default=False)
	rank = models.PositiveSmallIntegerField(db_index=True, null=True, blank=True)
	contest_year = models.PositiveIntegerField(default=datetime.datetime.now().year)
	score = models.PositiveIntegerField(null=True, blank=True)

	class Meta:
		ordering = ['style', 'score']


	def __unicode__(self):
		return "%s: %s" % (user.username, style.name)



# XXX need to make some kind of PositiveInteger range model thing
class JudgingResult(models.Model):
	judge = models.ForeignKey(User)
	judge_bjcp_id = models.CharField(max_length=255, null=True, blank=True)

	entry = models.ForeignKey(Entry)

	special_ingredients = models.CharField(max_length=5000, blank=True, null=True)

	# out of 12 points XXX
	aroma_description = models.CharField(max_length=5000)
	aroma_score = models.PositiveSmallIntegerField()

	# out of 3 points XXX
	appearance_description = models.CharField(max_length=5000)
	appearance_score = models.PositiveSmallIntegerField()

	# out of 20 points XXX
	flavor_description = models.CharField(max_length=5000)
	flavor_score = models.PositiveSmallIntegerField()

	# out of 5 points XXX
	mouthfeel_description = models.CharField(max_length=5000)
	mouthfeel_score = models.PositiveSmallIntegerField()

	# out of 10 points XXX
	overall_impression_description = models.CharField(max_length=5000)
	overall_impression_score = models.PositiveSmallIntegerField()

	# XXX put a help text:
	# (1 = not to style, 5 = classic example)
	stylistic_accuracy = models.PositiveSmallIntegerField()

	# XXX put a help text:
	# (1 = significant flaws, 5 = flawless)
	technical_merit = models.PositiveSmallIntegerField()

	# XXX put a help text:
	# (1 = lifeless, 5 = wonderful)
	intangibles = models.PositiveSmallIntegerField()


	def overall_rating(self):
		return self.aroma_score + self.appearance_score \
				+ self.flavor_score + self.mouthfeel_score \
				+ self.overall_impression_score + self.stylistic_accuracy \
				+ self.technical_merit + self.intangibles


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


	def __unicode__(self):
		return "%s: %s" % (self.entry.user.username, self.overall_rating())
