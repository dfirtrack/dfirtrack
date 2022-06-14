import csv

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError


class Command(BaseCommand):
    help = 'Add users from file.'

    def add_arguments(self, parser):
        parser.add_argument('FILE', nargs=1, type=str)

    def handle(self, *args, **options):

        # get filename from argument (type list)
        userfile = options['FILE'][0]

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
                    username=username_from_row, password=password_from_row
                )
                # write message to stdout
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
