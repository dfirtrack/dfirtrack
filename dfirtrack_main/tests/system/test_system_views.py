from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone
from dfirtrack_main.models import System, Systemstatus
import urllib.parse

class SystemViewTestCase(TestCase):
    """ system view tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_system', password='LqShcoecDud6JLRxhfKV')

        # create object
        systemstatus_1 = Systemstatus.objects.create(systemstatus_name='systemstatus_1')

        # create object
        System.objects.create(
            system_name = 'system_1',
            systemstatus = systemstatus_1,
            system_modify_time = timezone.now(),
            system_created_by_user_id = test_user,
            system_modified_by_user_id = test_user,
        )

    def test_system_list_not_logged_in(self):
        """ test list view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/system/', safe='')
        # get response
        response = self.client.get('/system/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_list_logged_in(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get('/system/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_system_list_template(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get('/system/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/system/system_list.html')

    def test_system_list_get_user_context(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get('/system/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_system')

    def test_system_list_redirect(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # get response
        response = self.client.get('/system', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_system_list_context_with_api(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get('/system/')
        # compare
        self.assertEqual(str(response.context['dfirtrack_api']), 'True')

    def test_system_list_context_without_api(self):
        """ test list view """

        # remove app from dfirtrack.settings
        installed_apps.remove('dfirtrack_api')
        # login testuser
        login = self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get('/system/')
        # compare
        self.assertEqual(str(response.context['dfirtrack_api']), 'False')

    def test_system_detail_not_logged_in(self):
        """ test detail view """

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/system/' + str(system_1.system_id) + '/', safe='')
        # get response
        response = self.client.get('/system/' + str(system_1.system_id) + '/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_detail_logged_in(self):
        """ test detail view """

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # login testuser
        login = self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get('/system/' + str(system_1.system_id) + '/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_system_detail_template(self):
        """ test detail view """

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # login testuser
        login = self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get('/system/' + str(system_1.system_id) + '/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/system/system_detail.html')

    def test_system_detail_get_user_context(self):
        """ test detail view """

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # login testuser
        login = self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get('/system/' + str(system_1.system_id) + '/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_system')

    def test_system_detail_redirect(self):
        """ test detail view """

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # login testuser
        login = self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # create url
        destination = urllib.parse.quote('/system/' + str(system_1.system_id) + '/', safe='/')
        # get response
        response = self.client.get('/system/' + str(system_1.system_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_system_add_not_logged_in(self):
        """ test add view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/system/add/', safe='')
        # get response
        response = self.client.get('/system/add/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_add_logged_in(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get('/system/add/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_system_add_template(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get('/system/add/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/system/system_add.html')

    def test_system_add_get_user_context(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get('/system/add/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_system')

    def test_system_add_redirect(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # create url
        destination = urllib.parse.quote('/system/add/', safe='/')
        # get response
        response = self.client.get('/system/add', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_system_edit_not_logged_in(self):
        """ test edit view """

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/system/' + str(system_1.system_id) + '/edit/', safe='')
        # get response
        response = self.client.get('/system/' + str(system_1.system_id) + '/edit/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_edit_logged_in(self):
        """ test edit view """

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # login testuser
        login = self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get('/system/' + str(system_1.system_id) + '/edit/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_system_edit_template(self):
        """ test edit view """

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # login testuser
        login = self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get('/system/' + str(system_1.system_id) + '/edit/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/system/system_edit.html')

    def test_system_edit_get_user_context(self):
        """ test edit view """

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # login testuser
        login = self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get('/system/' + str(system_1.system_id) + '/edit/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_system')

    def test_system_edit_redirect(self):
        """ test edit view """

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # login testuser
        login = self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # create url
        destination = urllib.parse.quote('/system/' + str(system_1.system_id) + '/edit/', safe='/')
        # get response
        response = self.client.get('/system/' + str(system_1.system_id) + '/edit', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)
