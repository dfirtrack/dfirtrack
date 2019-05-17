from django.contrib.auth.models import User
from django.test import TestCase
from dfirtrack_main.models import Os
import urllib.parse

class OsViewTestCase(TestCase):
    """ os view tests """

    @classmethod
    def setUpTestData(cls):

        # create object
        Os.objects.create(os_name='os_1')
        # create user
        test_user = User.objects.create_user(username='testuser_os', password='n7hIWBsrGsG0n4mSjbfw')

    def test_oss_list_not_logged_in(self):

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/oss/', safe='')
        # get response
        response = self.client.get('/oss/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_oss_list_logged_in(self):

        # login testuser
        login = self.client.login(username='testuser_os', password='n7hIWBsrGsG0n4mSjbfw')
        # get response
        response = self.client.get('/oss/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_oss_list_template(self):

        # login testuser
        login = self.client.login(username='testuser_os', password='n7hIWBsrGsG0n4mSjbfw')
        # get response
        response = self.client.get('/oss/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/os/oss_list.html')

    def test_oss_list_get_user_context(self):

        # login testuser
        login = self.client.login(username='testuser_os', password='n7hIWBsrGsG0n4mSjbfw')
        # get response
        response = self.client.get('/oss/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_os')

    def test_oss_detail_not_logged_in(self):

        # get object
        os_1 = Os.objects.get(os_name='os_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/oss/' + str(os_1.os_id), safe='')
        # get response
        response = self.client.get('/oss/' + str(os_1.os_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_oss_detail_logged_in(self):

        # get object
        os_1 = Os.objects.get(os_name='os_1')
        # login testuser
        login = self.client.login(username='testuser_os', password='n7hIWBsrGsG0n4mSjbfw')
        # get response
        response = self.client.get('/oss/' + str(os_1.os_id))
        # compare
        self.assertEqual(response.status_code, 200)

    def test_oss_detail_template(self):

        # get object
        os_1 = Os.objects.get(os_name='os_1')
        # login testuser
        login = self.client.login(username='testuser_os', password='n7hIWBsrGsG0n4mSjbfw')
        # get response
        response = self.client.get('/oss/' + str(os_1.os_id))
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/os/oss_detail.html')

    def test_oss_detail_get_user_context(self):

        # get object
        os_1 = Os.objects.get(os_name='os_1')
        # login testuser
        login = self.client.login(username='testuser_os', password='n7hIWBsrGsG0n4mSjbfw')
        # get response
        response = self.client.get('/oss/' + str(os_1.os_id))
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_os')

    def test_oss_add_not_logged_in(self):

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/oss/add/', safe='')
        # get response
        response = self.client.get('/oss/add/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_oss_add_logged_in(self):

        # login testuser
        login = self.client.login(username='testuser_os', password='n7hIWBsrGsG0n4mSjbfw')
        # get response
        response = self.client.get('/oss/add/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_oss_add_template(self):

        # login testuser
        login = self.client.login(username='testuser_os', password='n7hIWBsrGsG0n4mSjbfw')
        # get response
        response = self.client.get('/oss/add/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/os/oss_add.html')

    def test_oss_add_get_user_context(self):

        # login testuser
        login = self.client.login(username='testuser_os', password='n7hIWBsrGsG0n4mSjbfw')
        # get response
        response = self.client.get('/oss/add/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_os')

    def test_oss_edit_not_logged_in(self):

        # get object
        os_1 = Os.objects.get(os_name='os_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/oss/' + str(os_1.os_id) + '/edit/', safe='')
        # get response
        response = self.client.get('/oss/' + str(os_1.os_id) + '/edit/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_oss_edit_logged_in(self):

        # get object
        os_1 = Os.objects.get(os_name='os_1')
        # login testuser
        login = self.client.login(username='testuser_os', password='n7hIWBsrGsG0n4mSjbfw')
        # get response
        response = self.client.get('/oss/' + str(os_1.os_id) + '/edit/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_oss_edit_template(self):

        # get object
        os_1 = Os.objects.get(os_name='os_1')
        # login testuser
        login = self.client.login(username='testuser_os', password='n7hIWBsrGsG0n4mSjbfw')
        # get response
        response = self.client.get('/oss/' + str(os_1.os_id) + '/edit/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/os/oss_edit.html')

    def test_oss_edit_get_user_context(self):

        # get object
        os_1 = Os.objects.get(os_name='os_1')
        # login testuser
        login = self.client.login(username='testuser_os', password='n7hIWBsrGsG0n4mSjbfw')
        # get response
        response = self.client.get('/oss/' + str(os_1.os_id) + '/edit/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_os')
