import urllib.parse

from dfirtrack_artifacts.models import Artifactpriority, Artifactstatus, Artifacttype
from dfirtrack_main.models import System, Systemstatus
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import TestCase


class ArtifactCreatorViewTestCase(TestCase):
    """artifact creator view tests"""

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(
            username='testuser_artifact_creator', password='bHLMxCuEAUOv6WSwu26X'
        )

        # create objects
        Artifactpriority.objects.create(artifactpriority_name='artifactpriority_1')
        Artifactstatus.objects.create(artifactstatus_name='artifactstatus_1')

        # create objects
        Artifacttype.objects.create(artifacttype_name='artifact_creator_artifacttype_1')
        Artifacttype.objects.create(artifacttype_name='artifact_creator_artifacttype_2')
        Artifacttype.objects.create(artifacttype_name='artifact_creator_artifacttype_3')

        # create object
        systemstatus_1 = Systemstatus.objects.create(systemstatus_name='systemstatus_1')
        # create objects
        System.objects.create(
            system_name='artifact_creator_system_1',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )
        System.objects.create(
            system_name='artifact_creator_system_2',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )
        System.objects.create(
            system_name='artifact_creator_system_3',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )

    def test_artifact_creator_not_logged_in(self):
        """test creator view"""

        # create url
        destination = '/login/?next=' + urllib.parse.quote(
            '/artifacts/artifact/creator/', safe=''
        )
        # get response
        response = self.client.get('/artifacts/artifact/creator/', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_artifact_creator_logged_in(self):
        """test creator view"""

        # login testuser
        self.client.login(
            username='testuser_artifact_creator', password='bHLMxCuEAUOv6WSwu26X'
        )
        # get response
        response = self.client.get('/artifacts/artifact/creator/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_artifact_creator_template(self):
        """test creator view"""

        # login testuser
        self.client.login(
            username='testuser_artifact_creator', password='bHLMxCuEAUOv6WSwu26X'
        )
        # get response
        response = self.client.get('/artifacts/artifact/creator/')
        # compare
        self.assertTemplateUsed(
            response, 'dfirtrack_artifacts/artifact/artifact_creator.html'
        )

    def test_artifact_creator_get_user_context(self):
        """test creator view"""

        # login testuser
        self.client.login(
            username='testuser_artifact_creator', password='bHLMxCuEAUOv6WSwu26X'
        )
        # get response
        response = self.client.get('/artifacts/artifact/creator/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_artifact_creator')

    def test_artifact_creator_redirect(self):
        """test creator view"""

        # login testuser
        self.client.login(
            username='testuser_artifact_creator', password='bHLMxCuEAUOv6WSwu26X'
        )
        # create url
        destination = urllib.parse.quote('/artifacts/artifact/creator/', safe='/')
        # get response
        response = self.client.get('/artifacts/artifact/creator', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )

    def test_artifact_creator_post_redirect(self):
        """test creator view"""

        # login testuser
        self.client.login(
            username='testuser_artifact_creator', password='bHLMxCuEAUOv6WSwu26X'
        )
        # get objects
        artifactpriority_1 = Artifactpriority.objects.get(
            artifactpriority_name='artifactpriority_1'
        )
        artifactstatus_1 = Artifactstatus.objects.get(
            artifactstatus_name='artifactstatus_1'
        )
        artifacttype_1 = Artifacttype.objects.get(
            artifacttype_name='artifact_creator_artifacttype_1'
        )
        system_1 = System.objects.get(system_name='artifact_creator_system_1')
        # create post data
        data_dict = {
            'artifactpriority': artifactpriority_1.artifactpriority_id,
            'artifactstatus': artifactstatus_1.artifactstatus_id,
            'artifacttype': [
                artifacttype_1.artifacttype_id,
            ],
            'system': [
                system_1.system_id,
            ],
        }
        # create url
        destination = '/artifacts/artifact/'
        # get response
        response = self.client.post('/artifacts/artifact/creator/', data_dict)
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_artifact_creator_post_system_and_artifacts(self):
        """test creator view"""

        # login testuser
        self.client.login(
            username='testuser_artifact_creator', password='bHLMxCuEAUOv6WSwu26X'
        )
        # get objects
        artifactpriority_1 = Artifactpriority.objects.get(
            artifactpriority_name='artifactpriority_1'
        )
        artifactstatus_1 = Artifactstatus.objects.get(
            artifactstatus_name='artifactstatus_1'
        )
        artifacttype_1 = Artifacttype.objects.get(
            artifacttype_name='artifact_creator_artifacttype_1'
        )
        artifacttype_2 = Artifacttype.objects.get(
            artifacttype_name='artifact_creator_artifacttype_2'
        )
        artifacttype_3 = Artifacttype.objects.get(
            artifacttype_name='artifact_creator_artifacttype_3'
        )
        system_1 = System.objects.get(system_name='artifact_creator_system_1')
        system_2 = System.objects.get(system_name='artifact_creator_system_2')
        system_3 = System.objects.get(system_name='artifact_creator_system_3')
        # create post data
        data_dict = {
            'artifactpriority': artifactpriority_1.artifactpriority_id,
            'artifactstatus': artifactstatus_1.artifactstatus_id,
            'artifacttype': [
                artifacttype_1.artifacttype_id,
                artifacttype_2.artifacttype_id,
            ],
            'system': [system_1.system_id, system_2.system_id],
        }
        # get response
        self.client.post('/artifacts/artifact/creator/', data_dict)
        # compare
        self.assertTrue(
            system_1.artifact_system.filter(artifacttype=artifacttype_1).exists()
        )
        self.assertTrue(
            system_1.artifact_system.filter(artifacttype=artifacttype_2).exists()
        )
        self.assertFalse(
            system_1.artifact_system.filter(artifacttype=artifacttype_3).exists()
        )
        self.assertTrue(
            system_2.artifact_system.filter(artifacttype=artifacttype_1).exists()
        )
        self.assertTrue(
            system_2.artifact_system.filter(artifacttype=artifacttype_2).exists()
        )
        self.assertFalse(
            system_2.artifact_system.filter(artifacttype=artifacttype_3).exists()
        )
        self.assertFalse(
            system_3.artifact_system.filter(artifacttype=artifacttype_1).exists()
        )
        self.assertFalse(
            system_3.artifact_system.filter(artifacttype=artifacttype_2).exists()
        )
        self.assertFalse(
            system_3.artifact_system.filter(artifacttype=artifacttype_3).exists()
        )

    def test_artifact_creator_post_invalid_reload(self):
        """test creator view"""

        # login testuser
        self.client.login(
            username='testuser_artifact_creator', password='bHLMxCuEAUOv6WSwu26X'
        )
        # create post data
        data_dict = {}
        # get response
        response = self.client.post('/artifacts/artifact/creator/', data_dict)
        # compare
        self.assertEqual(response.status_code, 200)

    def test_artifact_creator_post_invalid_template(self):
        """test creator view"""

        # login testuser
        self.client.login(
            username='testuser_artifact_creator', password='bHLMxCuEAUOv6WSwu26X'
        )
        # create post data
        data_dict = {}
        # get response
        response = self.client.post('/artifacts/artifact/creator/', data_dict)
        # compare
        self.assertTemplateUsed(
            response, 'dfirtrack_artifacts/artifact/artifact_creator.html'
        )

    def test_artifact_creator_post_messages(self):
        """test creator view"""

        # login testuser
        self.client.login(
            username='testuser_artifact_creator', password='bHLMxCuEAUOv6WSwu26X'
        )
        # get objects
        artifactpriority_1 = Artifactpriority.objects.get(
            artifactpriority_name='artifactpriority_1'
        )
        artifactstatus_1 = Artifactstatus.objects.get(
            artifactstatus_name='artifactstatus_1'
        )
        artifacttype_1 = Artifacttype.objects.get(
            artifacttype_name='artifact_creator_artifacttype_1'
        )
        artifacttype_2 = Artifacttype.objects.get(
            artifacttype_name='artifact_creator_artifacttype_2'
        )
        artifacttype_3 = Artifacttype.objects.get(
            artifacttype_name='artifact_creator_artifacttype_3'
        )
        system_1 = System.objects.get(system_name='artifact_creator_system_1')
        system_2 = System.objects.get(system_name='artifact_creator_system_2')
        system_3 = System.objects.get(system_name='artifact_creator_system_3')
        # create post data
        data_dict = {
            'artifactpriority': artifactpriority_1.artifactpriority_id,
            'artifactstatus': artifactstatus_1.artifactstatus_id,
            'artifacttype': [
                artifacttype_1.artifacttype_id,
                artifacttype_2.artifacttype_id,
                artifacttype_3.artifacttype_id,
            ],
            'system': [system_1.system_id, system_2.system_id, system_3.system_id],
        }
        # get response
        response = self.client.post('/artifacts/artifact/creator/', data_dict)
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(str(messages[0]), 'Artifact creator started')
        self.assertEqual(str(messages[1]), '9 artifacts created for 3 systems.')
