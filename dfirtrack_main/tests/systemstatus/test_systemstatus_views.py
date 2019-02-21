from django.contrib.auth.models import User
from django.test import TestCase
from dfirtrack_main.models import Systemstatus
from dfirtrack_main.views import systemstatuss_views
import urllib.parse

class SystemstatusViewTestCase(TestCase):
    """ systemstatus view tests """

    @classmethod
    def setUpTestData(cls):

        # create object
        Systemstatus.objects.create(systemstatus_name='systemstatus_1', systemstatus_note='lorem ipsum')
        # create user
        test_user = User.objects.create_user(username='testuser_systemstatus', password='kWAvcuNoU97qpEy7UpDT')
        test_user.save()

    def test_systemstatuss_list_not_logged_in(self):

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/systemstatuss/', safe='')
        # get response
        response = self.client.get('/systemstatuss/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_systemstatuss_list_logged_in(self):

        # login testuser
        login = self.client.login(username='testuser_systemstatus', password='kWAvcuNoU97qpEy7UpDT')
        # get response
        response = self.client.get('/systemstatuss/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_systemstatuss_list_template(self):

        # login testuser
        login = self.client.login(username='testuser_systemstatus', password='kWAvcuNoU97qpEy7UpDT')
        # get response
        response = self.client.get('/systemstatuss/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/systemstatus/systemstatuss_list.html')

    def test_systemstatuss_list_get_user_context(self):

        # login testuser
        login = self.client.login(username='testuser_systemstatus', password='kWAvcuNoU97qpEy7UpDT')
        # get response
        response = self.client.get('/systemstatuss/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_systemstatus')

    def test_systemstatuss_detail_not_logged_in(self):

        # get object
        systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/systemstatuss/' + str(systemstatus_1.systemstatus_id), safe='')
        # get response
        response = self.client.get('/systemstatuss/' + str(systemstatus_1.systemstatus_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_systemstatuss_detail_logged_in(self):

        # get object
        systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')
        # login testuser
        login = self.client.login(username='testuser_systemstatus', password='kWAvcuNoU97qpEy7UpDT')
        # get response
        response = self.client.get('/systemstatuss/' + str(systemstatus_1.systemstatus_id))
        # compare
        self.assertEqual(response.status_code, 200)

    def test_systemstatuss_detail_template(self):

        # get object
        systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')
        # login testuser
        login = self.client.login(username='testuser_systemstatus', password='kWAvcuNoU97qpEy7UpDT')
        # get response
        response = self.client.get('/systemstatuss/' + str(systemstatus_1.systemstatus_id))
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/systemstatus/systemstatuss_detail.html')

    def test_systemstatuss_detail_get_user_context(self):

        # get object
        systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')
        # login testuser
        login = self.client.login(username='testuser_systemstatus', password='kWAvcuNoU97qpEy7UpDT')
        # get response
        response = self.client.get('/systemstatuss/' + str(systemstatus_1.systemstatus_id))
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_systemstatus')

#    def test_systemstatuss_detail_logged_in_not_existing(self):
#
#        # login testuser
#        login = self.client.login(username='testuser_systemstatus', password='kWAvcuNoU97qpEy7UpDT')
#        # get response
#        response = self.client.get('/systemstatuss/x')
#        # compare
#        self.assertEqual(response.status_code, 404)
