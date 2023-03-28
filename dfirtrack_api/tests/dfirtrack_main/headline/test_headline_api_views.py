import urllib.parse

from django.contrib.auth.models import User
from django.test import TestCase

from dfirtrack_main.models import Headline


class HeadlineAPIViewTestCase(TestCase):
    """headline API view tests"""

    @classmethod
    def setUpTestData(cls):
        # create object
        Headline.objects.create(headline_name='headline_api_1')
        # create user
        User.objects.create_user(
            username='testuser_headline_api', password='8ERK3w9IgLNnp1q84faX'
        )

    def test_headline_list_api_unauthorized(self):
        """unauthorized access is forbidden"""

        # get response
        response = self.client.get('/api/headline/')
        # compare
        self.assertEqual(response.status_code, 401)

    def test_headline_list_api_method_get(self):
        """GET is allowed"""

        # login testuser
        self.client.login(
            username='testuser_headline_api', password='8ERK3w9IgLNnp1q84faX'
        )
        # get response
        response = self.client.get('/api/headline/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_headline_list_api_method_post(self):
        """POST is allowed"""

        # login testuser
        self.client.login(
            username='testuser_headline_api', password='8ERK3w9IgLNnp1q84faX'
        )
        # create POST string
        poststring = {"headline_name": "headline_api_2"}
        # get response
        response = self.client.post('/api/headline/', data=poststring)
        # compare
        self.assertEqual(response.status_code, 201)

    def test_headline_list_api_redirect(self):
        """test redirect with appending slash"""

        # login testuser
        self.client.login(
            username='testuser_headline_api', password='8ERK3w9IgLNnp1q84faX'
        )
        # create url
        destination = urllib.parse.quote('/api/headline/', safe='/')
        # get response
        response = self.client.get('/api/headline', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )

    def test_headline_detail_api_unauthorized(self):
        """unauthorized access is forbidden"""

        # get object
        headline_api_1 = Headline.objects.get(headline_name='headline_api_1')
        # get response
        response = self.client.get(
            '/api/headline/' + str(headline_api_1.headline_id) + '/'
        )
        # compare
        self.assertEqual(response.status_code, 401)

    def test_headline_detail_api_method_get(self):
        """GET is allowed"""

        # get object
        headline_api_1 = Headline.objects.get(headline_name='headline_api_1')
        # login testuser
        self.client.login(
            username='testuser_headline_api', password='8ERK3w9IgLNnp1q84faX'
        )
        # get response
        response = self.client.get(
            '/api/headline/' + str(headline_api_1.headline_id) + '/'
        )
        # compare
        self.assertEqual(response.status_code, 200)

    def test_headline_detail_api_method_delete(self):
        """DELETE is forbidden"""

        # get object
        headline_api_1 = Headline.objects.get(headline_name='headline_api_1')
        # login testuser
        self.client.login(
            username='testuser_headline_api', password='8ERK3w9IgLNnp1q84faX'
        )
        # get response
        response = self.client.delete(
            '/api/headline/' + str(headline_api_1.headline_id) + '/'
        )
        # compare
        self.assertEqual(response.status_code, 405)

    def test_headline_detail_api_method_put(self):
        """PUT is allowed"""

        # get object
        headline_api_1 = Headline.objects.get(headline_name='headline_api_1')
        # login testuser
        self.client.login(
            username='testuser_headline_api', password='8ERK3w9IgLNnp1q84faX'
        )
        # create url
        destination = urllib.parse.quote(
            '/api/headline/' + str(headline_api_1.headline_id) + '/', safe='/'
        )
        # create PUT string
        putstring = {"headline_name": "new_headline_api_1"}
        # get response
        response = self.client.put(
            destination, data=putstring, content_type='application/json'
        )
        # compare
        self.assertEqual(response.status_code, 200)

    def test_headline_detail_api_redirect(self):
        """test redirect with appending slash"""

        # get object
        headline_api_1 = Headline.objects.get(headline_name='headline_api_1')
        # login testuser
        self.client.login(
            username='testuser_headline_api', password='8ERK3w9IgLNnp1q84faX'
        )
        # create url
        destination = urllib.parse.quote(
            '/api/headline/' + str(headline_api_1.headline_id) + '/', safe='/'
        )
        # get response
        response = self.client.get(
            '/api/headline/' + str(headline_api_1.headline_id), follow=True
        )
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )
