from django.contrib.auth.models import User
from django.test import TestCase
from dfirtrack_artifacts.models import Artifactstatus
import urllib.parse

class ArtifactstatusAPIViewTestCase(TestCase):
    """ artifactstatus API view tests """

    @classmethod
    def setUpTestData(cls):

        # create object
        Artifactstatus.objects.create(artifactstatus_name='artifactstatus_api_1')
        # create user
        test_user = User.objects.create_user(username='testuser_artifactstatus_api', password='aCTVRIdJ4cyVSkYiJKrM')

    def test_artifactstatus_list_api_unauthorized(self):
        """ unauthorized access is forbidden"""

        # get response
        response = self.client.get('/api/artifactstatuss/')
        # compare
        self.assertEqual(response.status_code, 401)

    def test_artifactstatus_list_api_method_get(self):
        """ GET is allowed """

        # login testuser
        login = self.client.login(username='testuser_artifactstatus_api', password='aCTVRIdJ4cyVSkYiJKrM')
        # get response
        response = self.client.get('/api/artifactstatuss/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_artifactstatus_list_api_method_post(self):
        """ POST is forbidden """

        # login testuser
        login = self.client.login(username='testuser_artifactstatus_api', password='aCTVRIdJ4cyVSkYiJKrM')
        # create POST string
        poststring = {"artifactstatus_name": "artifactstatus_api_2"}
        # get response
        response = self.client.post('/api/artifactstatuss/', data=poststring)
        # compare
        self.assertEqual(response.status_code, 405)

    def test_artifactstatus_list_api_redirect(self):
        """ test redirect with appending slash """

        # login testuser
        login = self.client.login(username='testuser_artifactstatus_api', password='aCTVRIdJ4cyVSkYiJKrM')
        # create url
        destination = urllib.parse.quote('/api/artifactstatuss/', safe='/')
        # get response
        response = self.client.get('/api/artifactstatuss', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

#    def test_artifactstatus_list_api_get_user_context(self):
#        """ test user context """
#
#        # login testuser
#        login = self.client.login(username='testuser_artifactstatus_api', password='aCTVRIdJ4cyVSkYiJKrM')
#        # get response
#        response = self.client.get('/api/artifactstatuss/')
#        # compare
#        self.assertEqual(str(response.context['user']), 'testuser_artifactstatus_api')

    def test_artifactstatus_detail_api_unauthorized (self):
        """ unauthorized access is forbidden"""

        # get object
        artifactstatus_api_1 = Artifactstatus.objects.get(artifactstatus_name='artifactstatus_api_1')
        # get response
        response = self.client.get('/api/artifactstatuss/' + str(artifactstatus_api_1.artifactstatus_id) + '/')
        # compare
        self.assertEqual(response.status_code, 401)

    def test_artifactstatus_detail_api_method_get(self):
        """ GET is allowed """

        # get object
        artifactstatus_api_1 = Artifactstatus.objects.get(artifactstatus_name='artifactstatus_api_1')
        # login testuser
        login = self.client.login(username='testuser_artifactstatus_api', password='aCTVRIdJ4cyVSkYiJKrM')
        # get response
        response = self.client.get('/api/artifactstatuss/' + str(artifactstatus_api_1.artifactstatus_id) + '/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_artifactstatus_detail_api_method_delete(self):
        """ DELETE is forbidden """

        # get object
        artifactstatus_api_1 = Artifactstatus.objects.get(artifactstatus_name='artifactstatus_api_1')
        # login testuser
        login = self.client.login(username='testuser_artifactstatus_api', password='aCTVRIdJ4cyVSkYiJKrM')
        # get response
        response = self.client.delete('/api/artifactstatuss/' + str(artifactstatus_api_1.artifactstatus_id) + '/')
        # compare
        self.assertEqual(response.status_code, 405)

    def test_artifactstatus_detail_api_method_put(self):
        """ PUT is forbidden """

        # get object
        artifactstatus_api_1 = Artifactstatus.objects.get(artifactstatus_name='artifactstatus_api_1')
        # login testuser
        login = self.client.login(username='testuser_artifactstatus_api', password='aCTVRIdJ4cyVSkYiJKrM')
        # create url
        destination = urllib.parse.quote('/api/artifactstatuss/' + str(artifactstatus_api_1.artifactstatus_id) + '/', safe='/')
        # create PUT string
        putstring = {"artifactstatus_name": "new_artifactstatus_api_1"}
        # get response
        response = self.client.put(destination, data=putstring, content_type='application/json')
        # compare
        self.assertEqual(response.status_code, 405)

    def test_artifactstatus_detail_api_redirect(self):
        """ test redirect with appending slash """

        # get object
        artifactstatus_api_1 = Artifactstatus.objects.get(artifactstatus_name='artifactstatus_api_1')
        # login testuser
        login = self.client.login(username='testuser_artifactstatus_api', password='aCTVRIdJ4cyVSkYiJKrM')
        # create url
        destination = urllib.parse.quote('/api/artifactstatuss/' + str(artifactstatus_api_1.artifactstatus_id) + '/', safe='/')
        # get response
        response = self.client.get('/api/artifactstatuss/' + str(artifactstatus_api_1.artifactstatus_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

#    def test_artifactstatus_detail_api_get_user_context(self):
#        """ test user context """
#
#        # get object
#        artifactstatus_api_1 = Artifactstatus.objects.get(artifactstatus_name='artifactstatus_api_1')
#        # login testuser
#        login = self.client.login(username='testuser_artifactstatus_api', password='aCTVRIdJ4cyVSkYiJKrM')
#        # get response
#        response = self.client.get('/api/artifactstatuss/' + str(artifactstatus_api_1.artifactstatus_id) + '/')
#        # compare
#        self.assertEqual(str(response.context['user']), 'testuser_artifactstatus_api')
