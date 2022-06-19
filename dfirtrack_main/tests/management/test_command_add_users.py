from io import StringIO

from django.contrib.auth.models import User
from django.core.management import call_command
from django.test import TestCase
from django.utils import timezone

from dfirtrack_main.tests.system_importer.test_system_importer_file_csv_check_content_file_system import (
    create_file_no_read_permission,
)


class CommandAddUsersTestCase(TestCase):
    """command tests"""

    def test_command_add_users_file_data(self):
        """test command"""

        # prepare string IO
        out = StringIO()
        # set import file
        importfile = 'dfirtrack_main/tests/management/files/11_file_data.csv'
        # call command
        call_command('add_users', importfile, stdout=out)
        # compare
        self.assertIn(
            f'\x1b[31;1mFile "{importfile}" does not seem to be a valid CSV file.\x1b[0m\n',
            out.getvalue(),
        )

    def test_command_add_users_file_empty(self):
        """test command"""

        # prepare string IO
        out = StringIO()
        # set import file
        importfile = 'dfirtrack_main/tests/management/files/12_file_empty.csv'
        # call command
        call_command('add_users', importfile, stdout=out)
        # compare
        self.assertIn(
            f'\x1b[31;1mFile "{importfile}" is empty.\x1b[0m\n', out.getvalue()
        )

    def test_command_add_users_file_archive(self):
        """test command"""

        # prepare string IO
        out = StringIO()
        # set import file
        importfile = 'dfirtrack_main/tests/management/files/13_file_archive.zip'
        # call command
        call_command('add_users', importfile, stdout=out)
        # compare
        self.assertIn(
            f'\x1b[31;1mFile "{importfile}" does not seem to be a valid CSV file.\x1b[0m\n',
            out.getvalue(),
        )

    def test_command_add_users_file_no_read_permission(self):
        """test command"""

        # prepare string IO
        out = StringIO()

        # get timestamp string
        t1 = timezone.now().strftime('%Y%m%d_%H%M%S')
        # set file system attributes
        csv_import_path = '/tmp'
        csv_import_filename = f'{t1}_command_add_users_no_read_permission.csv'

        # create file (uses function of system CSV importer tests)
        create_file_no_read_permission(csv_import_path, csv_import_filename)

        # set import file
        importfile = f'{csv_import_path}/{csv_import_filename}'

        # call command
        call_command('add_users', importfile, stdout=out)
        # compare
        self.assertIn(
            f'\x1b[31;1mNo read permission for file "{importfile}".\x1b[0m\n',
            out.getvalue(),
        )

    def test_command_add_users_file_not_existent(self):
        """test command"""

        # prepare string IO
        out = StringIO()
        # set import file
        importfile = '14_file_not_existent.csv'
        # call command
        call_command('add_users', importfile, stdout=out)
        # compare
        self.assertEquals(
            f'\x1b[31;1mFile "{importfile}" does not exist.\x1b[0m\n', out.getvalue()
        )

    def test_command_add_users(self):
        """test command"""

        # create user
        User.objects.create_user(username='user_013', password='gfRW8eVN7F68ayGtzXjV')
        # prepare string IO
        out = StringIO()
        # set import file
        importfile = 'dfirtrack_main/tests/management/files/01_user_default.csv'
        # compare
        self.assertFalse(User.objects.filter(username='user_011').exists())
        self.assertFalse(User.objects.filter(username='user_012').exists())
        self.assertTrue(User.objects.filter(username='user_013').exists())
        # call command
        call_command('add_users', importfile, stdout=out)
        # create long user name string
        username = 'u' * 151
        # compare
        self.assertIn(
            '\x1b[32;1mUser "user_011" successfully created.\x1b[0m\n', out.getvalue()
        )
        self.assertIn(
            '\x1b[32;1mUser "user_012" successfully created.\x1b[0m\n', out.getvalue()
        )
        self.assertIn(
            '\x1b[33;1mUser "user_013" already exists (password not changed).\x1b[0m\n',
            out.getvalue(),
        )
        self.assertIn(
            f'\x1b[31;1mUsername "{username}" is invalid.\x1b[0m\n', out.getvalue()
        )
        self.assertTrue(User.objects.filter(username='user_011').exists())
        self.assertTrue(User.objects.filter(username='user_012').exists())
        self.assertTrue(User.objects.filter(username='user_013').exists())

    def test_command_add_users_staff(self):
        """test command"""

        # create user
        User.objects.create_user(username='user_023', password='AVoq4rAAH6SliUJnF9nP')
        # prepare string IO
        out = StringIO()
        # set import file
        importfile = 'dfirtrack_main/tests/management/files/02_user_staff.csv'
        # prepare arguments
        args = [importfile]
        opts = {'is_staff': True}
        # compare
        self.assertFalse(User.objects.filter(username='user_021').exists())
        self.assertFalse(User.objects.filter(username='user_022').exists())
        self.assertTrue(User.objects.filter(username='user_023').exists())
        # call command
        call_command('add_users', *args, **opts, stdout=out)
        # compare
        self.assertIn(
            '\x1b[32;1mUser "user_021" successfully created and added to staff.\x1b[0m\n',
            out.getvalue(),
        )
        self.assertIn(
            '\x1b[32;1mUser "user_022" successfully created and added to staff.\x1b[0m\n',
            out.getvalue(),
        )
        self.assertIn(
            '\x1b[33;1mUser "user_023" already exists (password not changed).\x1b[0m\n',
            out.getvalue(),
        )
        self.assertTrue(User.objects.filter(username='user_021').exists())
        self.assertTrue(User.objects.filter(username='user_022').exists())
        self.assertTrue(User.objects.filter(username='user_023').exists())
        self.assertTrue(User.objects.get(username='user_021').is_staff)
        self.assertTrue(User.objects.get(username='user_022').is_staff)
        self.assertFalse(User.objects.get(username='user_023').is_staff)

    def test_command_add_users_delimiter_comma(self):
        """test command"""

        # prepare string IO
        out = StringIO()
        # set import file
        importfile = 'dfirtrack_main/tests/management/files/03_user_comma.csv'
        # prepare arguments
        args = [importfile]
        opts = {'delimiter': 'COMMA'}
        # compare
        self.assertFalse(User.objects.filter(username='user_031').exists())
        self.assertFalse(User.objects.filter(username='user_032').exists())
        # call command
        call_command('add_users', *args, **opts, stdout=out)
        # compare
        self.assertIn(
            '\x1b[32;1mUser "user_031" successfully created.\x1b[0m\n', out.getvalue()
        )
        self.assertIn(
            '\x1b[32;1mUser "user_032" successfully created.\x1b[0m\n', out.getvalue()
        )
        self.assertTrue(User.objects.filter(username='user_031').exists())
        self.assertTrue(User.objects.filter(username='user_032').exists())

    def test_command_add_users_delimiter_semicolon(self):
        """test command"""

        # prepare string IO
        out = StringIO()
        # set import file
        importfile = 'dfirtrack_main/tests/management/files/04_user_semicolon.csv'
        # prepare arguments
        args = [importfile]
        opts = {'delimiter': 'SEMICOLON'}
        # compare
        self.assertFalse(User.objects.filter(username='user_041').exists())
        self.assertFalse(User.objects.filter(username='user_042').exists())
        # call command
        call_command('add_users', *args, **opts, stdout=out)
        # compare
        self.assertIn(
            '\x1b[32;1mUser "user_041" successfully created.\x1b[0m\n', out.getvalue()
        )
        self.assertIn(
            '\x1b[32;1mUser "user_042" successfully created.\x1b[0m\n', out.getvalue()
        )
        self.assertTrue(User.objects.filter(username='user_041').exists())
        self.assertTrue(User.objects.filter(username='user_042').exists())

    def test_command_add_users_delimiter_pipe(self):
        """test command"""

        # prepare string IO
        out = StringIO()
        # set import file
        importfile = 'dfirtrack_main/tests/management/files/05_user_pipe.csv'
        # prepare arguments
        args = [importfile]
        opts = {'delimiter': 'PIPE'}
        # compare
        self.assertFalse(User.objects.filter(username='user_051').exists())
        self.assertFalse(User.objects.filter(username='user_052').exists())
        # call command
        call_command('add_users', *args, **opts, stdout=out)
        # compare
        self.assertIn(
            '\x1b[32;1mUser "user_051" successfully created.\x1b[0m\n', out.getvalue()
        )
        self.assertIn(
            '\x1b[32;1mUser "user_052" successfully created.\x1b[0m\n', out.getvalue()
        )
        self.assertTrue(User.objects.filter(username='user_051').exists())
        self.assertTrue(User.objects.filter(username='user_052').exists())

    def test_command_add_users_quotechar_single(self):
        """test command"""

        # prepare string IO
        out = StringIO()
        # set import file
        importfile = 'dfirtrack_main/tests/management/files/06_user_single.csv'
        # prepare arguments
        args = [importfile]
        opts = {'quotechar': 'SINGLE'}
        # compare
        self.assertFalse(User.objects.filter(username='user_061').exists())
        self.assertFalse(User.objects.filter(username='user_062').exists())
        # call command
        call_command('add_users', *args, **opts, stdout=out)
        # compare
        self.assertIn(
            '\x1b[32;1mUser "user_061" successfully created.\x1b[0m\n', out.getvalue()
        )
        self.assertIn(
            '\x1b[32;1mUser "user_062" successfully created.\x1b[0m\n', out.getvalue()
        )
        self.assertTrue(User.objects.filter(username='user_061').exists())
        self.assertTrue(User.objects.filter(username='user_062').exists())

    def test_command_add_users_quotechar_double(self):
        """test command"""

        # prepare string IO
        out = StringIO()
        # set import file
        importfile = 'dfirtrack_main/tests/management/files/07_user_double.csv'
        # prepare arguments
        args = [importfile]
        opts = {'quotechar': 'DOUBLE'}
        # compare
        self.assertFalse(User.objects.filter(username='user_071').exists())
        self.assertFalse(User.objects.filter(username='user_072').exists())
        # call command
        call_command('add_users', *args, **opts, stdout=out)
        # compare
        self.assertIn(
            '\x1b[32;1mUser "user_071" successfully created.\x1b[0m\n', out.getvalue()
        )
        self.assertIn(
            '\x1b[32;1mUser "user_072" successfully created.\x1b[0m\n', out.getvalue()
        )
        self.assertTrue(User.objects.filter(username='user_071').exists())
        self.assertTrue(User.objects.filter(username='user_072').exists())
