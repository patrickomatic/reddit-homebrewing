import datetime

from django.db import models, connection
from django.contrib.auth.models import User


def rating_description_str(rating):
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


class BeerStyleManager(models.Manager):
	def get_contest_years(self):
		cursor = connection.cursor()
		cursor.execute("""
			SELECT distinct(contest_year)
			FROM contest_beerstyle 
			ORDER BY contest_year DESC """)
		return [row[0] for row in cursor.fetchall()]

class BeerStyle(models.Model):
	name = models.CharField(max_length=255)
	contest_year = models.PositiveSmallIntegerField(default=datetime.datetime.now().year)

	objects = BeerStyleManager()


	def __unicode__(self):
		return "%s (contest year: %d)" % (self.name, self.contest_year)


class Entry(models.Model):
	style = models.ForeignKey('BeerStyle', db_index=True)
	user = models.ForeignKey(User)
	winner = models.BooleanField(default=False)
	rank = models.PositiveSmallIntegerField(db_index=True, null=True, blank=True)
	score = models.PositiveIntegerField(null=True, blank=True)

	class Meta:
		ordering = ['style', 'score']


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

	special_ingredients = models.CharField(max_length=5000, blank=True, null=True)

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
