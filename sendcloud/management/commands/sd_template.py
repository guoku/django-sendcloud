import logging
from django.core.management import BaseCommand
from sendcloud.core.template import TemplateAPI


logger = logging.getLogger('sendcloud')


class Command(BaseCommand):

    help = __doc__

    def add_arguments(self, parser):
        parser.add_arguments(
            '-l', '--list',
            dest='list',
            action="store_true",
            help="list mail template from Send Cloud"
        )

    def handle(self, *args, **options):
        _list = options.get('list')

        if _list:
            r = TemplateAPI().list()
            logger.info(r)

        return

