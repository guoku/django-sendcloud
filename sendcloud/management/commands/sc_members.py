import click
import logging
from django.core.management.base import BaseCommand

from sendcloud.core.members import MemberAPI

logger = logging.getLogger('sendcloud')


class Command(BaseCommand):
    help = __doc__

    table_width = 120

    def add_arguments(self, parser):
        parser.add_argument(
            '-L', '--address-list',
            # action='store_true',
            # nargs='+',
            dest='mail_list',
            type=str,
            help='Send Cloud Mail Address List',
        )

        parser.add_argument(
            '-m', '--member',
            dest='member',
            type=str,
            help='Send Cloud Mail Address List Member'
        )

        parser.add_argument(
            '-a', '--add',
            dest='add',
            action='store_true',
            help='Add member into Address list',
        )

        parser.add_argument(
            '-d', '--delete',
            dest='delete',
            action='store_true',
            help="Delete member from Address list",
        )

        parser.add_argument(
            '-l', '--list',
            dest="list",
            action="store_true",
            help="List SendCloud Mail Address",
        )

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
            """| %-30s|%15s |%20s |%20s |%20s |""" %
            ("member", "name", "vars", "gmtCreated", "gmtUpdated",)
        )

        self._print_separator()

        for row in statistics:
            click.echo(
                """| %-30s|%15s |%20s |%20s |%20s |""" %
                (row['member'], row['name'], row['vars'], row['gmtCreated'], row['gmtUpdated'])
            )

        self._print_separator()

    def handle(self, *args, **options):
        _mail_list = options.get('mail_list')

        _list = options.get('list')
        _add = options.get('add')
        _delete = options.get('delete')

        _member = options.get('member')
        # logger.info(_address)

        if _list:
            r = MemberAPI().list(address=_mail_list)
            self._print_stats_dashboard(statistics=r)

        if _add:
            r = MemberAPI().add(address=_mail_list, members=[_member])
            self.stdout.write(
                self.style.SUCCESS(
                    "add member ({member}) Success".format(member=_member)
                )
            )

        if _delete:
            r = MemberAPI().delete(address=_mail_list, members=[_member])
            self.stdout.write(
                self.style.SUCCESS(
                    "delete member ({member}) Success".format(member=_member)
                )
            )
        return
