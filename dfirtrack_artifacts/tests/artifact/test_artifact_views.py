from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone
from dfirtrack_artifacts.models import Artifact, Artifactstatus, Artifacttype
from dfirtrack_main.models import System, Systemstatus
import urllib.parse

class ArtifactViewTestCase(TestCase):
    """ artifact view tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_artifact', password='frUsVT2ukTjWNDjVMBlF')

        # create object
        artifactstatus_1 = Artifactstatus.objects.create(artifactstatus_name='artifactstatus_1')

        # create object
        artifacttype_1 = Artifacttype.objects.create(artifacttype_name='artifacttype_1')

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
        Artifact.objects.create(
            artifact_name = 'artifact_1',
            artifactstatus = artifactstatus_1,
            artifacttype = artifacttype_1,
            system = system_1,
            artifact_created_by_user_id = test_user,
            artifact_modified_by_user_id = test_user,
        )

    def test_artifact_list_not_logged_in(self):
        """ test list view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/artifacts/artifact/', safe='')
        # get response
        response = self.client.get('/artifacts/artifact/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_artifact_list_logged_in(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_artifact', password='frUsVT2ukTjWNDjVMBlF')
        # get response
        response = self.client.get('/artifacts/artifact/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_artifact_list_template(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_artifact', password='frUsVT2ukTjWNDjVMBlF')
        # get response
        response = self.client.get('/artifacts/artifact/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_artifacts/artifact/artifact_list.html')

    def test_artifact_list_get_user_context(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_artifact', password='frUsVT2ukTjWNDjVMBlF')
        # get response
        response = self.client.get('/artifacts/artifact/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_artifact')

    def test_artifact_detail_not_logged_in(self):
        """ test detail view """

        # get object
        artifact_1 = Artifact.objects.get(artifact_name='artifact_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/artifacts/artifact/detail/' + str(artifact_1.artifact_id) + '/', safe='')
        # get response
        response = self.client.get('/artifacts/artifact/detail/' + str(artifact_1.artifact_id) + '/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_artifact_detail_logged_in(self):
        """ test detail view """

        # get object
        artifact_1 = Artifact.objects.get(artifact_name='artifact_1')
        # login testuser
        login = self.client.login(username='testuser_artifact', password='frUsVT2ukTjWNDjVMBlF')
        # get response
        response = self.client.get('/artifacts/artifact/detail/' + str(artifact_1.artifact_id) + '/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_artifact_detail_template(self):
        """ test detail view """

        # get object
        artifact_1 = Artifact.objects.get(artifact_name='artifact_1')
        # login testuser
        login = self.client.login(username='testuser_artifact', password='frUsVT2ukTjWNDjVMBlF')
        # get response
        response = self.client.get('/artifacts/artifact/detail/' + str(artifact_1.artifact_id) + '/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_artifacts/artifact/artifact_detail.html')

    def test_artifact_detail_get_user_context(self):
        """ test detail view """

        # get object
        artifact_1 = Artifact.objects.get(artifact_name='artifact_1')
        # login testuser
        login = self.client.login(username='testuser_artifact', password='frUsVT2ukTjWNDjVMBlF')
        # get response
        response = self.client.get('/artifacts/artifact/detail/' + str(artifact_1.artifact_id) + '/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_artifact')

    def test_artifact_create_not_logged_in(self):
        """ test create view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/artifacts/artifact/create/', safe='')
        # get response
        response = self.client.get('/artifacts/artifact/create/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_artifact_create_logged_in(self):
        """ test create view """

        # login testuser
        login = self.client.login(username='testuser_artifact', password='frUsVT2ukTjWNDjVMBlF')
        # get response
        response = self.client.get('/artifacts/artifact/create/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_artifact_create_template(self):
        """ test create view """

        # login testuser
        login = self.client.login(username='testuser_artifact', password='frUsVT2ukTjWNDjVMBlF')
        # get response
        response = self.client.get('/artifacts/artifact/create/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_artifacts/artifact/artifact_add.html')

    def test_artifact_create_get_user_context(self):
        """ test create view """

        # login testuser
        login = self.client.login(username='testuser_artifact', password='frUsVT2ukTjWNDjVMBlF')
        # get response
        response = self.client.get('/artifacts/artifact/create/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_artifact')

    def test_artifact_update_not_logged_in(self):
        """ test update view """

        # get object
        artifact_1 = Artifact.objects.get(artifact_name='artifact_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/artifacts/artifact/update/' + str(artifact_1.artifact_id) + '/', safe='')
        # get response
        response = self.client.get('/artifacts/artifact/update/' + str(artifact_1.artifact_id) + '/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_artifact_update_logged_in(self):
        """ test update view """

        # get object
        artifact_1 = Artifact.objects.get(artifact_name='artifact_1')
        # login testuser
        login = self.client.login(username='testuser_artifact', password='frUsVT2ukTjWNDjVMBlF')
        # get response
        response = self.client.get('/artifacts/artifact/update/' + str(artifact_1.artifact_id) + '/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_artifact_update_template(self):
        """ test update view """

        # get object
        artifact_1 = Artifact.objects.get(artifact_name='artifact_1')
        # login testuser
        login = self.client.login(username='testuser_artifact', password='frUsVT2ukTjWNDjVMBlF')
        # get response
        response = self.client.get('/artifacts/artifact/update/' + str(artifact_1.artifact_id) + '/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_artifacts/artifact/artifact_edit.html')

    def test_artifact_update_get_user_context(self):
        """ test update view """

        # get object
        artifact_1 = Artifact.objects.get(artifact_name='artifact_1')
        # login testuser
        login = self.client.login(username='testuser_artifact', password='frUsVT2ukTjWNDjVMBlF')
        # get response
        response = self.client.get('/artifacts/artifact/update/' + str(artifact_1.artifact_id) + '/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_artifact')
