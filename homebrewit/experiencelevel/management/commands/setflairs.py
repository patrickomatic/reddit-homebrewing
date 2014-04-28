from django.core.management.base import BaseCommand, CommandError

from homebrewit.experiencelevel.models import *
from homebrewit.reddit import set_flair_csv


def split_by_amount(array, amount):
    ret = []
    while array:
        ret.append(array[:amount])
        array = array[amount:]

    return ret


class Command(BaseCommand):
    args = "<user1, user2>..."
    help = "Do a bulk update of everyone's flair with what's currently in the DB.  If no users are supplied it will update everyone's flair."

    def handle(self, *args, **kwargs):
        if args:
            experience_levels = [UserExperienceLevel.objects.get(user__username=user) for user in args]
        else:
            experience_levels = UserExperienceLevel.objects.all()

        for group in split_by_amount(experience_levels, 90):
            csv = ""
            for level in group:
                csv += "%s,,%s\n" % (level.user.username, level.experience_level.name.lower())

            set_flair_csv(csv)



