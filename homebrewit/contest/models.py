import datetime

from django.db import models
from django.contrib.auth.models import User


class BeerStyle(models.Model):
	name = models.CharField(max_length=255)

	def __unicode__(self):
		return self.name


class Entry(models.Model):
	style = models.ForeignKey('BeerStyle')
	user = models.ForeignKey(User)
	winner = models.BooleanField(default=False)
	rank = models.PositiveSmallIntegerField()
	contest_year = models.PositiveIntegerField(default=datetime.datetime.now().year)

	def __unicode__(self):
		return "%s: %s" % (user.username, style.name)


class JudgingResult(models.Model):
	taste = models.PositiveSmallIntegerField()
	appearance = models.PositiveSmallIntegerField()
	mouth_feel = models.PositiveSmallIntegerField()
	aroma = models.PositiveSmallIntegerField()
	entry = models.ForeignKey('Entry')
	contest_year = models.PositiveIntegerField(default=datetime.datetime.now().year)

	# XXX description, overall summary etc...

	def overall_rating(self):
		return float(self.taste) + float(self.appearance) + float(self.mouth_feel) + float(self.aroma) / 4.0


	def __unicode__(self):
		return "%s: %s" % (self.entry.user.username, self.overall_rating())
