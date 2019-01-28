import logging

import click
from django.core.management.base import BaseCommand
from sendcloud.core.address_list import AddressListAPI


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
            """| %-25s|%45s | %15s|%25s |%20s |%20s |""" %
            ("name", "address", 'memberCount', "description", "gmtCreated", "gmtUpdated",)
        )

        self._print_separator()

        for row in statistics:
            click.echo(
                """| %-25s|%45s | %15s|%25s |%20s |%20s |""" %
                (row['name'], row['address'], row["memberCount"],
                 row['description'].strip(), row['gmtCreated'], row['gmtUpdated'])
            )

        self._print_separator()

    def add_arguments(self, parser):
        parser.add_argument(
            '-n', '--address-name',
            dest='address',
            help='SendCloud Mail Address Name'
        )

        parser.add_argument(
            '-l', '--list',
            dest="list",
            action="store_true",
            help="List SendCloud Mail Address",
        )

    def handle(self, *args, **options):
        _list = options.get('list')
        _add = options.get('add')
        _address = options.get('address')

        if _list:
            r = AddressListAPI().list()
            # logger.info(r['info'])
            self._print_stats_dashboard(statistics=r['info']['dataList'])

        return
