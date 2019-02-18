from django.contrib.auth.models import User
from django.test import TestCase
from dfirtrack_main.models import Reason
from dfirtrack_main.views import reasons_views
import urllib.parse

class ReasonViewTestCase(TestCase):
    """ reason view tests """

    @classmethod
    def setUpTestData(cls):

        # create object
        Reason.objects.create(reason_name='reason_1', reason_note='lorem ipsum')
        # create user
        test_user = User.objects.create_user(username='testuser', password='jjSeshxL17aDEdqkt8tP')
        test_user.save()

    def test_reasons_list_not_logged_in(self):

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/reasons/', safe='')
        # get response
        response = self.client.get('/reasons/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_reasons_list_logged_in(self):

        # login testuser
        login = self.client.login(username='testuser', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/reasons/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_reasons_list_template(self):

        # login testuser
        login = self.client.login(username='testuser', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/reasons/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/reason/reasons_list.html')

    def test_reasons_list_get_user_context(self):

        # login testuser
        login = self.client.login(username='testuser', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/reasons/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser')

    def test_reasons_detail_not_logged_in(self):

        # get object
        reason_1 = Reason.objects.get(reason_name='reason_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/reasons/' + str(reason_1.reason_id), safe='')
        # get response
        response = self.client.get('/reasons/' + str(reason_1.reason_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_reasons_detail_logged_in(self):

        # get object
        reason_1 = Reason.objects.get(reason_name='reason_1')
        # login testuser
        login = self.client.login(username='testuser', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/reasons/' + str(reason_1.reason_id))
        # compare
        self.assertEqual(response.status_code, 200)

    def test_reasons_detail_template(self):

        # get object
        reason_1 = Reason.objects.get(reason_name='reason_1')
        # login testuser
        login = self.client.login(username='testuser', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/reasons/' + str(reason_1.reason_id))
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/reason/reasons_detail.html')

    def test_reasons_detail_get_user_context(self):

        # get object
        reason_1 = Reason.objects.get(reason_name='reason_1')
        # login testuser
        login = self.client.login(username='testuser', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/reasons/' + str(reason_1.reason_id))
        # compare
        self.assertEqual(str(response.context['user']), 'testuser')

    def test_reasons_add_not_logged_in(self):

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/reasons/add', safe='')
        # get response
        response = self.client.get('/reasons/add', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_reasons_add_logged_in(self):

        # login testuser
        login = self.client.login(username='testuser', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/reasons/add')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_reasons_add_template(self):

        # login testuser
        login = self.client.login(username='testuser', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/reasons/add')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/reason/reasons_add.html')

    def test_reasons_add_get_user_context(self):

        # login testuser
        login = self.client.login(username='testuser', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/reasons/add')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser')

    def test_reasons_edit_not_logged_in(self):

        # get object
        reason_1 = Reason.objects.get(reason_name='reason_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/reasons/' + str(reason_1.reason_id) + '/edit/', safe='')
        # get response
        response = self.client.get('/reasons/' + str(reason_1.reason_id) + '/edit/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_reasons_edit_logged_in(self):

        # get object
        reason_1 = Reason.objects.get(reason_name='reason_1')
        # login testuser
        login = self.client.login(username='testuser', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/reasons/' + str(reason_1.reason_id) + '/edit/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_reasons_edit_template(self):

        # get object
        reason_1 = Reason.objects.get(reason_name='reason_1')
        # login testuser
        login = self.client.login(username='testuser', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/reasons/' + str(reason_1.reason_id) + '/edit/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/reason/reasons_edit.html')

    def test_reasons_edit_get_user_context(self):

        # get object
        reason_1 = Reason.objects.get(reason_name='reason_1')
        # login testuser
        login = self.client.login(username='testuser', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/reasons/' + str(reason_1.reason_id) + '/edit/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser')

#    def test_reasons_detail_logged_in_not_existing(self):
#
#        # login testuser
#        login = self.client.login(username='testuser', password='jjSeshxL17aDEdqkt8tP')
#        # get response
#        response = self.client.get('/reasons/x')
#        # compare
#        self.assertEqual(response.status_code, 404)
