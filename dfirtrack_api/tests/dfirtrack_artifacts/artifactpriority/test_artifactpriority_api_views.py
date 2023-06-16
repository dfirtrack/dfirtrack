import urllib.parse

from django.contrib.auth.models import User
from django.test import TestCase

from dfirtrack_artifacts.models import Artifactpriority


class ArtifactpriorityAPIViewTestCase(TestCase):
    """artifactpriority API view tests"""

    @classmethod
    def setUpTestData(cls):
        # create object
        Artifactpriority.objects.create(artifactpriority_name='artifactpriority_api_1')
        # create user
        User.objects.create_user(
            username='testuser_artifactpriority_api', password='IktrZIZLncwTbOBD9Bhw'
        )

    def test_artifactpriority_list_api_unauthorized(self):
        """unauthorized access is forbidden"""

        # get response
        response = self.client.get('/api/artifactpriority/')
        # compare
        self.assertEqual(response.status_code, 401)

    def test_artifactpriority_list_api_method_get(self):
        """GET is allowed"""

        # login testuser
        self.client.login(
            username='testuser_artifactpriority_api', password='IktrZIZLncwTbOBD9Bhw'
        )
        # get response
        response = self.client.get('/api/artifactpriority/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_artifactpriority_list_api_method_post(self):
        """POST is forbidden"""

        # login testuser
        self.client.login(
            username='testuser_artifactpriority_api', password='IktrZIZLncwTbOBD9Bhw'
        )
        # create POST string
        poststring = {"artifactpriority_name": "artifactpriority_api_2"}
        # get response
        response = self.client.post('/api/artifactpriority/', data=poststring)
        # compare
        self.assertEqual(response.status_code, 405)

    def test_artifactpriority_list_api_redirect(self):
        """test redirect with appending slash"""

        # login testuser
        self.client.login(
            username='testuser_artifactpriority_api', password='IktrZIZLncwTbOBD9Bhw'
        )
        # create url
        destination = urllib.parse.quote('/api/artifactpriority/', safe='/')
        # get response
        response = self.client.get('/api/artifactpriority', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )

    def test_artifactpriority_detail_api_unauthorized(self):
        """unauthorized access is forbidden"""

        # get object
        artifactpriority_api_1 = Artifactpriority.objects.get(
            artifactpriority_name='artifactpriority_api_1'
        )
        # get response
        response = self.client.get(
            '/api/artifactpriority/'
            + str(artifactpriority_api_1.artifactpriority_id)
            + '/'
        )
        # compare
        self.assertEqual(response.status_code, 401)

    def test_artifactpriority_detail_api_method_get(self):
        """GET is allowed"""

        # get object
        artifactpriority_api_1 = Artifactpriority.objects.get(
            artifactpriority_name='artifactpriority_api_1'
        )
        # login testuser
        self.client.login(
            username='testuser_artifactpriority_api', password='IktrZIZLncwTbOBD9Bhw'
        )
        # get response
        response = self.client.get(
            '/api/artifactpriority/'
            + str(artifactpriority_api_1.artifactpriority_id)
            + '/'
        )
        # compare
        self.assertEqual(response.status_code, 200)

    def test_artifactpriority_detail_api_method_delete(self):
        """DELETE is forbidden"""

        # get object
        artifactpriority_api_1 = Artifactpriority.objects.get(
            artifactpriority_name='artifactpriority_api_1'
        )
        # login testuser
        self.client.login(
            username='testuser_artifactpriority_api', password='IktrZIZLncwTbOBD9Bhw'
        )
        # get response
        response = self.client.delete(
            '/api/artifactpriority/'
            + str(artifactpriority_api_1.artifactpriority_id)
            + '/'
        )
        # compare
        self.assertEqual(response.status_code, 405)

    def test_artifactpriority_detail_api_method_put(self):
        """PUT is forbidden"""

        # get object
        artifactpriority_api_1 = Artifactpriority.objects.get(
            artifactpriority_name='artifactpriority_api_1'
        )
        # login testuser
        self.client.login(
            username='testuser_artifactpriority_api', password='IktrZIZLncwTbOBD9Bhw'
        )
        # create url
        destination = urllib.parse.quote(
            '/api/artifactpriority/'
            + str(artifactpriority_api_1.artifactpriority_id)
            + '/',
            safe='/',
        )
        # create PUT string
        putstring = {"artifactpriority_name": "new_artifactpriority_api_1"}
        # get response
        response = self.client.put(
            destination, data=putstring, content_type='application/json'
        )
        # compare
        self.assertEqual(response.status_code, 405)

    def test_artifactpriority_detail_api_redirect(self):
        """test redirect with appending slash"""

        # get object
        artifactpriority_api_1 = Artifactpriority.objects.get(
            artifactpriority_name='artifactpriority_api_1'
        )
        # login testuser
        self.client.login(
            username='testuser_artifactpriority_api', password='IktrZIZLncwTbOBD9Bhw'
        )
        # create url
        destination = urllib.parse.quote(
            '/api/artifactpriority/'
            + str(artifactpriority_api_1.artifactpriority_id)
            + '/',
            safe='/',
        )
        # get response
        response = self.client.get(
            '/api/artifactpriority/' + str(artifactpriority_api_1.artifactpriority_id),
            follow=True,
        )
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )
