import urllib.parse
import uuid
from unittest.mock import patch

from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.utils import timezone

from dfirtrack_main.models import Case, Entry, System, Systemstatus


class EntryViewTestCase(TestCase):
    """entry view tests"""

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(
            username='testuser_entry', password='GBabI7lbSGB13jXjCRoL'
        )

        # create object
        systemstatus_1 = Systemstatus.objects.create(systemstatus_name='systemstatus_1')

        # create object
        system_1 = System.objects.create(
            system_name='system_1',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )

        # create object
        Entry.objects.create(
            system=system_1,
            entry_time=timezone.now(),
            entry_note='test_entry_view_entry',
            entry_created_by_user_id=test_user,
            entry_modified_by_user_id=test_user,
        )

    def test_entry_list_not_logged_in(self):
        """test list view"""

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/entry/', safe='')
        # get response
        response = self.client.get('/entry/', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_entry_list_logged_in(self):
        """test list view"""

        # login testuser
        self.client.login(username='testuser_entry', password='GBabI7lbSGB13jXjCRoL')
        # get response
        response = self.client.get('/entry/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_entry_list_template(self):
        """test list view"""

        # login testuser
        self.client.login(username='testuser_entry', password='GBabI7lbSGB13jXjCRoL')
        # get response
        response = self.client.get('/entry/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/entry/entry_list.html')

    def test_entry_list_get_user_context(self):
        """test list view"""

        # login testuser
        self.client.login(username='testuser_entry', password='GBabI7lbSGB13jXjCRoL')
        # get response
        response = self.client.get('/entry/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_entry')

    def test_entry_list_redirect(self):
        """test list view"""

        # login testuser
        self.client.login(username='testuser_entry', password='GBabI7lbSGB13jXjCRoL')
        # create url
        destination = urllib.parse.quote('/entry/', safe='/')
        # get response
        response = self.client.get('/entry', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )

    def test_entry_detail_not_logged_in(self):
        """test detail view"""

        # get object
        entry_1 = Entry.objects.get(
            entry_note='test_entry_view_entry',
        )
        # create url
        destination = '/login/?next=' + urllib.parse.quote(
            '/entry/' + str(entry_1.entry_id) + '/', safe=''
        )
        # get response
        response = self.client.get('/entry/' + str(entry_1.entry_id) + '/', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_entry_detail_logged_in(self):
        """test detail view"""

        # get object
        entry_1 = Entry.objects.get(
            entry_note='test_entry_view_entry',
        )
        # login testuser
        self.client.login(username='testuser_entry', password='GBabI7lbSGB13jXjCRoL')
        # get response
        response = self.client.get('/entry/' + str(entry_1.entry_id) + '/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_entry_detail_template(self):
        """test detail view"""

        # get object
        entry_1 = Entry.objects.get(
            entry_note='test_entry_view_entry',
        )
        # login testuser
        self.client.login(username='testuser_entry', password='GBabI7lbSGB13jXjCRoL')
        # get response
        response = self.client.get('/entry/' + str(entry_1.entry_id) + '/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/entry/entry_detail.html')

    def test_entry_detail_get_user_context(self):
        """test detail view"""

        # get object
        entry_1 = Entry.objects.get(
            entry_note='test_entry_view_entry',
        )
        # login testuser
        self.client.login(username='testuser_entry', password='GBabI7lbSGB13jXjCRoL')
        # get response
        response = self.client.get('/entry/' + str(entry_1.entry_id) + '/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_entry')

    def test_entry_detail_redirect(self):
        """test detail view"""

        # get object
        entry_1 = Entry.objects.get(
            entry_note='test_entry_view_entry',
        )
        # login testuser
        self.client.login(username='testuser_entry', password='GBabI7lbSGB13jXjCRoL')
        # create url
        destination = urllib.parse.quote(
            '/entry/' + str(entry_1.entry_id) + '/', safe='/'
        )
        # get response
        response = self.client.get('/entry/' + str(entry_1.entry_id), follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )

    def test_entry_add_not_logged_in(self):
        """test add view"""

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/entry/add/', safe='')
        # get response
        response = self.client.get('/entry/add/', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_entry_add_logged_in(self):
        """test add view"""

        # login testuser
        self.client.login(username='testuser_entry', password='GBabI7lbSGB13jXjCRoL')
        # get response
        response = self.client.get('/entry/add/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_entry_add_system_selected(self):
        """test add view"""

        # login testuser
        self.client.login(username='testuser_entry', password='GBabI7lbSGB13jXjCRoL')
        # get object
        system_id = System.objects.get(system_name='system_1').system_id
        # get response
        response = self.client.get('/entry/add/?system=' + str(system_id))
        # compare
        self.assertEqual(response.status_code, 200)

    def test_entry_add_template(self):
        """test add view"""

        # login testuser
        self.client.login(username='testuser_entry', password='GBabI7lbSGB13jXjCRoL')
        # get response
        response = self.client.get('/entry/add/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/generic_form.html')

    def test_entry_add_get_user_context(self):
        """test add view"""

        # login testuser
        self.client.login(username='testuser_entry', password='GBabI7lbSGB13jXjCRoL')
        # get response
        response = self.client.get('/entry/add/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_entry')

    def test_entry_add_redirect(self):
        """test add view"""

        # login testuser
        self.client.login(username='testuser_entry', password='GBabI7lbSGB13jXjCRoL')
        # create url
        destination = urllib.parse.quote('/entry/add/', safe='/')
        # get response
        response = self.client.get('/entry/add', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )

    def test_entry_add_post_redirect(self):
        """test add view"""

        # login testuser
        self.client.login(username='testuser_entry', password='GBabI7lbSGB13jXjCRoL')
        # get object
        system_id = System.objects.get(system_name='system_1').system_id
        # create post data
        data_dict = {
            'system': system_id,
            'entry_time': '2013-12-11 23:45:01',
            'entry_note': 'test_entry_view_entry_2',
        }
        # get response
        response = self.client.post('/entry/add/', data_dict)
        # create url
        destination = urllib.parse.quote('/system/' + str(system_id) + '/', safe='/')
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_entry_add_post_invalid_reload(self):
        """test add view"""

        # login testuser
        self.client.login(username='testuser_entry', password='GBabI7lbSGB13jXjCRoL')
        # create post data
        data_dict = {}
        # get response
        response = self.client.post('/entry/add/', data_dict)
        # compare
        self.assertEqual(response.status_code, 200)

    def test_entry_add_post_invalid_template(self):
        """test add view"""

        # login testuser
        self.client.login(username='testuser_entry', password='GBabI7lbSGB13jXjCRoL')
        # create post data
        data_dict = {}
        # get response
        response = self.client.post('/entry/add/', data_dict)
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/generic_form.html')

    def test_entry_add_post_duplicate(self):
        """test add view"""

        # login testuser
        self.client.login(username='testuser_entry', password='GBabI7lbSGB13jXjCRoL')
        # get time in different formats to avoid runtime warnings
        t1_datetime = timezone.now().replace(microsecond=0)
        t1_string = t1_datetime.strftime('%Y-%m-%d %H:%M:%S')
        # get user
        test_user = User.objects.get(username='testuser_entry')
        # get object
        system_1 = System.objects.get(system_name='system_1')
        # create object
        Entry.objects.create(
            system=system_1,
            entry_time=t1_datetime,
            entry_type='duplicate_entry_1',
            entry_content='duplicate_entry_1',
            entry_note='duplicate_entry_1',
            entry_created_by_user_id=test_user,
            entry_modified_by_user_id=test_user,
        )
        # get object
        duplicate_entry = Entry.objects.filter(entry_note='duplicate_entry_1')
        # compare
        self.assertEqual(len(duplicate_entry), 1)
        # create post data
        data_dict = {
            'system': system_1.system_id,
            'entry_time': t1_string,
            'entry_type': 'duplicate_entry_1',
            'entry_content': 'duplicate_entry_1',
            'entry_note': 'duplicate_entry_1',
        }
        # get response
        response = self.client.post('/entry/add/', data_dict)
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dfirtrack_main/generic_form.html')
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Entry with same content already exists')
        self.assertEqual(messages[0].level_tag, 'warning')
        # get object
        duplicate_entry = Entry.objects.filter(entry_note='duplicate_entry_1')
        # compare
        self.assertEqual(len(duplicate_entry), 1)

    def test_entry_edit_not_logged_in(self):
        """test edit view"""

        # get object
        entry_1 = Entry.objects.get(
            entry_note='test_entry_view_entry',
        )
        # create url
        destination = '/login/?next=' + urllib.parse.quote(
            '/entry/' + str(entry_1.entry_id) + '/edit/', safe=''
        )
        # get response
        response = self.client.get(
            '/entry/' + str(entry_1.entry_id) + '/edit/', follow=True
        )
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_entry_edit_logged_in(self):
        """test edit view"""

        # get object
        entry_1 = Entry.objects.get(
            entry_note='test_entry_view_entry',
        )
        # login testuser
        self.client.login(username='testuser_entry', password='GBabI7lbSGB13jXjCRoL')
        # get response
        response = self.client.get('/entry/' + str(entry_1.entry_id) + '/edit/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_entry_edit_template(self):
        """test edit view"""

        # get object
        entry_1 = Entry.objects.get(
            entry_note='test_entry_view_entry',
        )
        # login testuser
        self.client.login(username='testuser_entry', password='GBabI7lbSGB13jXjCRoL')
        # get response
        response = self.client.get('/entry/' + str(entry_1.entry_id) + '/edit/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/generic_form.html')

    def test_entry_edit_get_user_context(self):
        """test edit view"""

        # get object
        entry_1 = Entry.objects.get(
            entry_note='test_entry_view_entry',
        )
        # login testuser
        self.client.login(username='testuser_entry', password='GBabI7lbSGB13jXjCRoL')
        # get response
        response = self.client.get('/entry/' + str(entry_1.entry_id) + '/edit/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_entry')

    def test_entry_edit_redirect(self):
        """test edit view"""

        # get object
        entry_1 = Entry.objects.get(
            entry_note='test_entry_view_entry',
        )
        # login testuser
        self.client.login(username='testuser_entry', password='GBabI7lbSGB13jXjCRoL')
        # create url
        destination = urllib.parse.quote(
            '/entry/' + str(entry_1.entry_id) + '/edit/', safe='/'
        )
        # get response
        response = self.client.get(
            '/entry/' + str(entry_1.entry_id) + '/edit', follow=True
        )
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )

    def test_entry_edit_post_redirect(self):
        """test edit view"""

        # login testuser
        self.client.login(username='testuser_entry', password='GBabI7lbSGB13jXjCRoL')
        # get user
        test_user = User.objects.get(username='testuser_entry')
        # get object
        system_1 = System.objects.get(system_name='system_1')
        # create object
        entry_1 = Entry.objects.create(
            system=system_1,
            entry_time=timezone.now(),
            entry_note='test_entry_view_entry_3',
            entry_created_by_user_id=test_user,
            entry_modified_by_user_id=test_user,
        )
        # create post data
        data_dict = {
            'system': system_1.system_id,
            'entry_time': '2013-12-11 23:45:01',
            'entry_note': 'test_entry_view_entry_3_1',
            'entry_modified_by_user_id': test_user.id,
        }
        # get response
        response = self.client.post(
            '/entry/' + str(entry_1.entry_id) + '/edit/', data_dict
        )
        # create url
        destination = urllib.parse.quote(
            '/system/' + str(system_1.system_id) + '/', safe='/'
        )
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_entry_edit_post_invalid_reload(self):
        """test edit view"""

        # login testuser
        self.client.login(username='testuser_entry', password='GBabI7lbSGB13jXjCRoL')
        # get object
        entry_id = Entry.objects.get(
            entry_note='test_entry_view_entry',
        ).entry_id
        # create post data
        data_dict = {}
        # get response
        response = self.client.post('/entry/' + str(entry_id) + '/edit/', data_dict)
        # compare
        self.assertEqual(response.status_code, 200)

    def test_entry_edit_post_invalid_template(self):
        """test edit view"""

        # login testuser
        self.client.login(username='testuser_entry', password='GBabI7lbSGB13jXjCRoL')
        # get object
        entry_id = Entry.objects.get(
            entry_note='test_entry_view_entry',
        ).entry_id
        # create post data
        data_dict = {}
        # get response
        response = self.client.post('/entry/' + str(entry_id) + '/edit/', data_dict)
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/generic_form.html')

    def test_entry_edit_post_duplicate(self):
        """test edit view"""

        # login testuser
        self.client.login(username='testuser_entry', password='GBabI7lbSGB13jXjCRoL')
        # get time in different formats to avoid runtime warnings
        t2_datetime = timezone.now().replace(microsecond=0)
        t2_string = t2_datetime.strftime('%Y-%m-%d %H:%M:%S')
        # get user
        test_user = User.objects.get(username='testuser_entry')
        # get object
        system_1 = System.objects.get(system_name='system_1')
        # create object (for collision)
        Entry.objects.create(
            system=system_1,
            entry_time=t2_datetime,
            entry_type='duplicate_entry_2',
            entry_content='duplicate_entry_2',
            entry_note='duplicate_entry_2',
            entry_created_by_user_id=test_user,
            entry_modified_by_user_id=test_user,
        )
        # create object (to change)
        entry_id = Entry.objects.create(
            system=system_1,
            entry_time=t2_datetime,
            entry_type='no_duplicate_entry_2',
            entry_content='no_duplicate_entry_2',
            entry_note='no_duplicate_entry_2',
            entry_created_by_user_id=test_user,
            entry_modified_by_user_id=test_user,
        ).entry_id
        # get object
        duplicate_entry = Entry.objects.filter(entry_note='duplicate_entry_2')
        # compare
        self.assertEqual(len(duplicate_entry), 1)
        # create post data
        data_dict = {
            'system': system_1.system_id,
            'entry_time': t2_string,
            'entry_type': 'duplicate_entry_2',
            'entry_content': 'duplicate_entry_2',
            'entry_note': 'duplicate_entry_2',
        }
        # get response
        response = self.client.post('/entry/' + str(entry_id) + '/edit/', data_dict)
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dfirtrack_main/generic_form.html')
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Entry with same content already exists')
        self.assertEqual(messages[0].level_tag, 'warning')
        # get object
        duplicate_entry = Entry.objects.filter(entry_note='duplicate_entry_2')
        # compare
        self.assertEqual(len(duplicate_entry), 1)

    def test_entry_csv_import_step1_not_logged_in(self):
        """test step1 view"""

        # create url
        destination = '/login/?next=' + urllib.parse.quote(
            '/entry/import/step1/', safe=''
        )
        # get response
        response = self.client.get('/entry/import/step1/', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_entry_csv_import_step1_logged_in(self):
        """test step1 view"""

        # login testuser
        self.client.login(username='testuser_entry', password='GBabI7lbSGB13jXjCRoL')
        # get response
        response = self.client.get('/entry/import/step1/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_entry_csv_import_step1_template(self):
        """test step1 view"""

        # login testuser
        self.client.login(username='testuser_entry', password='GBabI7lbSGB13jXjCRoL')
        # get response
        response = self.client.get('/entry/import/step1/')
        # compare
        self.assertTemplateUsed(
            response, 'dfirtrack_main/entry/entry_import_step1.html'
        )

    def test_entry_csv_import_post_step1_redirect(self):
        """test step1 view"""

        # get objects
        system_1 = System.objects.get(system_name='system_1')
        # sample file
        csv_file = SimpleUploadedFile(
            "test.csv", b"datetime,timestamp_desc,message", content_type="text/csv"
        )
        # login testuser
        self.client.login(username='testuser_entry', password='GBabI7lbSGB13jXjCRoL')
        # create post data
        data_dict = {
            'system': system_1.system_id,
            'entryfile': csv_file,
            'delimiter': ',',
            'quotechar': '"',
        }
        destination = '/entry/import/step2/'

        # get response
        response = self.client.post('/entry/import/step1/', data_dict, follow=True)
        # check
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )
        self.assertInHTML('datetime', str(response.content))
        self.assertInHTML('timestamp_desc', str(response.content))
        self.assertInHTML('message', str(response.content))

    def test_entry_csv_import_post_step1_no_case(self):
        """test step1 view"""

        # get objects
        system_1 = System.objects.get(system_name='system_1')
        # sample file
        csv_file = SimpleUploadedFile(
            "test.csv", b"datetime,timestamp_desc,message", content_type="text/csv"
        )
        # login testuser
        self.client.login(username='testuser_entry', password='GBabI7lbSGB13jXjCRoL')
        # create post data
        data_dict = {
            'system': system_1.system_id,
            'entryfile': csv_file,
            'delimiter': ',',
            'quotechar': '"',
        }
        # static uuid
        test_uuid = uuid.uuid4()
        with patch.object(uuid, 'uuid4', return_value=test_uuid):
            # get response
            self.client.post('/entry/import/step1/', data_dict)
            # compare
            self.assertEqual(
                self.client.session['entry_csv_import']['file_name'],
                f'/tmp/{test_uuid}',
            )
            self.assertEqual(
                self.client.session['entry_csv_import']['system'], system_1.system_id
            )
            self.assertEqual(self.client.session['entry_csv_import']['case'], None)
            self.assertEqual(
                self.client.session['entry_csv_import']['fields'],
                ['datetime', 'timestamp_desc', 'message'],
            )
            self.assertEqual(self.client.session['entry_csv_import']['delimiter'], ',')
            self.assertEqual(self.client.session['entry_csv_import']['quotechar'], '"')

    def test_entry_csv_import_post_step1_with_case(self):
        """test step1 view"""

        # get objects
        system_1 = System.objects.get(system_name='system_1')
        test_user = User.objects.get(username='testuser_entry')
        case_1 = Case.objects.create(
            case_name='case_1',
            case_is_incident=True,
            case_created_by_user_id=test_user,
        )
        # sample file
        csv_file = SimpleUploadedFile(
            "test.csv", b"datetime,timestamp_desc,message", content_type="text/csv"
        )
        # login testuser
        self.client.login(username='testuser_entry', password='GBabI7lbSGB13jXjCRoL')
        # create post data
        data_dict = {
            'system': system_1.system_id,
            'case': case_1.case_id,
            'entryfile': csv_file,
            'delimiter': ',',
            'quotechar': '"',
        }
        # get response
        test_uuid = uuid.uuid4()
        with patch.object(uuid, 'uuid4', return_value=test_uuid):
            self.client.post('/entry/import/step1/', data_dict)
            # compare
            self.assertEqual(
                self.client.session['entry_csv_import']['file_name'],
                f'/tmp/{test_uuid}',
            )
            self.assertEqual(
                self.client.session['entry_csv_import']['system'], system_1.system_id
            )
            self.assertEqual(
                self.client.session['entry_csv_import']['case'], case_1.case_id
            )
            self.assertEqual(
                self.client.session['entry_csv_import']['fields'],
                ['datetime', 'timestamp_desc', 'message'],
            )
            self.assertEqual(self.client.session['entry_csv_import']['delimiter'], ',')
            self.assertEqual(self.client.session['entry_csv_import']['quotechar'], '"')

    def test_entry_csv_import_step1_post_invalid_data(self):
        """test step1 view"""

        # login testuser
        self.client.login(username='testuser_entry', password='GBabI7lbSGB13jXjCRoL')
        # create post data
        data_dict = {}
        # get response
        response = self.client.post('/entry/import/step1/', data_dict)
        self.assertTemplateUsed(
            response, 'dfirtrack_main/entry/entry_import_step1.html'
        )
        self.assertContains(response, 'This field is required')

    def test_entry_csv_import_post_step1_invalid_unicode(self):
        """test step1 view"""

        # get objects
        system_1 = System.objects.get(system_name='system_1')
        # sample file
        csv_file = SimpleUploadedFile("test.csv", b"\x89", content_type="text/csv")
        # login testuser
        self.client.login(username='testuser_entry', password='GBabI7lbSGB13jXjCRoL')
        # create post data
        data_dict = {
            'system': system_1.system_id,
            'entryfile': csv_file,
            'delimiter': ',',
            'quotechar': '"',
        }

        # get response
        response = self.client.post('/entry/import/step1/', data_dict)
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertTemplateUsed(
            response, 'dfirtrack_main/entry/entry_import_step1.html'
        )
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Uploaded CSV is not a valid unicode file.')
        self.assertEqual(messages[0].level_tag, 'error')

    def test_entry_csv_import_step2_not_logged_in(self):
        """test step2 view"""

        # create url
        destination = '/login/?next=' + urllib.parse.quote(
            '/entry/import/step2/', safe=''
        )
        # get response
        response = self.client.get('/entry/import/step2/', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_entry_csv_import_step2_logged_in(self):
        """test step2 view"""

        # login testuser
        self.client.login(username='testuser_entry', password='GBabI7lbSGB13jXjCRoL')
        # mock session
        session = self.client.session
        session['entry_csv_import'] = {'fields': ['dummy']}
        session.save()
        # get response
        response = self.client.get('/entry/import/step2/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_entry_csv_import_step2_template(self):
        """test step2 view"""

        # login testuser
        self.client.login(username='testuser_entry', password='GBabI7lbSGB13jXjCRoL')
        # mock session
        session = self.client.session
        session['entry_csv_import'] = {'fields': ['dummy']}
        session.save()
        # get response
        response = self.client.get('/entry/import/step2/')
        # compare
        self.assertTemplateUsed(
            response, 'dfirtrack_main/entry/entry_import_step2.html'
        )

    def test_entry_csv_import_step2_post_invalid_data(self):
        """test step1 view"""

        # login testuser
        self.client.login(username='testuser_entry', password='GBabI7lbSGB13jXjCRoL')
        # mock session
        session = self.client.session
        session['entry_csv_import'] = {'fields': ['dummy']}
        session.save()
        # create post data
        data_dict = {}
        # get response
        response = self.client.post('/entry/import/step2/', data_dict)
        self.assertTemplateUsed(
            response, 'dfirtrack_main/entry/entry_import_step2.html'
        )
        self.assertContains(response, 'This field is required')

    def test_entry_csv_import_get_step1_missing_step1_redirect(self):
        """test step1 view"""

        # login testuser
        self.client.login(username='testuser_entry', password='GBabI7lbSGB13jXjCRoL')

        # destination
        destination = '/entry/import/step1/'
        # get response
        response = self.client.get('/entry/import/step2/')
        # check
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_entry_csv_import_post_step2_success_redirect(self):
        """test step1 view"""

        # get objects
        system_id = System.objects.get(system_name='system_1').system_id
        # login testuser
        self.client.login(username='testuser_entry', password='GBabI7lbSGB13jXjCRoL')
        # prepare session
        session = self.client.session
        session['entry_csv_import'] = {
            'fields': ["datetime", "timestamp_desc", "message"],
            'system': system_id,
            'case': None,
            'file_name': 'test_file_name',
            'delimiter': ',',
            'quotechar': '"',
        }
        session.save()
        # create post data
        data_dict = {
            'entry_time': 0,
            'entry_type': 1,
            'entry_content': 2,
            'entry_tag': -1,
        }
        # destination
        destination = '/entry/'
        # post data
        response = self.client.post('/entry/import/step2/', data_dict, follow=True)

        # check
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )
