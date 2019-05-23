from django.contrib.auth.models import User
from django.test import TestCase
from dfirtrack_main.models import Ip
import urllib.parse

class IpViewTestCase(TestCase):
    """ ip view tests """

    @classmethod
    def setUpTestData(cls):

        # create object
        Ip.objects.create(ip_ip='127.0.0.1')
        # create user
        test_user = User.objects.create_user(username='testuser_ip', password='pRs9Ap7oc9W0yjLfnP2Y')

    def test_ips_list_not_logged_in(self):
        """ test list view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/ips/', safe='')
        # get response
        response = self.client.get('/ips/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_ips_list_logged_in(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_ip', password='pRs9Ap7oc9W0yjLfnP2Y')
        # get response
        response = self.client.get('/ips/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_ips_list_template(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_ip', password='pRs9Ap7oc9W0yjLfnP2Y')
        # get response
        response = self.client.get('/ips/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/ip/ips_list.html')

    def test_ips_list_get_user_context(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_ip', password='pRs9Ap7oc9W0yjLfnP2Y')
        # get response
        response = self.client.get('/ips/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_ip')

    def test_ips_detail_not_logged_in(self):
        """ test detail view """

        # get object
        ip_1 = Ip.objects.get(ip_ip='127.0.0.1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/ips/' + str(ip_1.ip_id), safe='')
        # get response
        response = self.client.get('/ips/' + str(ip_1.ip_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_ips_detail_logged_in(self):
        """ test detail view """

        # get object
        ip_1 = Ip.objects.get(ip_ip='127.0.0.1')
        # login testuser
        login = self.client.login(username='testuser_ip', password='pRs9Ap7oc9W0yjLfnP2Y')
        # get response
        response = self.client.get('/ips/' + str(ip_1.ip_id))
        # compare
        self.assertEqual(response.status_code, 200)

    def test_ips_detail_template(self):
        """ test detail view """

        # get object
        ip_1 = Ip.objects.get(ip_ip='127.0.0.1')
        # login testuser
        login = self.client.login(username='testuser_ip', password='pRs9Ap7oc9W0yjLfnP2Y')
        # get response
        response = self.client.get('/ips/' + str(ip_1.ip_id))
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/ip/ips_detail.html')

    def test_ips_detail_get_user_context(self):
        """ test detail view """

        # get object
        ip_1 = Ip.objects.get(ip_ip='127.0.0.1')
        # login testuser
        login = self.client.login(username='testuser_ip', password='pRs9Ap7oc9W0yjLfnP2Y')
        # get response
        response = self.client.get('/ips/' + str(ip_1.ip_id))
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_ip')

    def test_ips_add_not_logged_in(self):
        """ test add view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/ips/add/', safe='')
        # get response
        response = self.client.get('/ips/add/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_ips_add_logged_in(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_ip', password='pRs9Ap7oc9W0yjLfnP2Y')
        # get response
        response = self.client.get('/ips/add/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_ips_add_template(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_ip', password='pRs9Ap7oc9W0yjLfnP2Y')
        # get response
        response = self.client.get('/ips/add/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/ip/ips_add.html')

    def test_ips_add_get_user_context(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_ip', password='pRs9Ap7oc9W0yjLfnP2Y')
        # get response
        response = self.client.get('/ips/add/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_ip')

    def test_ips_edit_not_logged_in(self):
        """ test edit view """

        # get object
        ip_1 = Ip.objects.get(ip_ip='127.0.0.1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/ips/' + str(ip_1.ip_id) + '/edit/', safe='')
        # get response
        response = self.client.get('/ips/' + str(ip_1.ip_id) + '/edit/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_ips_edit_logged_in(self):
        """ test edit view """

        # get object
        ip_1 = Ip.objects.get(ip_ip='127.0.0.1')
        # login testuser
        login = self.client.login(username='testuser_ip', password='pRs9Ap7oc9W0yjLfnP2Y')
        # get response
        response = self.client.get('/ips/' + str(ip_1.ip_id) + '/edit/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_ips_edit_template(self):
        """ test edit view """

        # get object
        ip_1 = Ip.objects.get(ip_ip='127.0.0.1')
        # login testuser
        login = self.client.login(username='testuser_ip', password='pRs9Ap7oc9W0yjLfnP2Y')
        # get response
        response = self.client.get('/ips/' + str(ip_1.ip_id) + '/edit/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/ip/ips_edit.html')

    def test_ips_edit_get_user_context(self):
        """ test edit view """

        # get object
        ip_1 = Ip.objects.get(ip_ip='127.0.0.1')
        # login testuser
        login = self.client.login(username='testuser_ip', password='pRs9Ap7oc9W0yjLfnP2Y')
        # get response
        response = self.client.get('/ips/' + str(ip_1.ip_id) + '/edit/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_ip')
