from django.db import models
from django.contrib.auth.models import User


class BeerStyle(models.Model):
	name = models.CharField(max_length=255)

	def __unicode__(self):
		return self.name


class Entry(models.Model):
	style = models.ForeignKey('BeerStyle')
	user = models.ForeignKey(User)

	def __unicode__(self):
		return "%s: %s" % (user.username, style.name)


class JudgingResult(models.Model):
	# XXX set max_value to 10
	taste = models.PositiveIntegerField()
	appearance = models.PositiveIntegerField()
	mouth_feel = models.PositiveIntegerField()
	aroma = models.PositiveIntegerField()
	entry = models.ForeignKey('Entry')

	# XXX description, overall summary etc...

	def overall_rating(self):
		return float(self.taste) + float(self.appearance) + float(self.mouth_feel) + float(self.aroma) / 4.0


	def __unicode__(self):
		return "%s: %s" % (self.entry.user.username, self.overall_rating())
