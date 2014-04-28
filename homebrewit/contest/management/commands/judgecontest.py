from django.core.management.base import BaseCommand

from homebrewit.contest.models import *


class Command(BaseCommand):
    args = '<year1 year2 ...>'
    help = "Compile the results and set the winners of a contest for a given year"

    def handle(self, *args, **options):
        for year in args:
            Entry.objects.judge_entries(int(year))
