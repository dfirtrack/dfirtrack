import urllib.parse

from django.contrib.auth.models import User
from django.test import TestCase

from dfirtrack_main.models import Analysisstatus


class AnalysisstatusAPIViewTestCase(TestCase):
    """analysisstatus API view tests"""

    @classmethod
    def setUpTestData(cls):

        # create object
        Analysisstatus.objects.create(analysisstatus_name='analysisstatus_api_1')
        # create user
        User.objects.create_user(
            username='testuser_analysisstatus_api', password='aCTVRIdJ4cyVSkYiJKrM'
        )

    def test_analysisstatus_list_api_unauthorized(self):
        """unauthorized access is forbidden"""

        # get response
        response = self.client.get('/api/analysisstatus/')
        # compare
        self.assertEqual(response.status_code, 401)

    def test_analysisstatus_list_api_method_get(self):
        """GET is allowed"""

        # login testuser
        self.client.login(
            username='testuser_analysisstatus_api', password='aCTVRIdJ4cyVSkYiJKrM'
        )
        # get response
        response = self.client.get('/api/analysisstatus/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_analysisstatus_list_api_method_post(self):
        """POST is forbidden"""

        # login testuser
        self.client.login(
            username='testuser_analysisstatus_api', password='aCTVRIdJ4cyVSkYiJKrM'
        )
        # create POST string
        poststring = {"analysisstatus_name": "analysisstatus_api_2"}
        # get response
        response = self.client.post('/api/analysisstatus/', data=poststring)
        # compare
        self.assertEqual(response.status_code, 405)

    def test_analysisstatus_list_api_redirect(self):
        """test redirect with appending slash"""

        # login testuser
        self.client.login(
            username='testuser_analysisstatus_api', password='aCTVRIdJ4cyVSkYiJKrM'
        )
        # create url
        destination = urllib.parse.quote('/api/analysisstatus/', safe='/')
        # get response
        response = self.client.get('/api/analysisstatus', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )

    def test_analysisstatus_detail_api_unauthorized(self):
        """unauthorized access is forbidden"""

        # get object
        analysisstatus_api_1 = Analysisstatus.objects.get(
            analysisstatus_name='analysisstatus_api_1'
        )
        # get response
        response = self.client.get(
            '/api/analysisstatus/' + str(analysisstatus_api_1.analysisstatus_id) + '/'
        )
        # compare
        self.assertEqual(response.status_code, 401)

    def test_analysisstatus_detail_api_method_get(self):
        """GET is allowed"""

        # get object
        analysisstatus_api_1 = Analysisstatus.objects.get(
            analysisstatus_name='analysisstatus_api_1'
        )
        # login testuser
        self.client.login(
            username='testuser_analysisstatus_api', password='aCTVRIdJ4cyVSkYiJKrM'
        )
        # get response
        response = self.client.get(
            '/api/analysisstatus/' + str(analysisstatus_api_1.analysisstatus_id) + '/'
        )
        # compare
        self.assertEqual(response.status_code, 200)

    def test_analysisstatus_detail_api_method_delete(self):
        """DELETE is forbidden"""

        # get object
        analysisstatus_api_1 = Analysisstatus.objects.get(
            analysisstatus_name='analysisstatus_api_1'
        )
        # login testuser
        self.client.login(
            username='testuser_analysisstatus_api', password='aCTVRIdJ4cyVSkYiJKrM'
        )
        # get response
        response = self.client.delete(
            '/api/analysisstatus/' + str(analysisstatus_api_1.analysisstatus_id) + '/'
        )
        # compare
        self.assertEqual(response.status_code, 405)

    def test_analysisstatus_detail_api_method_put(self):
        """PUT is forbidden"""

        # get object
        analysisstatus_api_1 = Analysisstatus.objects.get(
            analysisstatus_name='analysisstatus_api_1'
        )
        # login testuser
        self.client.login(
            username='testuser_analysisstatus_api', password='aCTVRIdJ4cyVSkYiJKrM'
        )
        # create url
        destination = urllib.parse.quote(
            '/api/analysisstatus/' + str(analysisstatus_api_1.analysisstatus_id) + '/',
            safe='/',
        )
        # create PUT string
        putstring = {"analysisstatus_name": "new_analysisstatus_api_1"}
        # get response
        response = self.client.put(
            destination, data=putstring, content_type='application/json'
        )
        # compare
        self.assertEqual(response.status_code, 405)

    def test_analysisstatus_detail_api_redirect(self):
        """test redirect with appending slash"""

        # get object
        analysisstatus_api_1 = Analysisstatus.objects.get(
            analysisstatus_name='analysisstatus_api_1'
        )
        # login testuser
        self.client.login(
            username='testuser_analysisstatus_api', password='aCTVRIdJ4cyVSkYiJKrM'
        )
        # create url
        destination = urllib.parse.quote(
            '/api/analysisstatus/' + str(analysisstatus_api_1.analysisstatus_id) + '/',
            safe='/',
        )
        # get response
        response = self.client.get(
            '/api/analysisstatus/' + str(analysisstatus_api_1.analysisstatus_id),
            follow=True,
        )
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )
