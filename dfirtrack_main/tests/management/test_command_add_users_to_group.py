from io import StringIO

from django.contrib.auth.models import Group, User
from django.core.management import call_command
from django.test import TestCase
from django.utils import timezone

from dfirtrack_main.tests.system_importer.test_system_importer_file_csv_check_content_file_system import (
    create_file_no_read_permission,
)


class CommandAddUsersToGroupTestCase(TestCase):
    """command tests"""

    def test_command_add_users_to_group_file_data(self):
        """test command"""

        # prepare string IO
        out = StringIO()
        # set import file
        importfile = 'dfirtrack_main/tests/management/files/11_file_data.csv'
        # set group name
        groupname = 'test_qroup'
        # call command
        call_command('add_users_to_group', importfile, groupname, stdout=out)
        # compare
        self.assertIn(
            f'File "{importfile}" does not seem to be a valid CSV file.',
            out.getvalue(),
        )

    def test_command_add_users_to_group_file_empty(self):
        """test command"""

        # prepare string IO
        out = StringIO()
        # set import file
        importfile = 'dfirtrack_main/tests/management/files/12_file_empty.csv'
        # set group name
        groupname = 'test_qroup'
        # call command
        call_command('add_users_to_group', importfile, groupname, stdout=out)
        # compare
        self.assertIn(f'File "{importfile}" is empty.', out.getvalue())

    def test_command_add_users_to_group_file_archive(self):
        """test command"""

        # prepare string IO
        out = StringIO()
        # set import file
        importfile = 'dfirtrack_main/tests/management/files/13_file_archive.zip'
        # set group name
        groupname = 'test_qroup'
        # call command
        call_command('add_users_to_group', importfile, groupname, stdout=out)
        # compare
        self.assertIn(
            f'File "{importfile}" does not seem to be a valid CSV file.',
            out.getvalue(),
        )

    def test_command_add_users_to_group_file_no_read_permission(self):
        """test command"""

        # prepare string IO
        out = StringIO()

        # get timestamp string
        t1 = timezone.now().strftime('%Y%m%d_%H%M%S')
        # set file system attributes
        csv_import_path = '/tmp'
        csv_import_filename = f'{t1}_command_add_users_to_group_no_read_permission.csv'

        # create file (uses function of system CSV importer tests)
        create_file_no_read_permission(csv_import_path, csv_import_filename)

        # set group name
        groupname = 'test_qroup'
        # set import file
        importfile = f'{csv_import_path}/{csv_import_filename}'

        # call command
        call_command('add_users_to_group', importfile, groupname, stdout=out)
        # compare
        self.assertIn(
            f'No read permission for file "{importfile}".',
            out.getvalue(),
        )

    def test_command_add_users_to_group_file_not_existent(self):
        """test command"""

        # prepare string IO
        out = StringIO()
        # set import file
        importfile = '14_file_not_existent.csv'
        # set group name
        groupname = 'test_qroup'
        # call command
        call_command('add_users_to_group', importfile, groupname, stdout=out)
        # compare
        self.assertIn(f'File "{importfile}" does not exist.', out.getvalue())

    def test_command_add_users_to_group_group_not_existent(self):
        """test command"""

        # prepare string IO
        out = StringIO()
        # set import file
        importfile = 'dfirtrack_main/tests/management/files/01_user_default.csv'
        # set group name
        groupname = 'test_qroup'
        # call command
        call_command('add_users_to_group', importfile, groupname, stdout=out)
        # compare
        self.assertIn(f'Group "{groupname}" does not exist.', out.getvalue())

    def test_command_add_users_to_group(self):
        """test command"""

        # create users
        user_211 = User.objects.create_user(
            username='user_211', password='QyxnxCyQU18Pkduu62Cc'
        )
        user_212 = User.objects.create_user(
            username='user_212', password='vZLVyqsaRQpTvUBviT4f'
        )
        # prepare string IO
        out = StringIO()
        # set import file
        importfile = 'dfirtrack_main/tests/management/files/21_user_group.csv'
        # set group name
        groupname = 'test_qroup'
        # create group
        testgroup = Group.objects.create(name=groupname)
        # add user to group
        testgroup.user_set.add(user_212)
        # compare
        self.assertFalse(user_211.groups.filter(name=groupname).exists())
        self.assertTrue(user_212.groups.filter(name=groupname).exists())
        # call command
        call_command('add_users_to_group', importfile, groupname, stdout=out)
        # compare
        self.assertIn(
            f'User "user_211" successfully added to group "{groupname}".',
            out.getvalue(),
        )
        self.assertIn(
            f'User "user_212" is already member of group "{groupname}".',
            out.getvalue(),
        )
        self.assertIn('User "user_213" does not exist.', out.getvalue())
        self.assertTrue(user_211.groups.filter(name=groupname).exists())
        self.assertTrue(user_212.groups.filter(name=groupname).exists())

    def test_command_add_users_to_group_delimiter_comma(self):
        """test command"""

        # create users
        user_031 = User.objects.create_user(
            username='user_031', password='QyxnxCyQU18Pkduu62Cc'
        )
        user_032 = User.objects.create_user(
            username='user_032', password='vZLVyqsaRQpTvUBviT4f'
        )
        # prepare string IO
        out = StringIO()
        # set import file
        importfile = 'dfirtrack_main/tests/management/files/03_user_comma.csv'
        # set group name
        groupname = 'test_qroup'
        # prepare arguments
        args = [importfile, groupname]
        opts = {'delimiter': 'COMMA'}
        # create group
        Group.objects.create(name=groupname)
        # compare
        self.assertFalse(user_031.groups.filter(name=groupname).exists())
        self.assertFalse(user_032.groups.filter(name=groupname).exists())
        # call command
        call_command('add_users_to_group', *args, **opts, stdout=out)
        # compare
        self.assertIn(
            f'User "user_031" successfully added to group "{groupname}".',
            out.getvalue(),
        )
        self.assertIn(
            f'User "user_032" successfully added to group "{groupname}".',
            out.getvalue(),
        )
        self.assertTrue(user_031.groups.filter(name=groupname).exists())
        self.assertTrue(user_032.groups.filter(name=groupname).exists())

    def test_command_add_users_to_group_delimiter_semicolon(self):
        """test command"""

        # create users
        user_041 = User.objects.create_user(
            username='user_041', password='QyxnxCyQU18Pkduu62Cc'
        )
        user_042 = User.objects.create_user(
            username='user_042', password='vZLVyqsaRQpTvUBviT4f'
        )
        # prepare string IO
        out = StringIO()
        # set import file
        importfile = 'dfirtrack_main/tests/management/files/04_user_semicolon.csv'
        # set group name
        groupname = 'test_qroup'
        # prepare arguments
        args = [importfile, groupname]
        opts = {'delimiter': 'SEMICOLON'}
        # create group
        Group.objects.create(name=groupname)
        # compare
        self.assertFalse(user_041.groups.filter(name=groupname).exists())
        self.assertFalse(user_042.groups.filter(name=groupname).exists())
        # call command
        call_command('add_users_to_group', *args, **opts, stdout=out)
        # compare
        self.assertIn(
            f'User "user_041" successfully added to group "{groupname}".',
            out.getvalue(),
        )
        self.assertIn(
            f'User "user_042" successfully added to group "{groupname}".',
            out.getvalue(),
        )
        self.assertTrue(user_041.groups.filter(name=groupname).exists())
        self.assertTrue(user_042.groups.filter(name=groupname).exists())

    def test_command_add_users_to_group_delimiter_pipe(self):
        """test command"""

        # create users
        user_051 = User.objects.create_user(
            username='user_051', password='QyxnxCyQU18Pkduu62Cc'
        )
        user_052 = User.objects.create_user(
            username='user_052', password='vZLVyqsaRQpTvUBviT4f'
        )
        # prepare string IO
        out = StringIO()
        # set import file
        importfile = 'dfirtrack_main/tests/management/files/05_user_pipe.csv'
        # set group name
        groupname = 'test_qroup'
        # prepare arguments
        args = [importfile, groupname]
        opts = {'delimiter': 'PIPE'}
        # create group
        Group.objects.create(name=groupname)
        # compare
        self.assertFalse(user_051.groups.filter(name=groupname).exists())
        self.assertFalse(user_052.groups.filter(name=groupname).exists())
        # call command
        call_command('add_users_to_group', *args, **opts, stdout=out)
        # compare
        self.assertIn(
            f'User "user_051" successfully added to group "{groupname}".',
            out.getvalue(),
        )
        self.assertIn(
            f'User "user_052" successfully added to group "{groupname}".',
            out.getvalue(),
        )
        self.assertTrue(user_051.groups.filter(name=groupname).exists())
        self.assertTrue(user_052.groups.filter(name=groupname).exists())

    def test_command_add_users_to_group_quotechar_single(self):
        """test command"""

        # create users
        user_061 = User.objects.create_user(
            username='user_061', password='QyxnxCyQU18Pkduu62Cc'
        )
        user_062 = User.objects.create_user(
            username='user_062', password='vZLVyqsaRQpTvUBviT4f'
        )
        # prepare string IO
        out = StringIO()
        # set import file
        importfile = 'dfirtrack_main/tests/management/files/06_user_single.csv'
        # set group name
        groupname = 'test_qroup'
        # prepare arguments
        args = [importfile, groupname]
        opts = {'quotechar': 'SINGLE'}
        # create group
        Group.objects.create(name=groupname)
        # compare
        self.assertFalse(user_061.groups.filter(name=groupname).exists())
        self.assertFalse(user_062.groups.filter(name=groupname).exists())
        # call command
        call_command('add_users_to_group', *args, **opts, stdout=out)
        # compare
        self.assertIn(
            f'User "user_061" successfully added to group "{groupname}".',
            out.getvalue(),
        )
        self.assertIn(
            f'User "user_062" successfully added to group "{groupname}".',
            out.getvalue(),
        )
        self.assertTrue(user_061.groups.filter(name=groupname).exists())
        self.assertTrue(user_062.groups.filter(name=groupname).exists())

    def test_command_add_users_to_group_quotechar_double(self):
        """test command"""

        # create users
        user_071 = User.objects.create_user(
            username='user_071', password='QyxnxCyQU18Pkduu62Cc'
        )
        user_072 = User.objects.create_user(
            username='user_072', password='vZLVyqsaRQpTvUBviT4f'
        )
        # prepare string IO
        out = StringIO()
        # set import file
        importfile = 'dfirtrack_main/tests/management/files/07_user_double.csv'
        # set group name
        groupname = 'test_qroup'
        # prepare arguments
        args = [importfile, groupname]
        opts = {'quotechar': 'DOUBLE'}
        # create group
        Group.objects.create(name=groupname)
        # compare
        self.assertFalse(user_071.groups.filter(name=groupname).exists())
        self.assertFalse(user_072.groups.filter(name=groupname).exists())
        # call command
        call_command('add_users_to_group', *args, **opts, stdout=out)
        # compare
        self.assertIn(
            f'User "user_071" successfully added to group "{groupname}".',
            out.getvalue(),
        )
        self.assertIn(
            f'User "user_072" successfully added to group "{groupname}".',
            out.getvalue(),
        )
        self.assertTrue(user_071.groups.filter(name=groupname).exists())
        self.assertTrue(user_072.groups.filter(name=groupname).exists())
