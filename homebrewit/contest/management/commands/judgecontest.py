from django.core.management.base import BaseCommand

from homebrewit.contest.models import *


class Command(BaseCommand):
	args = '<year1 year2 ...>'
	help = "Compile the results and set the winners of a contest for a given year"

	def handle(self, *args, **options):
		for year in args:
			year = int(year)

			# calculate the score of each entry for the year
			for entry in Entry.objects.filter(entry__contest_year=year):
				total, num = 0, 0

				# get the average of each judge who judged this entry
				for result in JudgingResult.objects.filter(entry=entry):
					num += 1
					total += result.overall_rating()

				entry.score = total / num
				entry.save()


			# now for each style, assign winners
			for style in BeerStyle.objects.filter(contest_year=year):
				place = 1
				for entry in Entry.objects.get_top_3(year, style):
					entry.winner = True
					entry.rank = place
					entry.save()
					place += 1
