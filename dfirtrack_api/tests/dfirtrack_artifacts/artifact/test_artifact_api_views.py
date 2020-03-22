from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone
from dfirtrack_artifacts.models import Artifact, Artifactstatus, Artifacttype
from dfirtrack_main.models import System, Systemstatus
import urllib.parse

class ArtifactAPIViewTestCase(TestCase):
    """ artifact API view tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_artifact_api', password='rQeyaRKd7Lt6D518TTzv')

        # create object
        systemstatus_1 = Systemstatus.objects.create(systemstatus_name='systemstatus_1')

        # create object
        system_1 = System.objects.create(
            system_name = 'system_1',
            systemstatus = systemstatus_1,
            system_modify_time = timezone.now(),
            system_created_by_user_id = test_user,
            system_modified_by_user_id = test_user,
        )

        # create object
        artifactstatus_1 = Artifactstatus.objects.create(artifactstatus_name='artifactstatus_1')

        # create object
        artifacttype_1 = Artifacttype.objects.create(artifacttype_name='artifacttype_1')

        # create object
        Artifact.objects.create(
            artifact_name='artifact_api_1',
            artifactstatus = artifactstatus_1,
            artifacttype = artifacttype_1,
            system = system_1,
            artifact_created_by_user_id = test_user,
            artifact_modified_by_user_id = test_user,
        )

    def test_artifact_list_api_unauthorized(self):
        """ unauthorized access is forbidden"""

        # get response
        response = self.client.get('/api/artifacts/')
        # compare
        self.assertEqual(response.status_code, 401)

    def test_artifact_list_api_method_get(self):
        """ GET is allowed """

        # login testuser
        login = self.client.login(username='testuser_artifact_api', password='rQeyaRKd7Lt6D518TTzv')
        # get response
        response = self.client.get('/api/artifacts/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_artifact_list_api_method_post(self):
        """ POST is forbidden """

        # login testuser
        login = self.client.login(username='testuser_artifact_api', password='rQeyaRKd7Lt6D518TTzv')
        # create POST string
        poststring = {"artifact_name": "artifact_api_2"}
        # get response
        response = self.client.post('/api/artifacts/', data=poststring)
        # compare
        self.assertEqual(response.status_code, 405)

    def test_artifact_list_api_redirect(self):
        """ test redirect with appending slash """

        # login testuser
        login = self.client.login(username='testuser_artifact_api', password='rQeyaRKd7Lt6D518TTzv')
        # create url
        destination = urllib.parse.quote('/api/artifacts/', safe='/')
        # get response
        response = self.client.get('/api/artifacts', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_artifact_detail_api_unauthorized (self):
        """ unauthorized access is forbidden"""

        # get object
        artifact_api_1 = Artifact.objects.get(artifact_name='artifact_api_1')
        # get response
        response = self.client.get('/api/artifacts/' + str(artifact_api_1.artifact_id) + '/')
        # compare
        self.assertEqual(response.status_code, 401)

    def test_artifact_detail_api_method_get(self):
        """ GET is allowed """

        # get object
        artifact_api_1 = Artifact.objects.get(artifact_name='artifact_api_1')
        # login testuser
        login = self.client.login(username='testuser_artifact_api', password='rQeyaRKd7Lt6D518TTzv')
        # get response
        response = self.client.get('/api/artifacts/' + str(artifact_api_1.artifact_id) + '/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_artifact_detail_api_method_delete(self):
        """ DELETE is forbidden """

        # get object
        artifact_api_1 = Artifact.objects.get(artifact_name='artifact_api_1')
        # login testuser
        login = self.client.login(username='testuser_artifact_api', password='rQeyaRKd7Lt6D518TTzv')
        # get response
        response = self.client.delete('/api/artifacts/' + str(artifact_api_1.artifact_id) + '/')
        # compare
        self.assertEqual(response.status_code, 405)

    def test_artifact_detail_api_method_put(self):
        """ PUT is forbidden """

        # get object
        artifact_api_1 = Artifact.objects.get(artifact_name='artifact_api_1')
        # login testuser
        login = self.client.login(username='testuser_artifact_api', password='rQeyaRKd7Lt6D518TTzv')
        # create url
        destination = urllib.parse.quote('/api/artifacts/' + str(artifact_api_1.artifact_id) + '/', safe='/')
        # create PUT string
        putstring = {"artifact_name": "new_artifact_api_1"}
        # get response
        response = self.client.put(destination, data=putstring, content_='application/json')
        # compare
        self.assertEqual(response.status_code, 405)

    def test_artifact_detail_api_redirect(self):
        """ test redirect with appending slash """

        # get object
        artifact_api_1 = Artifact.objects.get(artifact_name='artifact_api_1')
        # login testuser
        login = self.client.login(username='testuser_artifact_api', password='rQeyaRKd7Lt6D518TTzv')
        # create url
        destination = urllib.parse.quote('/api/artifacts/' + str(artifact_api_1.artifact_id) + '/', safe='/')
        # get response
        response = self.client.get('/api/artifacts/' + str(artifact_api_1.artifact_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)
