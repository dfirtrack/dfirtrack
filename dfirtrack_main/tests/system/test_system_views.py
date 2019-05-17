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

    def test_systems_list_not_logged_in(self):

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/systems/', safe='')
        # get response
        response = self.client.get('/systems/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_systems_list_logged_in(self):

        # login testuser
        login = self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get('/systems/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_systems_list_template(self):

        # login testuser
        login = self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get('/systems/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/system/systems_list.html')

    def test_systems_list_get_user_context(self):

        # login testuser
        login = self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get('/systems/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_system')

    def test_systems_detail_not_logged_in(self):

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/systems/' + str(system_1.system_id), safe='')
        # get response
        response = self.client.get('/systems/' + str(system_1.system_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_systems_detail_logged_in(self):

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # login testuser
        login = self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get('/systems/' + str(system_1.system_id))
        # compare
        self.assertEqual(response.status_code, 200)

    def test_systems_detail_template(self):

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # login testuser
        login = self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get('/systems/' + str(system_1.system_id))
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/system/systems_detail.html')

    def test_systems_detail_get_user_context(self):

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # login testuser
        login = self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get('/systems/' + str(system_1.system_id))
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_system')

    def test_systems_add_not_logged_in(self):

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/systems/add/', safe='')
        # get response
        response = self.client.get('/systems/add/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_systems_add_logged_in(self):

        # login testuser
        login = self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get('/systems/add/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_systems_add_template(self):

        # login testuser
        login = self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get('/systems/add/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/system/systems_add.html')

    def test_systems_add_get_user_context(self):

        # login testuser
        login = self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get('/systems/add/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_system')

    def test_systems_edit_not_logged_in(self):

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/systems/' + str(system_1.system_id) + '/edit/', safe='')
        # get response
        response = self.client.get('/systems/' + str(system_1.system_id) + '/edit/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_systems_edit_logged_in(self):

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # login testuser
        login = self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get('/systems/' + str(system_1.system_id) + '/edit/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_systems_edit_template(self):

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # login testuser
        login = self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get('/systems/' + str(system_1.system_id) + '/edit/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/system/systems_edit.html')

    def test_systems_edit_get_user_context(self):

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # login testuser
        login = self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
        # get response
        response = self.client.get('/systems/' + str(system_1.system_id) + '/edit/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_system')

#    def test_systems_detail_logged_in_not_existing(self):
#
#        # login testuser
#        login = self.client.login(username='testuser_system', password='LqShcoecDud6JLRxhfKV')
#        # get response
#        response = self.client.get('/systems/x')
#        # compare
#        self.assertEqual(response.status_code, 404)
