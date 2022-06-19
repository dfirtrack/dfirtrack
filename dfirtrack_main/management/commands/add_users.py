import csv

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db import transaction
from django.db.utils import DataError, IntegrityError

from dfirtrack_main.management.commands.check_file import check_file


class Command(BaseCommand):
    '''add users from file'''

    # command help message
    help = 'Add users from file.'

    def add_arguments(self, parser):
        '''arguments'''

        # CSV file path with username, password (string)
        parser.add_argument(
            'userfile',
            nargs=1,
            type=str,
            help='A CSV file containing user names and passwords (<USER>,<PASSWORD>).',
        )

        # is_staff switch (boolean)
        parser.add_argument(
            '-s',
            '--is_staff',
            action='store_true',
            help='Designates whether the users can access the admin site.',
        )

        # delimiter (choice)
        parser.add_argument(
            '-d',
            '--delimiter',
            choices=['COMMA', 'SEMICOLON', 'PIPE'],
            type=str,
            help='Delimiter used in CSV file (defaults to "COMMA").',
        )

        # quotechar (choice)
        parser.add_argument(
            '-q',
            '--quotechar',
            choices=['SINGLE', 'DOUBLE'],
            type=str,
            help='Quotechar used in CSV file (defaults to "SINGLE").',
        )

    def handle(self, *args, **options):
        '''command logic'''

        # get filename from argument (type list)
        userfile = options['userfile'][0]

        # get filename from argument (type boolean)
        is_staff = options['is_staff']

        # get delimiter
        delimiter = options['delimiter']

        # get quotechar
        quotechar = options['quotechar']

        # define delimiter
        if delimiter:
            if delimiter == 'COMMA':
                delimiter = ','
            if delimiter == 'SEMICOLON':
                delimiter = ';'
            if delimiter == 'PIPE':
                delimiter = '|'
        else:
            delimiter = ','

        # get quotechar
        if quotechar:
            if quotechar == 'SINGLE':
                quotechar = "'"
            if quotechar == 'DOUBLE':
                quotechar = '"'
        else:
            quotechar = "'"

        # check file and get file handle
        usercsv = check_file(self, userfile, delimiter, quotechar)

        # if no file handle was returned
        if not usercsv:
            # return
            return

        # read rows out of csv
        rows = csv.reader(usercsv, delimiter=delimiter, quotechar=quotechar)

        # iterate over rows
        for row in rows:

            # get values from CSV
            username_from_row = row[0]
            password_from_row = row[1]

            # try to create user
            try:
                # atomic transaction needed for tests in combination with forced exception
                with transaction.atomic():
                    User.objects.create_user(
                        username=username_from_row,
                        password=password_from_row,
                        is_staff=is_staff,
                    )
                # write message to stdout
                if is_staff:
                    self.stdout.write(
                        self.style.SUCCESS(
                            f'User "{username_from_row}" successfully created and added to staff.'
                        )
                    )
                else:
                    self.stdout.write(
                        self.style.SUCCESS(
                            f'User "{username_from_row}" successfully created.'
                        )
                    )
            # user already exists
            except IntegrityError:
                # write message to stdout
                self.stdout.write(
                    self.style.WARNING(
                        f'User "{username_from_row}" already exists (password not changed).'
                    )
                )
            # username invalid
            except DataError:
                # write message to stdout
                self.stdout.write(
                    self.style.ERROR(f'Username "{username_from_row}" is invalid.')
                )

        # close file
        usercsv.close()
