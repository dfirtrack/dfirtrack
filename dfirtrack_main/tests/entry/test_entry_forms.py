from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone
from dfirtrack_main.forms import EntryForm
from dfirtrack_main.models import System, Systemstatus

class EntryFormTestCase(TestCase):
    """ entry form tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_entry', password='z2B7MofdZ4suAn6AYGSo')

        # create object
        systemstatus_1 = Systemstatus.objects.create(systemstatus_name='systemstatus_1')

        # create object
        system_1 = System.objects.create(
            system_name='system_1',
            systemstatus = systemstatus_1,
            system_modify_time = timezone.now(),
            system_created_by_user_id = test_user,
            system_modified_by_user_id = test_user,
        )

    def test_entry_time_label(self):

        # get object
        form = EntryForm()
        # compare
        self.assertEquals(form.fields['entry_time'].label, 'Entry time (for sorting) (YYYY-MM-DD HH:MM:SS) (*)')

    def test_system_label(self):

        # get object
        form = EntryForm()
        # compare
        self.assertEquals(form.fields['system'].label, 'System (*)')

    def test_entry_sha1_label(self):

        # get object
        form = EntryForm()
        # compare
        self.assertEquals(form.fields['entry_sha1'].label, 'Entry sha1')

    def test_entry_date_label(self):

        # get object
        form = EntryForm()
        # compare
        self.assertEquals(form.fields['entry_date'].label, 'Entry date (YYYY-MM-DD)')

    def test_entry_utc_label(self):

        # get object
        form = EntryForm()
        # compare
        self.assertEquals(form.fields['entry_utc'].label, 'Entry time (for report) (HH:MM:SS)')

    def test_entry_system_label(self):

        # get object
        form = EntryForm()
        # compare
        self.assertEquals(form.fields['entry_system'].label, 'Entry system (for report)')

    def test_entry_type_label(self):

        # get object
        form = EntryForm()
        # compare
        self.assertEquals(form.fields['entry_type'].label, 'Entry type')

    def test_entry_content_label(self):

        # get object
        form = EntryForm()
        # compare
        self.assertEquals(form.fields['entry_content'].label, 'Entry content')

    def test_entry_note_label(self):

        # get object
        form = EntryForm()
        # compare
        self.assertEquals(form.fields['entry_note'].label, 'Entry note')

    def test_case_label(self):

        # get object
        form = EntryForm()
        # compare
        self.assertEquals(form.fields['case'].label, 'Case')

    def test_entry_time_empty(self):

        # get object
        form = EntryForm(data = {
            'entry_time': '',
        })
        # compare
        self.assertFalse(form.is_valid())

    def test_entry_time_filled(self):

        # define datetime string
        entry_time_string = '2001-02-03 12:34:56'
        # get object
        form = EntryForm(data = {
            'entry_time': entry_time_string,
        })
        # compare
        self.assertFalse(form.is_valid())

    def test_entry_time_filled_system_filled(self):

        # define datetime string
        entry_time_string = '2009-08-07 12:34:56'
        # get foreign key object id
        system_id = System.objects.get(system_name='system_1').system_id
        # get object
        form = EntryForm(data = {
            'entry_time': entry_time_string,
            'system': system_id,
        })
        # compare
        self.assertTrue(form.is_valid())

    def test_entry_sha1_proper_chars(self):

        # define datetime string
        entry_time_string = '2009-08-07 12:34:56'
        # get foreign key object id
        system_id = System.objects.get(system_name='system_1').system_id
        # get object
        form = EntryForm(data = {
            'entry_time': entry_time_string,
            'system': system_id,
            'entry_sha1': 'ssssssssssssssssssssssssssssssssssssssss',
        })
        # compare
        self.assertTrue(form.is_valid())

    def test_entry_sha1_too_many_chars(self):

        # define datetime string
        entry_time_string = '2009-08-07 12:34:56'
        # get foreign key object id
        system_id = System.objects.get(system_name='system_1').system_id
        # get object
        form = EntryForm(data = {
            'entry_time': entry_time_string,
            'system': system_id,
            'entry_sha1': 'sssssssssssssssssssssssssssssssssssssssss',
        })
        # compare
        self.assertFalse(form.is_valid())

    def test_entry_date_proper_chars(self):

        # define datetime string
        entry_time_string = '2009-08-07 12:34:56'
        # get foreign key object id
        system_id = System.objects.get(system_name='system_1').system_id
        # get object
        form = EntryForm(data = {
            'entry_time': entry_time_string,
            'system': system_id,
            'entry_date': 'dddddddddd',
        })
        # compare
        self.assertTrue(form.is_valid())

    def test_entry_date_too_many_chars(self):

        # define datetime string
        entry_time_string = '2009-08-07 12:34:56'
        # get foreign key object id
        system_id = System.objects.get(system_name='system_1').system_id
        # get object
        form = EntryForm(data = {
            'entry_time': entry_time_string,
            'system': system_id,
            'entry_date': 'ddddddddddd',
        })
        # compare
        self.assertFalse(form.is_valid())

    def test_entry_utc_proper_chars(self):

        # define datetime string
        entry_time_string = '2009-08-07 12:34:56'
        # get foreign key object id
        system_id = System.objects.get(system_name='system_1').system_id
        # get object
        form = EntryForm(data = {
            'entry_time': entry_time_string,
            'system': system_id,
            'entry_utc': 'uuuuuuuu',
        })
        # compare
        self.assertTrue(form.is_valid())

    def test_entry_utc_too_many_chars(self):

        # define datetime string
        entry_time_string = '2009-08-07 12:34:56'
        # get foreign key object id
        system_id = System.objects.get(system_name='system_1').system_id
        # get object
        form = EntryForm(data = {
            'entry_time': entry_time_string,
            'system': system_id,
            'entry_utc': 'uuuuuuuuu',
        })
        # compare
        self.assertFalse(form.is_valid())

    def test_entry_system_proper_chars(self):

        # define datetime string
        entry_time_string = '2009-08-07 12:34:56'
        # get foreign key object id
        system_id = System.objects.get(system_name='system_1').system_id
        # get object
        form = EntryForm(data = {
            'entry_time': entry_time_string,
            'system': system_id,
            'entry_system': 'ssssssssssssssssssssssssssssss',
        })
        # compare
        self.assertTrue(form.is_valid())

    def test_entry_system_too_many_chars(self):

        # define datetime string
        entry_time_string = '2009-08-07 12:34:56'
        # get foreign key object id
        system_id = System.objects.get(system_name='system_1').system_id
        # get object
        form = EntryForm(data = {
            'entry_time': entry_time_string,
            'system': system_id,
            'entry_system': 'sssssssssssssssssssssssssssssss',
        })
        # compare
        self.assertFalse(form.is_valid())

    def test_entry_type_proper_chars(self):

        # define datetime string
        entry_time_string = '2009-08-07 12:34:56'
        # get foreign key object id
        system_id = System.objects.get(system_name='system_1').system_id
        # get object
        form = EntryForm(data = {
            'entry_time': entry_time_string,
            'system': system_id,
            'entry_type': 'tttttttttttttttttttttttttttttt',
        })
        # compare
        self.assertTrue(form.is_valid())

    def test_entry_type_too_many_chars(self):

        # define datetime string
        entry_time_string = '2009-08-07 12:34:56'
        # get foreign key object id
        system_id = System.objects.get(system_name='system_1').system_id
        # get object
        form = EntryForm(data = {
            'entry_time': entry_time_string,
            'system': system_id,
            'entry_type': 'ttttttttttttttttttttttttttttttt',
        })
        # compare
        self.assertFalse(form.is_valid())
