from django.core.management.base import NoArgsCommand

from homebrewit.contest.models import *

class Command(NoArgsCommand):
    help = "Send all contestants an email who haven't yet been emailed"

    def handle(self, *args, **kwargs):
        for entry in Entry.objects.filter(mailed_entry=False).filter(style__judge__isnull=False):
            entry.send_shipping_email()
