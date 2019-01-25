from django.core.management.base import BaseCommand

from sendcloud.core.members import MemberAPI


class Command(BaseCommand):

    help = __doc__

    def add_arguments(self, parser):
        parser.add_argument(
            '-a', '--address',
            action='store_true',
            dest='address',
            help='Send Cloud Mail Address List'
        )

    def handle(self, *args, **options):

        return
