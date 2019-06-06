from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone
from dfirtrack_main.models import Analystmemo, System, Systemstatus
import urllib.parse

class AnalystmemoViewTestCase(TestCase):
    """ analystmemo view tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_analystmemo', password='M4d878CFQiHcJQrZr4iN')

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
        Analystmemo.objects.create(
            analystmemo_note='lorem ipsum',
            system = system_1,
            analystmemo_created_by_user_id = test_user,
            analystmemo_modified_by_user_id = test_user,
        )

    def test_analystmemos_list_not_logged_in(self):
        """ test list view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/analystmemos/', safe='')
        # get response
        response = self.client.get('/analystmemos/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_analystmemos_list_logged_in(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_analystmemo', password='M4d878CFQiHcJQrZr4iN')
        # get response
        response = self.client.get('/analystmemos/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_analystmemos_list_template(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_analystmemo', password='M4d878CFQiHcJQrZr4iN')
        # get response
        response = self.client.get('/analystmemos/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/analystmemo/analystmemos_list.html')

    def test_analystmemos_list_get_user_context(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_analystmemo', password='M4d878CFQiHcJQrZr4iN')
        # get response
        response = self.client.get('/analystmemos/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_analystmemo')

    def test_analystmemos_detail_not_logged_in(self):
        """ test detail view """

        # get object
        analystmemo_1 = Analystmemo.objects.get(analystmemo_note='lorem ipsum')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/analystmemos/' + str(analystmemo_1.analystmemo_id), safe='')
        # get response
        response = self.client.get('/analystmemos/' + str(analystmemo_1.analystmemo_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_analystmemos_detail_logged_in(self):
        """ test detail view """

        # get object
        analystmemo_1 = Analystmemo.objects.get(analystmemo_note='lorem ipsum')
        # login testuser
        login = self.client.login(username='testuser_analystmemo', password='M4d878CFQiHcJQrZr4iN')
        # get response
        response = self.client.get('/analystmemos/' + str(analystmemo_1.analystmemo_id))
        # compare
        self.assertEqual(response.status_code, 200)

    def test_analystmemos_detail_template(self):
        """ test detail view """

        # get object
        analystmemo_1 = Analystmemo.objects.get(analystmemo_note='lorem ipsum')
        # login testuser
        login = self.client.login(username='testuser_analystmemo', password='M4d878CFQiHcJQrZr4iN')
        # get response
        response = self.client.get('/analystmemos/' + str(analystmemo_1.analystmemo_id))
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/analystmemo/analystmemos_detail.html')

    def test_analystmemos_detail_get_user_context(self):
        """ test detail view """

        # get object
        analystmemo_1 = Analystmemo.objects.get(analystmemo_note='lorem ipsum')
        # login testuser
        login = self.client.login(username='testuser_analystmemo', password='M4d878CFQiHcJQrZr4iN')
        # get response
        response = self.client.get('/analystmemos/' + str(analystmemo_1.analystmemo_id))
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_analystmemo')

    def test_analystmemos_add_not_logged_in(self):
        """ test add view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/analystmemos/add/', safe='')
        # get response
        response = self.client.get('/analystmemos/add/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_analystmemos_add_logged_in(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_analystmemo', password='M4d878CFQiHcJQrZr4iN')
        # get response
        response = self.client.get('/analystmemos/add/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_analystmemos_add_template(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_analystmemo', password='M4d878CFQiHcJQrZr4iN')
        # get response
        response = self.client.get('/analystmemos/add/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/analystmemo/analystmemos_add.html')

    def test_analystmemos_add_get_user_context(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_analystmemo', password='M4d878CFQiHcJQrZr4iN')
        # get response
        response = self.client.get('/analystmemos/add/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_analystmemo')

    def test_analystmemos_edit_not_logged_in(self):
        """ test edit view """

        # get object
        analystmemo_1 = Analystmemo.objects.get(analystmemo_note='lorem ipsum')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/analystmemos/' + str(analystmemo_1.analystmemo_id) + '/edit/', safe='')
        # get response
        response = self.client.get('/analystmemos/' + str(analystmemo_1.analystmemo_id) + '/edit/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_analystmemos_edit_logged_in(self):
        """ test edit view """

        # get object
        analystmemo_1 = Analystmemo.objects.get(analystmemo_note='lorem ipsum')
        # login testuser
        login = self.client.login(username='testuser_analystmemo', password='M4d878CFQiHcJQrZr4iN')
        # get response
        response = self.client.get('/analystmemos/' + str(analystmemo_1.analystmemo_id) + '/edit/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_analystmemos_edit_template(self):
        """ test edit view """

        # get object
        analystmemo_1 = Analystmemo.objects.get(analystmemo_note='lorem ipsum')
        # login testuser
        login = self.client.login(username='testuser_analystmemo', password='M4d878CFQiHcJQrZr4iN')
        # get response
        response = self.client.get('/analystmemos/' + str(analystmemo_1.analystmemo_id) + '/edit/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/analystmemo/analystmemos_edit.html')

    def test_analystmemos_edit_get_user_context(self):
        """ test edit view """

        # get object
        analystmemo_1 = Analystmemo.objects.get(analystmemo_note='lorem ipsum')
        # login testuser
        login = self.client.login(username='testuser_analystmemo', password='M4d878CFQiHcJQrZr4iN')
        # get response
        response = self.client.get('/analystmemos/' + str(analystmemo_1.analystmemo_id) + '/edit/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_analystmemo')
