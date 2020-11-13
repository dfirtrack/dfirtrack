from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import TestCase
from django.utils import timezone
#from django.utils.dateparse import parse_datetime
from dfirtrack.config import EVIDENCE_PATH
from dfirtrack_artifacts.models import Artifact, Artifactstatus, Artifacttype
from dfirtrack_main.models import System, Systemstatus
from mock import patch
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
            artifact_md5 = 'd41d8cd98f00b204e9800998ecf8427e',
            artifact_sha1 = 'da39a3ee5e6b4b0d3255bfef95601890afd80709',
            artifact_sha256 = 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855',
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
        self.client.login(username='testuser_artifact', password='frUsVT2ukTjWNDjVMBlF')
        # get response
        response = self.client.get('/artifacts/artifact/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_artifact_list_template(self):
        """ test list view """

        # login testuser
        self.client.login(username='testuser_artifact', password='frUsVT2ukTjWNDjVMBlF')
        # get response
        response = self.client.get('/artifacts/artifact/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_artifacts/artifact/artifact_list.html')

    def test_artifact_list_get_user_context(self):
        """ test list view """

        # login testuser
        self.client.login(username='testuser_artifact', password='frUsVT2ukTjWNDjVMBlF')
        # get response
        response = self.client.get('/artifacts/artifact/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_artifact')

    def test_artifact_list_redirect(self):
        """ test list view """

        # login testuser
        self.client.login(username='testuser_artifact', password='frUsVT2ukTjWNDjVMBlF')
        # create url
        destination = urllib.parse.quote('/artifacts/artifact/', safe='/')
        # get response
        response = self.client.get('/artifacts/artifact', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

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
        self.client.login(username='testuser_artifact', password='frUsVT2ukTjWNDjVMBlF')
        # get response
        response = self.client.get('/artifacts/artifact/detail/' + str(artifact_1.artifact_id) + '/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_artifact_detail_template(self):
        """ test detail view """

        # get object
        artifact_1 = Artifact.objects.get(artifact_name='artifact_1')
        # login testuser
        self.client.login(username='testuser_artifact', password='frUsVT2ukTjWNDjVMBlF')
        # get response
        response = self.client.get('/artifacts/artifact/detail/' + str(artifact_1.artifact_id) + '/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_artifacts/artifact/artifact_detail.html')

    def test_artifact_detail_get_user_context(self):
        """ test detail view """

        # get object
        artifact_1 = Artifact.objects.get(artifact_name='artifact_1')
        # login testuser
        self.client.login(username='testuser_artifact', password='frUsVT2ukTjWNDjVMBlF')
        # get response
        response = self.client.get('/artifacts/artifact/detail/' + str(artifact_1.artifact_id) + '/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_artifact')

    def test_artifact_detail_redirect(self):
        """ test detail view """

        # get object
        artifact_1 = Artifact.objects.get(artifact_name='artifact_1')
        # login testuser
        self.client.login(username='testuser_artifact', password='frUsVT2ukTjWNDjVMBlF')
        # create url
        destination = urllib.parse.quote('/artifacts/artifact/detail/' + str(artifact_1.artifact_id) + '/', safe='/')
        # get response
        response = self.client.get('/artifacts/artifact/detail/' + str(artifact_1.artifact_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

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
        self.client.login(username='testuser_artifact', password='frUsVT2ukTjWNDjVMBlF')
        # get response
        response = self.client.get('/artifacts/artifact/create/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_artifact_create_template(self):
        """ test create view """

        # login testuser
        self.client.login(username='testuser_artifact', password='frUsVT2ukTjWNDjVMBlF')
        # get response
        response = self.client.get('/artifacts/artifact/create/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_artifacts/artifact/artifact_add.html')

    def test_artifact_create_get_user_context(self):
        """ test create view """

        # login testuser
        self.client.login(username='testuser_artifact', password='frUsVT2ukTjWNDjVMBlF')
        # get response
        response = self.client.get('/artifacts/artifact/create/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_artifact')

    def test_artifact_create_redirect(self):
        """ test create view """

        # login testuser
        self.client.login(username='testuser_artifact', password='frUsVT2ukTjWNDjVMBlF')
        # create url
        destination = urllib.parse.quote('/artifacts/artifact/create/', safe='/')
        # get response
        response = self.client.get('/artifacts/artifact/create', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_artifact_create_post_redirect(self):
        """ test create view """

        # login testuser
        self.client.login(username='testuser_artifact', password='frUsVT2ukTjWNDjVMBlF')
        # get objects
        artifactstatus_id = Artifactstatus.objects.get(artifactstatus_name = 'artifactstatus_1').artifactstatus_id
        artifacttype_id = Artifacttype.objects.get(artifacttype_name = 'artifacttype_1').artifacttype_id
        system_id = System.objects.get(system_name = 'system_1').system_id
        # create post data
        data_dict = {
            'artifact_name': 'artifact_create_post_test',
            'artifactstatus': artifactstatus_id,
            'artifacttype': artifacttype_id,
            'system': system_id,
        }
        # get response
        response = self.client.post('/artifacts/artifact/create/', data_dict)
        # get artifact
        artifact_id = Artifact.objects.get(artifact_name = 'artifact_create_post_test').artifact_id
        # create url
        destination = urllib.parse.quote('/artifacts/artifact/detail/' + str(artifact_id) + '/', safe='/')
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_artifact_create_post_complete(self):
        """ test create view """

        # mock timezone.now()
        t1_now = timezone.now()
        with patch.object(timezone, 'now', return_value=t1_now):

            # TODO: fix times

            # login testuser
            self.client.login(username='testuser_artifact', password='frUsVT2ukTjWNDjVMBlF')
            # get user
            test_user = User.objects.get(username='testuser_artifact')
            # get objects
            artifactstatus_id = Artifactstatus.objects.get(artifactstatus_name = 'artifactstatus_1').artifactstatus_id
            artifacttype_id = Artifacttype.objects.get(artifacttype_name = 'artifacttype_1').artifacttype_id
            system_id = System.objects.get(system_name = 'system_1').system_id
            # create post data
            data_dict = {
                'artifactstatus': artifactstatus_id,
                'artifacttype': artifacttype_id,
                # 'case': TODO
                'system': system_id,
                #'artifact_aqcquisition_time': '2020-02-01 12:34:56',
                'artifact_md5': 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
                'artifact_name': 'Artifact Create_post_complete_test',
                'artifact_note_analysisresult': 'this is a note for analysis results - export considered',
                'artifact_note_external': 'this is a note for external usage - export considered',
                'artifact_note_internal': 'this is a note for internal usage - no export intended',
                # 'artifact_requested_time': '2020-02-02 23:45:16',
                'artifact_sha1': 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
                'artifact_sha256': 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
                'artifact_source_path': '/bin/evil',
            }
            # get response
            self.client.post('/artifacts/artifact/create/', data_dict)
            # get artifact
            artifact = Artifact.objects.get(artifact_name = 'Artifact Create_post_complete_test')
            # build expected storage path
            expected_storage_path = EVIDENCE_PATH + '/' + str(artifact.system.system_uuid) + '/' + artifact.artifacttype.artifacttype_slug + '/' + str(artifact.artifact_uuid)
            # build expected acquisition time
            #expected_acquisition_time = parse_datetime('2020-02-01T12:34:56')
            # build expected requested time
            #expected_requested_time = parse_datetime('2020-02-02T23:45:16')
            # compare
            self.assertEqual(artifact.artifactstatus.artifactstatus_name, 'artifactstatus_1')
            self.assertEqual(artifact.artifacttype.artifacttype_name, 'artifacttype_1')
            #self.assertEqual(artifact.case, '')
            self.assertEqual(artifact.system.system_name, 'system_1')
            #self.assertEqual(artifact.artifact_acquisition_time, expected_acquisition_time)
            self.assertEqual(artifact.artifact_md5, 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
            self.assertEqual(artifact.artifact_name, 'Artifact Create_post_complete_test')
            self.assertEqual(artifact.artifact_note_analysisresult, 'this is a note for analysis results - export considered')
            self.assertEqual(artifact.artifact_note_external, 'this is a note for external usage - export considered')
            self.assertEqual(artifact.artifact_note_internal, 'this is a note for internal usage - no export intended')
            #self.assertEqual(artifact.artifact_requested_time, expected_requested_time)
            self.assertEqual(artifact.artifact_sha1, 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
            self.assertEqual(artifact.artifact_sha256, 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
            self.assertEqual(artifact.artifact_slug, 'artifact-create_post_complete_test')
            self.assertEqual(artifact.artifact_source_path, '/bin/evil')
            self.assertEqual(artifact.artifact_storage_path, expected_storage_path)
            self.assertTrue(artifact.artifact_uuid)
            self.assertEqual(artifact.artifact_create_time, t1_now)
            self.assertEqual(artifact.artifact_modify_time, t1_now)
            self.assertEqual(artifact.artifact_created_by_user_id, test_user)
            self.assertEqual(artifact.artifact_modified_by_user_id, test_user)

    def test_artifact_create_post_invalid_reload(self):
        """ test create view """

        # login testuser
        self.client.login(username='testuser_artifact', password='frUsVT2ukTjWNDjVMBlF')
        # create post data
        data_dict = {}
        # get response
        response = self.client.post('/artifacts/artifact/create/', data_dict)
        # compare
        self.assertEqual(response.status_code, 200)

    def test_artifact_create_post_invalid_template(self):
        """ test create view """

        # login testuser
        self.client.login(username='testuser_artifact', password='frUsVT2ukTjWNDjVMBlF')
        # create post data
        data_dict = {}
        # get response
        response = self.client.post('/artifacts/artifact/create/', data_dict)
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_artifacts/artifact/artifact_add.html')

    def test_artifact_create_md5_message(self):
        """ test create view """

        # login testuser
        self.client.login(username='testuser_artifact', password='frUsVT2ukTjWNDjVMBlF')
        # get objects
        artifactstatus_id = Artifactstatus.objects.get(artifactstatus_name = 'artifactstatus_1').artifactstatus_id
        artifacttype_id = Artifacttype.objects.get(artifacttype_name = 'artifacttype_1').artifacttype_id
        system_id = System.objects.get(system_name = 'system_1').system_id
        # create post data
        data_dict = {
            'artifact_name': 'artifact_md5_test',
            'artifactstatus': artifactstatus_id,
            'artifacttype': artifacttype_id,
            'system': system_id,
            'artifact_md5': 'd41d8cd98f00b204e9800998ecf8427e',
        }
        # get response
        response = self.client.post('/artifacts/artifact/create/', data_dict)
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(str(messages[-1]), 'MD5 already exists for other artifact(s)')

    def test_artifact_create_sha1_message(self):
        """ test create view """

        # login testuser
        self.client.login(username='testuser_artifact', password='frUsVT2ukTjWNDjVMBlF')
        # get objects
        artifactstatus_id = Artifactstatus.objects.get(artifactstatus_name = 'artifactstatus_1').artifactstatus_id
        artifacttype_id = Artifacttype.objects.get(artifacttype_name = 'artifacttype_1').artifacttype_id
        system_id = System.objects.get(system_name = 'system_1').system_id
        # create post data
        data_dict = {
            'artifact_name': 'artifact_sha1_test',
            'artifactstatus': artifactstatus_id,
            'artifacttype': artifacttype_id,
            'system': system_id,
            'artifact_sha1': 'da39a3ee5e6b4b0d3255bfef95601890afd80709',
        }
        # get response
        response = self.client.post('/artifacts/artifact/create/', data_dict)
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(str(messages[-1]), 'SHA1 already exists for other artifact(s)')

    def test_artifact_create_sha256_message(self):
        """ test create view """

        # login testuser
        self.client.login(username='testuser_artifact', password='frUsVT2ukTjWNDjVMBlF')
        # get objects
        artifactstatus_id = Artifactstatus.objects.get(artifactstatus_name = 'artifactstatus_1').artifactstatus_id
        artifacttype_id = Artifacttype.objects.get(artifacttype_name = 'artifacttype_1').artifacttype_id
        system_id = System.objects.get(system_name = 'system_1').system_id
        # create post data
        data_dict = {
            'artifact_name': 'artifact_sha256_test',
            'artifactstatus': artifactstatus_id,
            'artifacttype': artifacttype_id,
            'system': system_id,
            'artifact_sha256': 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855',
        }
        # get response
        response = self.client.post('/artifacts/artifact/create/', data_dict)
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(str(messages[-1]), 'SHA256 already exists for other artifact(s)')

    def test_artifact_create_with_system_not_logged_in(self):
        """ test create view """

        # get object
        system_id = System.objects.get(system_name = 'system_1').system_id
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/artifacts/artifact/create/%3Fsystem%3D' + str(system_id), safe='%')
        # get response
        response = self.client.get('/artifacts/artifact/create/?system=' + str(system_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_artifact_create_with_system_logged_in(self):
        """ test create view """

        # get object
        system_id = System.objects.get(system_name = 'system_1').system_id
        # login testuser
        self.client.login(username='testuser_artifact', password='frUsVT2ukTjWNDjVMBlF')
        # get response
        response = self.client.get('/artifacts/artifact/create/?system=' + str(system_id))
        # compare
        self.assertEqual(response.status_code, 200)

    def test_artifact_create_with_system_template(self):
        """ test create view """

        # get object
        system_id = System.objects.get(system_name = 'system_1').system_id
        # login testuser
        self.client.login(username='testuser_artifact', password='frUsVT2ukTjWNDjVMBlF')
        # get response
        response = self.client.get('/artifacts/artifact/create/?system=' + str(system_id))
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_artifacts/artifact/artifact_add.html')

    def test_artifact_create_with_system_get_user_context(self):
        """ test create view """

        # get object
        system_id = System.objects.get(system_name = 'system_1').system_id
        # login testuser
        self.client.login(username='testuser_artifact', password='frUsVT2ukTjWNDjVMBlF')
        # get response
        response = self.client.get('/artifacts/artifact/create/?system=' + str(system_id))
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_artifact')

    def test_artifact_create_with_system_redirect(self):
        """ test create view """

        # get object
        system_id = System.objects.get(system_name = 'system_1').system_id
        # login testuser
        self.client.login(username='testuser_artifact', password='frUsVT2ukTjWNDjVMBlF')
        # create url
        destination = urllib.parse.quote('/artifacts/artifact/create/?system=' + str(system_id), safe='/=?')
        # get response
        response = self.client.get('/artifacts/artifact/create?system=' + str(system_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

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
        self.client.login(username='testuser_artifact', password='frUsVT2ukTjWNDjVMBlF')
        # get response
        response = self.client.get('/artifacts/artifact/update/' + str(artifact_1.artifact_id) + '/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_artifact_update_template(self):
        """ test update view """

        # get object
        artifact_1 = Artifact.objects.get(artifact_name='artifact_1')
        # login testuser
        self.client.login(username='testuser_artifact', password='frUsVT2ukTjWNDjVMBlF')
        # get response
        response = self.client.get('/artifacts/artifact/update/' + str(artifact_1.artifact_id) + '/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_artifacts/artifact/artifact_edit.html')

    def test_artifact_update_get_user_context(self):
        """ test update view """

        # get object
        artifact_1 = Artifact.objects.get(artifact_name='artifact_1')
        # login testuser
        self.client.login(username='testuser_artifact', password='frUsVT2ukTjWNDjVMBlF')
        # get response
        response = self.client.get('/artifacts/artifact/update/' + str(artifact_1.artifact_id) + '/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_artifact')

    def test_artifact_update_redirect(self):
        """ test update view """

        # get object
        artifact_1 = Artifact.objects.get(artifact_name='artifact_1')
        # login testuser
        self.client.login(username='testuser_artifact', password='frUsVT2ukTjWNDjVMBlF')
        # create url
        destination = urllib.parse.quote('/artifacts/artifact/update/' + str(artifact_1.artifact_id) + '/', safe='/')
        # get response
        response = self.client.get('/artifacts/artifact/update/' + str(artifact_1.artifact_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_artifact_update_post_redirect(self):
        """ test update view """

        # login testuser
        self.client.login(username='testuser_artifact', password='frUsVT2ukTjWNDjVMBlF')
        # get user
        test_user = User.objects.get(username='testuser_artifact')
        # get objects
        artifactstatus = Artifactstatus.objects.get(artifactstatus_name = 'artifactstatus_1')
        artifacttype = Artifacttype.objects.get(artifacttype_name = 'artifacttype_1')
        system = System.objects.get(system_name = 'system_1')
        # create object
        artifact = Artifact.objects.create(
            artifact_name = 'artifact_update_post_test_1',
            artifactstatus = artifactstatus,
            artifacttype = artifacttype,
            system = system,
            artifact_created_by_user_id = test_user,
            artifact_modified_by_user_id = test_user,
        )
        # create post data
        data_dict = {
            'artifact_name': 'artifact_update_post_test_2',
            'artifactstatus': artifactstatus.artifactstatus_id,
            'artifacttype': artifacttype.artifacttype_id,
            'system': system.system_id,
        }
        # get response
        response = self.client.post('/artifacts/artifact/update/' + str(artifact.artifact_id) + '/', data_dict)
        # create url
        destination = urllib.parse.quote('/artifacts/artifact/detail/' + str(artifact.artifact_id) + '/', safe='/')
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_artifact_update_post_invalid_reload(self):
        """ test update view """

        # login testuser
        self.client.login(username='testuser_artifact', password='frUsVT2ukTjWNDjVMBlF')
        # get object
        artifact_id = Artifact.objects.get(artifact_name='artifact_1').artifact_id
        # create post data
        data_dict = {}
        # get response
        response = self.client.post('/artifacts/artifact/update/' + str(artifact_id) + '/', data_dict)
        # compare
        self.assertEqual(response.status_code, 200)

    def test_artifact_update_post_invalid_template(self):
        """ test update view """

        # login testuser
        self.client.login(username='testuser_artifact', password='frUsVT2ukTjWNDjVMBlF')
        # get object
        artifact_id = Artifact.objects.get(artifact_name='artifact_1').artifact_id
        # create post data
        data_dict = {}
        # get response
        response = self.client.post('/artifacts/artifact/update/' + str(artifact_id) + '/', data_dict)
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_artifacts/artifact/artifact_edit.html')
