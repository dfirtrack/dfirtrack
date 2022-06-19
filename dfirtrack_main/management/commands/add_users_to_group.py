import csv

from django.contrib.auth.models import Group, User
from django.core.management.base import BaseCommand

from dfirtrack_main.management.commands.check_file import check_file


class Command(BaseCommand):
    '''add users from file to group.'''

    # command help message
    help = 'Add users from file to group.'

    def add_arguments(self, parser):
        '''arguments'''

        # CSV file with at least username (string)
        parser.add_argument(
            'userfile',
            nargs=1,
            type=str,
            help='A comma-seperated CSV file containing user names in first column.',
        )

        # group name (string)
        parser.add_argument(
            'groupname', nargs=1, type=str, help='The group name to add the users.'
        )

    def handle(self, *args, **options):
        '''command logic'''

        # get filename from argument (type list)
        userfile = options['userfile'][0]

        # get group from argument (type list)
        groupname = options['groupname'][0]

        # TODO: [code] remove hardcoded arguments
        quotechar = "'"
        delimiter = ','

        # check file and get file handle
        usercsv = check_file(self, userfile, quotechar, delimiter)

        # if no file handle was returned
        if not usercsv:
            # return
            return

        # try to get group
        try:
            group = Group.objects.get(name=groupname)
        except Group.DoesNotExist:
            # write message to stdout
            self.stdout.write(self.style.ERROR(f'Group "{groupname}" does not exist.'))
            # return (group does not exist)
            return

        # read rows out of csv
        rows = csv.reader(usercsv, delimiter=delimiter, quotechar=quotechar)

        # iterate over rows
        for row in rows:

            # get values from CSV
            username_from_row = row[0]

            # try to get user
            try:
                # get user
                user = User.objects.get(username=username_from_row)
                # check if user already is member of group
                if user.groups.filter(name=groupname).exists():
                    # write message to stdout
                    self.stdout.write(
                        self.style.WARNING(
                            f'User "{username_from_row}" is already member of group "{groupname}".'
                        )
                    )
                # user is not member of group
                else:
                    # add user to group
                    group.user_set.add(user)
                    # write message to stdout
                    self.stdout.write(
                        self.style.SUCCESS(
                            f'User "{username_from_row}" successfully added to group "{groupname}".'
                        )
                    )
            # user does not exist
            except User.DoesNotExist:
                # write message to stdout
                self.stdout.write(
                    self.style.ERROR(f'User "{username_from_row}" does not exist.')
                )

        # close file
        usercsv.close()
