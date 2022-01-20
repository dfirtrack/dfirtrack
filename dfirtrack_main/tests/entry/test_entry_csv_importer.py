import hashlib
from datetime import datetime

from django.contrib.auth.models import User
from django.test import TestCase
from django.utils.timezone import get_current_timezone
from mock import mock_open, patch

from dfirtrack_main.importer.file.csv_entry_import import csv_entry_import_async
from dfirtrack_main.models import Entry, System, Systemstatus, Tag, Tagcolor


class EntryCsvImporterTestCase(TestCase):
    @classmethod
    def setUpTestData(self):

        # create user
        test_user = User.objects.create_user(
            username='testuser_entry', password='GB1237lbSGB13jXjCRoL'
        )

        # create object
        systemstatus_1 = Systemstatus.objects.create(systemstatus_name='systemstatus_1')

        # create object
        System.objects.create(
            system_name='system_1',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )

        # create object
        tagcolor = Tagcolor.objects.create(tagcolor_name='tagcolor_name_1')

        # create object
        Tag.objects.create(
            tag_name='tag_1',
            tagcolor=tagcolor,
            tag_modified_by_user_id=test_user,
        )

    def execute_csv_entry_import_async(
        self, csv_string, delimiter=None, quotechar=None
    ):
        # get objects
        system_id = System.objects.get(system_name='system_1').system_id
        test_user = User.objects.get(username='testuser_entry')
        # prepare import argument field_mapping
        field_mapping = {
            'entry_time': 0,
            'entry_type': 1,
            'entry_content': 2,
            'entry_tag': 3,
        }
        # mockup file
        test_file_path = '/tmp/test.csv'
        # set delimiter and quotechar
        if not delimiter:
            delimiter = ','
        if not quotechar:
            quotechar = '"'

        with patch("builtins.open", mock_open(read_data=csv_string)) as mock_file:
            with patch("os.remove", return_value=True) as mock_os:
                # execute csv entry import
                csv_entry_import_async(
                    system_id,
                    test_file_path,
                    field_mapping,
                    test_user,
                    delimiter,
                    quotechar,
                )

                # check mockup file access
                mock_file.assert_called_with(test_file_path, newline='')
                mock_os.assert_called_with(test_file_path)

    def test_upload_csv_one_entry(self):
        """test upload csv one entry"""

        # login
        self.client.login(username='testuser_entry', password='GB1237lbSGB13jXjCRoL')
        # prepare csv string
        now = datetime.now(tz=get_current_timezone())
        csv_string = f'datetime,type,message\n"{now}",single_test,"Lorem ipsum","[]"'
        # run task
        self.execute_csv_entry_import_async(csv_string)

        # get messages
        response = self.client.get('/entry/')
        messages = list(response.context['messages'])
        # get created entry
        entries = Entry.objects.filter(entry_time=str(now))
        # check
        self.assertEqual(len(entries), 1)
        self.assertEqual(len(messages), 1)
        self.assertEqual(entries[0].entry_type, 'single_test')
        self.assertEqual(entries[0].entry_content, 'Lorem ipsum')
        self.assertEqual(str(messages[0]), 'Imported 1 entries for system "system_1".')

    def test_upload_csv_entry_sha1_calculation(self):
        """test upload one entry sha1 calculation"""

        # get system
        system_id = System.objects.get(system_name='system_1').system_id

        # prepare csv string
        now = datetime.now(tz=get_current_timezone())
        csv_string = f'datetime,type,message\n"{now}",sha1_test,"Lorem ipsum","[]"'
        # calculate hash
        m = hashlib.sha1()  # nosec
        m.update(str(system_id).encode())
        m.update(now.isoformat().encode())
        m.update(b'sha1_test')
        m.update(b'Lorem ipsum')

        # start task
        self.execute_csv_entry_import_async(csv_string)

        # get created entry
        entry = Entry.objects.get(entry_sha1=m.hexdigest())
        # check
        self.assertIsNotNone(entry)
        self.assertEqual(entry.entry_type, 'sha1_test')

    def test_upload_csv_entry_tag(self):
        """test upload one entry sha1 calculation"""

        # get system
        system_id = System.objects.get(system_name='system_1').system_id

        # prepare csv string
        now = datetime.now(tz=get_current_timezone())
        csv_string = (
            f'datetime,type,message,tag\n"{now}",sha1_test,"Lorem ipsum","[\'tag_1\']"'
        )
        # calculate hash
        m = hashlib.sha1()  # nosec
        m.update(str(system_id).encode())
        m.update(now.isoformat().encode())
        m.update(b'sha1_test')
        m.update(b'Lorem ipsum')

        # start task
        self.execute_csv_entry_import_async(
            csv_string,
        )

        # get created entry
        entry = Entry.objects.get(entry_sha1=m.hexdigest())
        # check
        self.assertEqual(len(entry.tag.all()), 1)
        self.assertEqual(entry.tag.all()[0].tag_name, 'tag_1')

    def test_upload_csv_duplicated_entries(self):
        """test upload duplicated entries"""

        # login
        self.client.login(username='testuser_entry', password='GB1237lbSGB13jXjCRoL')
        # prepare csv string
        now = datetime.now(tz=get_current_timezone())
        csv_string = f'datetime,type,message\n"{now}",dup_test,"Lorem ipsum","[]"\n"{now}",dup_test,"Lorem ipsum","[]"'

        # execute
        self.execute_csv_entry_import_async(csv_string)

        # get messages
        response = self.client.get('/entry/')
        messages = list(response.context['messages'])
        # get created entry
        entries = Entry.objects.filter(entry_time=str(now))
        # check
        self.assertEqual(len(entries), 1)
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]),
            'Imported 1 entries for system "system_1". Removed 1 duplicates.',
        )

    def test_upload_csv_faulty_entry(self):
        """test upload duplicated entries"""

        # login
        self.client.login(username='testuser_entry', password='GB1237lbSGB13jXjCRoL')
        # prepare csv string
        csv_string = 'datetime,type,message\n"12345679",faulty_test,"Lorem ipsum","[]"'

        # execute
        self.execute_csv_entry_import_async(csv_string)

        # get messages
        response = self.client.get('/entry/')
        messages = list(response.context['messages'])
        # check
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]), 'Could not import 1 of 1 entries for system "system_1".'
        )

    def test_upload_csv_file_not_found(self):

        # login
        self.client.login(username='testuser_entry', password='GB1237lbSGB13jXjCRoL')
        # get objects
        system_id = System.objects.get(system_name='system_1').system_id
        test_user = User.objects.get(username='testuser_entry')
        # prepare import argument filed_mapping
        field_mapping = {
            'entry_time': 0,
            'entry_type': 1,
            'entry_content': 2,
        }
        # mockup file
        test_file_path = '/tmp/file_not_found_test.csv'

        # execute csv entry import
        csv_entry_import_async(
            system_id,
            test_file_path,
            field_mapping,
            test_user,
            delimiter='"',
            quotechar=',',
        )

        # check mockup file access

        response = self.client.get('/entry/')
        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]),
            "Could not import the CSV file. Maybe the upload wasn't successful or the file was deleted.",
        )

    def test_upload_custom_delimiter(self):
        """test upload duplicated entries"""

        # login
        self.client.login(username='testuser_entry', password='GB1237lbSGB13jXjCRoL')
        # prepare csv string
        now = datetime.now(tz=get_current_timezone())
        csv_string = f'datetime|type|message\n"{now}"|dup_test|"Lorem ipsum"|[]'

        # execute
        self.execute_csv_entry_import_async(csv_string, delimiter='|')

        # get messages
        response = self.client.get('/entry/')
        messages = list(response.context['messages'])
        # get created entry
        entries = Entry.objects.filter(entry_time=str(now))
        # check
        self.assertEqual(len(entries), 1)
        self.assertEqual(len(messages), 1)

    def test_upload_custom_quotechar(self):
        """test upload duplicated entries"""

        # login
        self.client.login(username='testuser_entry', password='GB1237lbSGB13jXjCRoL')
        # prepare csv string
        now = datetime.now(tz=get_current_timezone())
        csv_string = f"datetime,type,message\n'{now}',dup_test,'Lorem ipsum',[]"

        # execute
        self.execute_csv_entry_import_async(csv_string, quotechar="'")

        # get messages
        response = self.client.get('/entry/')
        messages = list(response.context['messages'])
        # get created entry
        entries = Entry.objects.filter(entry_time=str(now))
        # check
        self.assertEqual(len(entries), 1)
        self.assertEqual(len(messages), 1)
