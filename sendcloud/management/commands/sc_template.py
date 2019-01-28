import logging

import click
from django.core.management.base import BaseCommand
from sendcloud.core.template import TemplateAPI

logger = logging.getLogger('sendcloud')


class Command(BaseCommand):
    help = __doc__
    table_width = 200

    def _print_separator(self):
        try:
            click.echo(self._separator)
        except AttributeError:
            self._separator = "-" * self.table_width
            click.echo(self._separator)

    def _print_stats_dashboard(self, statistics):

        click.echo()
        click.echo("Django Send Cloud CLI Dashboard")
        click.echo()

        # Header
        click.echo(
            """| %-45s|%25s | %15s |%20s |%20s |""" %
            ("name", "invokeName", 'templateType', "gmtCreated", "gmtUpdated",)
        )

        self._print_separator()

        for row in statistics:
            click.echo(
                """| %-45s|%25s | %15s |%20s |%20s |""" %
                (row['name'], row['invokeName'], row["templateType"],
                 row['gmtCreated'], row['gmtUpdated'])
            )

        self._print_separator()

    def add_arguments(self, parser):
        parser.add_argument(
            '-i', '--invoke-name',
            dest="invoke_name",
            help="Send Cloud invoke name "
        )

        parser.add_argument(
            '-l', '--list',
            dest='list',
            action="store_true",
            help="list mail template from Send Cloud"
        )

        parser.add_argument(
            '-g', '--get-invoke-name',
            dest='get',
            action='store_true',
            help='get invoke name from Send Cloud'
        )

    def handle(self, *args, **options):
        _list = options.get('list')
        _get = options.get('get')

        _invoke_name = options.get('invoke_name')

        if _list:
            r = TemplateAPI().list()
            logger.info(r)
            self._print_stats_dashboard(statistics=r['info']['dataList'])

        if _get:
            r = TemplateAPI().get(invoke_name=_invoke_name)
            # logger.info(r)
            self.stdout.write(
                self.style.SUCCESS(
                    "check Mail Template ({invoke_name}) Success".format(invoke_name=_invoke_name)
                )
            )

        return
