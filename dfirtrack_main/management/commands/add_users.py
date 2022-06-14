import csv

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError


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
            help='A comma-seperated CSV file containing user names and passwords (<USER>,<PASSWORD>).',
        )

        # is_staff switch (boolean)
        parser.add_argument(
            '--is_staff',
            action='store_true',
            help='Designates whether the users can access the admin site.',
        )

    def handle(self, *args, **options):
        '''command logic'''

        # get filename from argument (type list)
        userfile = options['userfile'][0]

        # get filename from argument (type list)
        is_staff = options['is_staff']

        # try to open file
        try:
            # open file
            usercsv = open(userfile)

        # file does not exist
        except FileNotFoundError:
            # write message to stdout
            self.stdout.write(self.style.ERROR(f'File "{userfile}" does not exist.'))
            # return (file does not exist)
            return

        # TODO: [code] remove hardcoded arguments
        quotechar = "'"
        delimiter = ','

        # read rows out of csv
        rows = csv.reader(usercsv, delimiter=delimiter, quotechar=quotechar)

        try:
            # try to iterate over rows
            for row in rows:
                # do nothing
                pass

        # wrong file type
        except UnicodeDecodeError:

            # write message to stdout
            self.stdout.write(
                self.style.ERROR(
                    f'File "{userfile}" does not seem to be a valid CSV file.'
                )
            )

            # return (wrong file type)
            return

        # jump to begin of file again after iterating in file check
        usercsv.seek(0)

        # read rows out of csv
        rows = csv.reader(usercsv, delimiter=delimiter, quotechar=quotechar)

        # iterate over rows
        for row in rows:

            # get values from CSV
            username_from_row = row[0]
            password_from_row = row[1]

            # try to create user
            try:
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
                    self.style.ERROR(f'User "{username_from_row}" already exists.')
                )

        # close file
        usercsv.close()
