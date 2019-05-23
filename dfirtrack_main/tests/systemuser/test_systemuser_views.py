from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone
from dfirtrack_main.models import System, Systemstatus, Systemuser
import urllib.parse

class SystemuserViewTestCase(TestCase):
    """ systemuser view tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_systemuser', password='BXgnvXckpl1BS3I5ShJs')

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
        Systemuser.objects.create(systemuser_name='systemuser_1', system = system_1)

    def test_systemusers_list_not_logged_in(self):
        """ test list view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/systemusers/', safe='')
        # get response
        response = self.client.get('/systemusers/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_systemusers_list_logged_in(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_systemuser', password='BXgnvXckpl1BS3I5ShJs')
        # get response
        response = self.client.get('/systemusers/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_systemusers_list_template(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_systemuser', password='BXgnvXckpl1BS3I5ShJs')
        # get response
        response = self.client.get('/systemusers/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/systemuser/systemusers_list.html')

    def test_systemusers_list_get_user_context(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_systemuser', password='BXgnvXckpl1BS3I5ShJs')
        # get response
        response = self.client.get('/systemusers/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_systemuser')

    def test_systemusers_detail_not_logged_in(self):
        """ test detail view """

        # get object
        systemuser_1 = Systemuser.objects.get(systemuser_name='systemuser_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/systemusers/' + str(systemuser_1.systemuser_id), safe='')
        # get response
        response = self.client.get('/systemusers/' + str(systemuser_1.systemuser_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_systemusers_detail_logged_in(self):
        """ test detail view """

        # get object
        systemuser_1 = Systemuser.objects.get(systemuser_name='systemuser_1')
        # login testuser
        login = self.client.login(username='testuser_systemuser', password='BXgnvXckpl1BS3I5ShJs')
        # get response
        response = self.client.get('/systemusers/' + str(systemuser_1.systemuser_id))
        # compare
        self.assertEqual(response.status_code, 200)

    def test_systemusers_detail_template(self):
        """ test detail view """

        # get object
        systemuser_1 = Systemuser.objects.get(systemuser_name='systemuser_1')
        # login testuser
        login = self.client.login(username='testuser_systemuser', password='BXgnvXckpl1BS3I5ShJs')
        # get response
        response = self.client.get('/systemusers/' + str(systemuser_1.systemuser_id))
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/systemuser/systemusers_detail.html')

    def test_systemusers_detail_get_user_context(self):
        """ test detail view """

        # get object
        systemuser_1 = Systemuser.objects.get(systemuser_name='systemuser_1')
        # login testuser
        login = self.client.login(username='testuser_systemuser', password='BXgnvXckpl1BS3I5ShJs')
        # get response
        response = self.client.get('/systemusers/' + str(systemuser_1.systemuser_id))
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_systemuser')

    def test_systemusers_add_not_logged_in(self):
        """ test add view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/systemusers/add/', safe='')
        # get response
        response = self.client.get('/systemusers/add/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_systemusers_add_logged_in(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_systemuser', password='BXgnvXckpl1BS3I5ShJs')
        # get response
        response = self.client.get('/systemusers/add/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_systemusers_add_template(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_systemuser', password='BXgnvXckpl1BS3I5ShJs')
        # get response
        response = self.client.get('/systemusers/add/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/systemuser/systemusers_add.html')

    def test_systemusers_add_get_user_context(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_systemuser', password='BXgnvXckpl1BS3I5ShJs')
        # get response
        response = self.client.get('/systemusers/add/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_systemuser')

    def test_systemusers_edit_not_logged_in(self):
        """ test edit view """

        # get object
        systemuser_1 = Systemuser.objects.get(systemuser_name='systemuser_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/systemusers/' + str(systemuser_1.systemuser_id) + '/edit/', safe='')
        # get response
        response = self.client.get('/systemusers/' + str(systemuser_1.systemuser_id) + '/edit/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_systemusers_edit_logged_in(self):
        """ test edit view """

        # get object
        systemuser_1 = Systemuser.objects.get(systemuser_name='systemuser_1')
        # login testuser
        login = self.client.login(username='testuser_systemuser', password='BXgnvXckpl1BS3I5ShJs')
        # get response
        response = self.client.get('/systemusers/' + str(systemuser_1.systemuser_id) + '/edit/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_systemusers_edit_template(self):
        """ test edit view """

        # get object
        systemuser_1 = Systemuser.objects.get(systemuser_name='systemuser_1')
        # login testuser
        login = self.client.login(username='testuser_systemuser', password='BXgnvXckpl1BS3I5ShJs')
        # get response
        response = self.client.get('/systemusers/' + str(systemuser_1.systemuser_id) + '/edit/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/systemuser/systemusers_edit.html')

    def test_systemusers_edit_get_user_context(self):
        """ test edit view """

        # get object
        systemuser_1 = Systemuser.objects.get(systemuser_name='systemuser_1')
        # login testuser
        login = self.client.login(username='testuser_systemuser', password='BXgnvXckpl1BS3I5ShJs')
        # get response
        response = self.client.get('/systemusers/' + str(systemuser_1.systemuser_id) + '/edit/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_systemuser')
