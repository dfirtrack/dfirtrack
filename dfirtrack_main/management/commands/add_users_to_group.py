import csv

from django.contrib.auth.models import Group, User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Add users from file to group.'

    def add_arguments(self, parser):
        parser.add_argument('FILE', nargs=1, type=str)
        parser.add_argument('GROUP', nargs=1, type=str)

    def handle(self, *args, **options):

        # get filename from argument (type list)
        userfile = options['FILE'][0]

        # get group from argument (type list)
        groupname = options['GROUP'][0]

        # try to get group
        try:
            group = Group.objects.get(name=groupname)
        except Group.DoesNotExist:
            # write message to stdout
            self.stdout.write(self.style.ERROR(f'Group "{groupname}" does not exist.'))
            # return (group does not exist)
            return

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
            self.stdout.write(self.style.ERROR(f'File "{userfile}" does not seem to be a valid CSV file.'))

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

            # try to get user
            try:
                user = User.objects.get(username=username_from_row)
                # add user to group
                group.user_set.add(user)
                # write message to stdout
                self.stdout.write(self.style.SUCCESS(f'User "{username_from_row}" successfully added to group "{groupname}".'))
            # user does not exist
            except User.DoesNotExist:
                # write message to stdout
                self.stdout.write(self.style.ERROR(f'User "{username_from_row}" does not exist.'))

        # close file
        usercsv.close()
