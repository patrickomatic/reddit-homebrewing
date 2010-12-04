from django.db import models
from django.contrib.auth.models import User


class BeerStyle(models.Model):
	name = models.CharField(max_length=255)

class Entry(models.Model):
	style = models.ForeignKey('BeerStyle')
	user = models.ForeignKey(User)

class JudgingResults(models.Model):
	# XXX set max_value to 10
	taste = models.PositiveIntegerField()
	appearance = models.PositiveIntegerField()
	mouth_feel = models.PositiveIntegerField()
	aroma = models.PositiveIntegerField()

	# XXX description, overall summary etc...
