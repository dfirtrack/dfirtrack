from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone
from dfirtrack_main.models import Entry, System, Systemstatus
import urllib.parse

class EntryViewTestCase(TestCase):
    """ entry view tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_entry', password='GBabI7lbSGB13jXjCRoL')

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

        # create object
        Entry.objects.create(
            system = system_1,
            entry_time = timezone.now(),
            entry_sha1 = 'da39a3ee5e6b4b0d3255bfef95601890afd80709',
            entry_created_by_user_id = test_user,
            entry_modified_by_user_id = test_user,
        )

    def test_entrys_list_not_logged_in(self):

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/entrys/', safe='')
        # get response
        response = self.client.get('/entrys/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_entrys_list_logged_in(self):

        # login testuser
        login = self.client.login(username='testuser_entry', password='GBabI7lbSGB13jXjCRoL')
        # get response
        response = self.client.get('/entrys/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_entrys_list_template(self):

        # login testuser
        login = self.client.login(username='testuser_entry', password='GBabI7lbSGB13jXjCRoL')
        # get response
        response = self.client.get('/entrys/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/entry/entrys_list.html')

    def test_entrys_list_get_user_context(self):

        # login testuser
        login = self.client.login(username='testuser_entry', password='GBabI7lbSGB13jXjCRoL')
        # get response
        response = self.client.get('/entrys/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_entry')

    def test_entrys_detail_not_logged_in(self):

        # get object
        entry_1 = Entry.objects.get(entry_sha1='da39a3ee5e6b4b0d3255bfef95601890afd80709')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/entrys/' + str(entry_1.entry_id), safe='')
        # get response
        response = self.client.get('/entrys/' + str(entry_1.entry_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_entrys_detail_logged_in(self):

        # get object
        entry_1 = Entry.objects.get(entry_sha1='da39a3ee5e6b4b0d3255bfef95601890afd80709')
        # login testuser
        login = self.client.login(username='testuser_entry', password='GBabI7lbSGB13jXjCRoL')
        # get response
        response = self.client.get('/entrys/' + str(entry_1.entry_id))
        # compare
        self.assertEqual(response.status_code, 200)

    def test_entrys_detail_template(self):

        # get object
        entry_1 = Entry.objects.get(entry_sha1='da39a3ee5e6b4b0d3255bfef95601890afd80709')
        # login testuser
        login = self.client.login(username='testuser_entry', password='GBabI7lbSGB13jXjCRoL')
        # get response
        response = self.client.get('/entrys/' + str(entry_1.entry_id))
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/entry/entrys_detail.html')

    def test_entrys_detail_get_user_context(self):

        # get object
        entry_1 = Entry.objects.get(entry_sha1='da39a3ee5e6b4b0d3255bfef95601890afd80709')
        # login testuser
        login = self.client.login(username='testuser_entry', password='GBabI7lbSGB13jXjCRoL')
        # get response
        response = self.client.get('/entrys/' + str(entry_1.entry_id))
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_entry')

    def test_entrys_add_not_logged_in(self):

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/entrys/add/', safe='')
        # get response
        response = self.client.get('/entrys/add/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_entrys_add_logged_in(self):

        # login testuser
        login = self.client.login(username='testuser_entry', password='GBabI7lbSGB13jXjCRoL')
        # get response
        response = self.client.get('/entrys/add/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_entrys_add_template(self):

        # login testuser
        login = self.client.login(username='testuser_entry', password='GBabI7lbSGB13jXjCRoL')
        # get response
        response = self.client.get('/entrys/add/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/entry/entrys_add.html')

    def test_entrys_add_get_user_context(self):

        # login testuser
        login = self.client.login(username='testuser_entry', password='GBabI7lbSGB13jXjCRoL')
        # get response
        response = self.client.get('/entrys/add/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_entry')

    def test_entrys_edit_not_logged_in(self):

        # get object
        entry_1 = Entry.objects.get(entry_sha1='da39a3ee5e6b4b0d3255bfef95601890afd80709')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/entrys/' + str(entry_1.entry_id) + '/edit/', safe='')
        # get response
        response = self.client.get('/entrys/' + str(entry_1.entry_id) + '/edit/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_entrys_edit_logged_in(self):

        # get object
        entry_1 = Entry.objects.get(entry_sha1='da39a3ee5e6b4b0d3255bfef95601890afd80709')
        # login testuser
        login = self.client.login(username='testuser_entry', password='GBabI7lbSGB13jXjCRoL')
        # get response
        response = self.client.get('/entrys/' + str(entry_1.entry_id) + '/edit/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_entrys_edit_template(self):

        # get object
        entry_1 = Entry.objects.get(entry_sha1='da39a3ee5e6b4b0d3255bfef95601890afd80709')
        # login testuser
        login = self.client.login(username='testuser_entry', password='GBabI7lbSGB13jXjCRoL')
        # get response
        response = self.client.get('/entrys/' + str(entry_1.entry_id) + '/edit/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/entry/entrys_edit.html')

    def test_entrys_edit_get_user_context(self):

        # get object
        entry_1 = Entry.objects.get(entry_sha1='da39a3ee5e6b4b0d3255bfef95601890afd80709')
        # login testuser
        login = self.client.login(username='testuser_entry', password='GBabI7lbSGB13jXjCRoL')
        # get response
        response = self.client.get('/entrys/' + str(entry_1.entry_id) + '/edit/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_entry')
