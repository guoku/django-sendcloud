from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = __doc__

    def add_arguments(self, parser):

        pass

    def handle(self, *args, **options):
        return
