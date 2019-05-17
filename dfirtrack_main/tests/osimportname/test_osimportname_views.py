from django.contrib.auth.models import User
from django.test import TestCase
from dfirtrack_main.models import Os, Osimportname
import urllib.parse

class OsimportnameViewTestCase(TestCase):
    """ osimportname view tests """

    @classmethod
    def setUpTestData(cls):

        # create object
        os_1 = Os.objects.create(os_name='os_1')
        # create object
        Osimportname.objects.create(osimportname_name='osimportname_1', osimportname_importer='osimportname_importer_1', os = os_1)
        # create user
        test_user = User.objects.create_user(username='testuser_osimportname', password='SU7QGdCzPMBJd3l9URoS')

    def test_osimportnames_list_not_logged_in(self):

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/osimportnames/', safe='')
        # get response
        response = self.client.get('/osimportnames/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_osimportnames_list_logged_in(self):

        # login testuser
        login = self.client.login(username='testuser_osimportname', password='SU7QGdCzPMBJd3l9URoS')
        # get response
        response = self.client.get('/osimportnames/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_osimportnames_list_template(self):

        # login testuser
        login = self.client.login(username='testuser_osimportname', password='SU7QGdCzPMBJd3l9URoS')
        # get response
        response = self.client.get('/osimportnames/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/osimportname/osimportnames_list.html')

    def test_osimportnames_list_get_user_context(self):

        # login testuser
        login = self.client.login(username='testuser_osimportname', password='SU7QGdCzPMBJd3l9URoS')
        # get response
        response = self.client.get('/osimportnames/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_osimportname')

    def test_osimportnames_add_not_logged_in(self):

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/osimportnames/add/', safe='')
        # get response
        response = self.client.get('/osimportnames/add/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_osimportnames_add_logged_in(self):

        # login testuser
        login = self.client.login(username='testuser_osimportname', password='SU7QGdCzPMBJd3l9URoS')
        # get response
        response = self.client.get('/osimportnames/add/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_osimportnames_add_template(self):

        # login testuser
        login = self.client.login(username='testuser_osimportname', password='SU7QGdCzPMBJd3l9URoS')
        # get response
        response = self.client.get('/osimportnames/add/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/osimportname/osimportnames_add.html')

    def test_osimportnames_add_get_user_context(self):

        # login testuser
        login = self.client.login(username='testuser_osimportname', password='SU7QGdCzPMBJd3l9URoS')
        # get response
        response = self.client.get('/osimportnames/add/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_osimportname')

    def test_osimportnames_edit_not_logged_in(self):

        # get object
        osimportname_1 = Osimportname.objects.get(osimportname_name='osimportname_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/osimportnames/' + str(osimportname_1.osimportname_id) + '/edit/', safe='')
        # get response
        response = self.client.get('/osimportnames/' + str(osimportname_1.osimportname_id) + '/edit/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_osimportnames_edit_logged_in(self):

        # get object
        osimportname_1 = Osimportname.objects.get(osimportname_name='osimportname_1')
        # login testuser
        login = self.client.login(username='testuser_osimportname', password='SU7QGdCzPMBJd3l9URoS')
        # get response
        response = self.client.get('/osimportnames/' + str(osimportname_1.osimportname_id) + '/edit/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_osimportnames_edit_template(self):

        # get object
        osimportname_1 = Osimportname.objects.get(osimportname_name='osimportname_1')
        # login testuser
        login = self.client.login(username='testuser_osimportname', password='SU7QGdCzPMBJd3l9URoS')
        # get response
        response = self.client.get('/osimportnames/' + str(osimportname_1.osimportname_id) + '/edit/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/osimportname/osimportnames_edit.html')

    def test_osimportnames_edit_get_user_context(self):

        # get object
        osimportname_1 = Osimportname.objects.get(osimportname_name='osimportname_1')
        # login testuser
        login = self.client.login(username='testuser_osimportname', password='SU7QGdCzPMBJd3l9URoS')
        # get response
        response = self.client.get('/osimportnames/' + str(osimportname_1.osimportname_id) + '/edit/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_osimportname')

#    def test_osimportnames_detail_logged_in_not_existing(self):
#
#        # login testuser
#        login = self.client.login(username='testuser_osimportname', password='SU7QGdCzPMBJd3l9URoS')
#        # get response
#        response = self.client.get('/osimportnames/x')
#        # compare
#        self.assertEqual(response.status_code, 404)
