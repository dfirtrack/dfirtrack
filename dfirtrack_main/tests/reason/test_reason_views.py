from django.contrib.auth.models import User
from django.test import TestCase
from dfirtrack_main.models import Reason
import urllib.parse

class ReasonViewTestCase(TestCase):
    """ reason view tests """

    @classmethod
    def setUpTestData(cls):

        # create object
        Reason.objects.create(reason_name='reason_1')
        # create user
        test_user = User.objects.create_user(username='testuser_reason', password='h8NrY2f7ei8uzh2CoAuD')

    def test_reason_list_not_logged_in(self):
        """ test list view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/reason/', safe='')
        # get response
        response = self.client.get('/reason/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_reason_list_logged_in(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_reason', password='h8NrY2f7ei8uzh2CoAuD')
        # get response
        response = self.client.get('/reason/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_reason_list_template(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_reason', password='h8NrY2f7ei8uzh2CoAuD')
        # get response
        response = self.client.get('/reason/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/reason/reason_list.html')

    def test_reason_list_get_user_context(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_reason', password='h8NrY2f7ei8uzh2CoAuD')
        # get response
        response = self.client.get('/reason/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_reason')

    def test_reason_list_redirect(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_reason', password='h8NrY2f7ei8uzh2CoAuD')
        # create url
        destination = urllib.parse.quote('/reason/', safe='/')
        # get response
        response = self.client.get('/reason', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_reason_detail_not_logged_in(self):
        """ test detail view """

        # get object
        reason_1 = Reason.objects.get(reason_name='reason_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/reason/' + str(reason_1.reason_id) + '/', safe='')
        # get response
        response = self.client.get('/reason/' + str(reason_1.reason_id) + '/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_reason_detail_logged_in(self):
        """ test detail view """

        # get object
        reason_1 = Reason.objects.get(reason_name='reason_1')
        # login testuser
        login = self.client.login(username='testuser_reason', password='h8NrY2f7ei8uzh2CoAuD')
        # get response
        response = self.client.get('/reason/' + str(reason_1.reason_id) + '/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_reason_detail_template(self):
        """ test detail view """

        # get object
        reason_1 = Reason.objects.get(reason_name='reason_1')
        # login testuser
        login = self.client.login(username='testuser_reason', password='h8NrY2f7ei8uzh2CoAuD')
        # get response
        response = self.client.get('/reason/' + str(reason_1.reason_id) + '/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/reason/reason_detail.html')

    def test_reason_detail_get_user_context(self):
        """ test detail view """

        # get object
        reason_1 = Reason.objects.get(reason_name='reason_1')
        # login testuser
        login = self.client.login(username='testuser_reason', password='h8NrY2f7ei8uzh2CoAuD')
        # get response
        response = self.client.get('/reason/' + str(reason_1.reason_id) + '/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_reason')

    def test_reason_detail_redirect(self):
        """ test detail view """

        # get object
        reason_1 = Reason.objects.get(reason_name='reason_1')
        # login testuser
        login = self.client.login(username='testuser_reason', password='h8NrY2f7ei8uzh2CoAuD')
        # create url
        destination = urllib.parse.quote('/reason/' + str(reason_1.reason_id) + '/', safe='/')
        # get response
        response = self.client.get('/reason/' + str(reason_1.reason_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_reason_add_not_logged_in(self):
        """ test add view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/reason/add/', safe='')
        # get response
        response = self.client.get('/reason/add/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_reason_add_logged_in(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_reason', password='h8NrY2f7ei8uzh2CoAuD')
        # get response
        response = self.client.get('/reason/add/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_reason_add_template(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_reason', password='h8NrY2f7ei8uzh2CoAuD')
        # get response
        response = self.client.get('/reason/add/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/reason/reason_add.html')

    def test_reason_add_get_user_context(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_reason', password='h8NrY2f7ei8uzh2CoAuD')
        # get response
        response = self.client.get('/reason/add/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_reason')

    def test_reason_add_redirect(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_reason', password='h8NrY2f7ei8uzh2CoAuD')
        # create url
        destination = urllib.parse.quote('/reason/add/', safe='/')
        # get response
        response = self.client.get('/reason/add', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_reason_edit_not_logged_in(self):
        """ test edit view """

        # get object
        reason_1 = Reason.objects.get(reason_name='reason_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/reason/' + str(reason_1.reason_id) + '/edit/', safe='')
        # get response
        response = self.client.get('/reason/' + str(reason_1.reason_id) + '/edit/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_reason_edit_logged_in(self):
        """ test edit view """

        # get object
        reason_1 = Reason.objects.get(reason_name='reason_1')
        # login testuser
        login = self.client.login(username='testuser_reason', password='h8NrY2f7ei8uzh2CoAuD')
        # get response
        response = self.client.get('/reason/' + str(reason_1.reason_id) + '/edit/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_reason_edit_template(self):
        """ test edit view """

        # get object
        reason_1 = Reason.objects.get(reason_name='reason_1')
        # login testuser
        login = self.client.login(username='testuser_reason', password='h8NrY2f7ei8uzh2CoAuD')
        # get response
        response = self.client.get('/reason/' + str(reason_1.reason_id) + '/edit/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/reason/reason_edit.html')

    def test_reason_edit_get_user_context(self):
        """ test edit view """

        # get object
        reason_1 = Reason.objects.get(reason_name='reason_1')
        # login testuser
        login = self.client.login(username='testuser_reason', password='h8NrY2f7ei8uzh2CoAuD')
        # get response
        response = self.client.get('/reason/' + str(reason_1.reason_id) + '/edit/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_reason')

    def test_reason_edit_redirect(self):
        """ test edit view """

        # get object
        reason_1 = Reason.objects.get(reason_name='reason_1')
        # login testuser
        login = self.client.login(username='testuser_reason', password='h8NrY2f7ei8uzh2CoAuD')
        # create url
        destination = urllib.parse.quote('/reason/' + str(reason_1.reason_id) + '/edit/', safe='/')
        # get response
        response = self.client.get('/reason/' + str(reason_1.reason_id) + '/edit', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)
