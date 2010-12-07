from django.core.management.base import BaseCommand

from homebrewit.contest.models import *


class Command(BaseCommand):
	args = '<year1 year2 ...>'
	help = "Compile the results and set the winners of a contest for a given year"

	def handle(self, *args, **options):
		for year in args:
			# calculate the score of each entry for the year
			for entry in Entry.objects.filter(contest_year=int(year)):
				total, num = 0, 0

				for result in JudgingResult.objects.filter(entry=entry):
					num += 1
					total += result.overall_rating()

				entry.score = total / num
				entry.save()


			# now for each style, assign winners
			for style in Style.objects.all():
				place = 1
				for entry in Entry.objects.filter(contest_year=int(year), style=style)[:3]:
					entry.winner = True
					entry.rank = place
					entry.save()
					place += 1
