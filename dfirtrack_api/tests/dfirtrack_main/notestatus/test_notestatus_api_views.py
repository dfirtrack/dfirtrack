from django.contrib.auth.models import User
from django.test import TestCase
from dfirtrack_main.models import Notestatus
import urllib.parse


class NotestatusAPIViewTestCase(TestCase):
    """ notestatus API view tests """

    @classmethod
    def setUpTestData(cls):

        # create object
        Notestatus.objects.create(notestatus_name='notestatus_api_1')
        # create user
        User.objects.create_user(username='testuser_notestatus_api', password='MacT9WxkBEz2w5a6B0v6')

    def test_notestatus_list_api_unauthorized(self):
        """ unauthorized access is forbidden"""

        # get response
        response = self.client.get('/api/notestatus/')
        # compare
        self.assertEqual(response.status_code, 401)

    def test_notestatus_list_api_method_get(self):
        """ GET is allowed """

        # login testuser
        self.client.login(username='testuser_notestatus_api', password='MacT9WxkBEz2w5a6B0v6')
        # get response
        response = self.client.get('/api/notestatus/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_notestatus_list_api_method_post(self):
        """ POST is forbidden """

        # login testuser
        self.client.login(username='testuser_notestatus_api', password='MacT9WxkBEz2w5a6B0v6')
        # create POST string
        poststring = {"notestatus_name": "notestatus_api_2"}
        # get response
        response = self.client.post('/api/notestatus/', data=poststring)
        # compare
        self.assertEqual(response.status_code, 405)

    def test_notestatus_list_api_redirect(self):
        """ test redirect with appending slash """

        # login testuser
        self.client.login(username='testuser_notestatus_api', password='MacT9WxkBEz2w5a6B0v6')
        # create url
        destination = urllib.parse.quote('/api/notestatus/', safe='/')
        # get response
        response = self.client.get('/api/notestatus', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_notestatus_detail_api_unauthorized (self):
        """ unauthorized access is forbidden"""

        # get object
        notestatus_api_1 = Notestatus.objects.get(notestatus_name='notestatus_api_1')
        # get response
        response = self.client.get('/api/notestatus/' + str(notestatus_api_1.notestatus_id) + '/')
        # compare
        self.assertEqual(response.status_code, 401)

    def test_notestatus_detail_api_method_get(self):
        """ GET is allowed """

        # get object
        notestatus_api_1 = Notestatus.objects.get(notestatus_name='notestatus_api_1')
        # login testuser
        self.client.login(username='testuser_notestatus_api', password='MacT9WxkBEz2w5a6B0v6')
        # get response
        response = self.client.get('/api/notestatus/' + str(notestatus_api_1.notestatus_id) + '/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_notestatus_detail_api_method_delete(self):
        """ DELETE is forbidden """

        # get object
        notestatus_api_1 = Notestatus.objects.get(notestatus_name='notestatus_api_1')
        # login testuser
        self.client.login(username='testuser_notestatus_api', password='MacT9WxkBEz2w5a6B0v6')
        # get response
        response = self.client.delete('/api/notestatus/' + str(notestatus_api_1.notestatus_id) + '/')
        # compare
        self.assertEqual(response.status_code, 405)

    def test_notestatus_detail_api_method_put(self):
        """ PUT is forbidden """

        # get object
        notestatus_api_1 = Notestatus.objects.get(notestatus_name='notestatus_api_1')
        # login testuser
        self.client.login(username='testuser_notestatus_api', password='MacT9WxkBEz2w5a6B0v6')
        # create url
        destination = urllib.parse.quote('/api/notestatus/' + str(notestatus_api_1.notestatus_id) + '/', safe='/')
        # create PUT string
        putstring = {"notestatus_name": "new_notestatus_api_1"}
        # get response
        response = self.client.put(destination, data=putstring, content_type='application/json')
        # compare
        self.assertEqual(response.status_code, 405)

    def test_notestatus_detail_api_redirect(self):
        """ test redirect with appending slash """

        # get object
        notestatus_api_1 = Notestatus.objects.get(notestatus_name='notestatus_api_1')
        # login testuser
        self.client.login(username='testuser_notestatus_api', password='MacT9WxkBEz2w5a6B0v6')
        # create url
        destination = urllib.parse.quote('/api/notestatus/' + str(notestatus_api_1.notestatus_id) + '/', safe='/')
        # get response
        response = self.client.get('/api/notestatus/' + str(notestatus_api_1.notestatus_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)
