from django.core.management import BaseCommand


class Command(BaseCommand):

    help = __doc__

    def add_arguments(self, parser):
        parser.add_arguments(
            '-l', '--list',
            dest='list',
            action="store_true"
        )

    def handle(self, *args, **options):
        pass