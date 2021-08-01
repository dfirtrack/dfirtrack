from datetime import datetime
from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone
from dfirtrack_artifacts.models import Artifact
from dfirtrack_artifacts.models import Artifactpriority
from dfirtrack_artifacts.models import Artifactstatus
from dfirtrack_artifacts.models import Artifacttype
from dfirtrack_main.models import Case
from dfirtrack_main.models import System
from dfirtrack_main.models import Systemstatus
from dfirtrack_main.models import Tag
from dfirtrack_main.models import Tagcolor
import urllib.parse


class ArtifactAPIViewTestCase(TestCase):
    """ artifact API view tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_artifact_api', password='rQeyaRKd7Lt6D518TTzv')

        # create object
        Case.objects.create(
            case_name = 'case_1',
            case_is_incident = True,
            case_created_by_user_id = test_user,
        )

        # create object
        systemstatus_1 = Systemstatus.objects.create(systemstatus_name='systemstatus_1')

        # create object
        system_1 = System.objects.create(
            system_name = 'system_1',
            systemstatus = systemstatus_1,
            system_created_by_user_id = test_user,
            system_modified_by_user_id = test_user,
        )

        # create object
        tagcolor_1 = Tagcolor.objects.create(tagcolor_name='tagcolor_1')
        # create object
        Tag.objects.create(
            tagcolor = tagcolor_1,
            tag_name = 'tag_1',
        )

        # create objects
        artifactpriority_1 = Artifactpriority.objects.create(artifactpriority_name='artifactpriority_1')
        artifactstatus_1 = Artifactstatus.objects.create(artifactstatus_name='artifactstatus_1')
        artifacttype_1 = Artifacttype.objects.create(artifacttype_name='artifacttype_1')

        # create object
        Artifact.objects.create(
            artifact_name='artifact_api_1',
            artifactpriority = artifactpriority_1,
            artifactstatus = artifactstatus_1,
            artifacttype = artifacttype_1,
            system = system_1,
            artifact_created_by_user_id = test_user,
            artifact_modified_by_user_id = test_user,
        )

    def test_artifact_list_api_unauthorized(self):
        """ unauthorized access is forbidden"""

        # get response
        response = self.client.get('/api/artifact/')
        # compare
        self.assertEqual(response.status_code, 401)

    def test_artifact_list_api_method_get(self):
        """ GET is allowed """

        # login testuser
        self.client.login(username='testuser_artifact_api', password='rQeyaRKd7Lt6D518TTzv')
        # get response
        response = self.client.get('/api/artifact/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_artifact_list_api_method_post(self):
        """ POST is allowed """

        # login testuser
        self.client.login(username='testuser_artifact_api', password='rQeyaRKd7Lt6D518TTzv')
        # get user
        test_user_id = User.objects.get(username='testuser_artifact_api').id
        # get objects
        artifactpriority_1 = Artifactpriority.objects.get(artifactpriority_name='artifactpriority_1')
        artifactstatus_1 = Artifactstatus.objects.get(artifactstatus_name='artifactstatus_1')
        artifacttype_1 = Artifacttype.objects.get(artifacttype_name='artifacttype_1')
        # get object
        system_1 = System.objects.get(system_name='system_1')
        # create POST string
        poststring = {
            "artifact_name": "artifact_api_2",
            "artifactpriority": artifactpriority_1.artifactpriority_id,
            "artifactstatus": artifactstatus_1.artifactstatus_id,
            "artifacttype": artifacttype_1.artifacttype_id,
            "system": system_1.system_id,
            "artifact_created_by_user_id": test_user_id,
            "artifact_modified_by_user_id": test_user_id,
        }
        # check for existence of object
        artifact_api_2_none = Artifact.objects.filter(artifact_name='artifact_api_2')
        # compare
        self.assertEqual(len(artifact_api_2_none), 0)
        # get response
        response = self.client.post('/api/artifact/', data=poststring, content_type='application/json')
        # compare
        self.assertEqual(response.status_code, 201)
        # get new object
        artifact_api_2 = Artifact.objects.get(artifact_name='artifact_api_2')
        # compare
        self.assertEqual(artifact_api_2.artifactpriority, artifactpriority_1)
        self.assertEqual(artifact_api_2.artifactstatus, artifactstatus_1)
        self.assertEqual(artifact_api_2.artifacttype, artifacttype_1)
        self.assertEqual(artifact_api_2.system, system_1)

    def test_artifact_list_api_method_post_all_id(self):
        """ POST is allowed """

        # login testuser
        self.client.login(username='testuser_artifact_api', password='rQeyaRKd7Lt6D518TTzv')
        # get user
        test_user_id = User.objects.get(username='testuser_artifact_api').id
        # get objects
        artifactpriority_1 = Artifactpriority.objects.get(artifactpriority_name='artifactpriority_1')
        artifactstatus_1 = Artifactstatus.objects.get(artifactstatus_name='artifactstatus_1')
        artifacttype_1 = Artifacttype.objects.get(artifacttype_name='artifacttype_1')
        # get objects
        case_1 = Case.objects.get(case_name='case_1')
        system_1 = System.objects.get(system_name='system_1')
        tag_1 = Tag.objects.get(tag_name='tag_1')
        # create POST string
        poststring = {
            "artifact_name": "artifact_api_3",
            "artifactpriority": artifactpriority_1.artifactpriority_id,
            "artifactstatus": artifactstatus_1.artifactstatus_id,
            "artifacttype": artifacttype_1.artifacttype_id,
            "case": case_1.case_id,
            "system": system_1.system_id,
            "tag": [
                tag_1.tag_id,
            ],
            "artifact_md5": "d41d8cd98f00b204e9800998ecf8427e",
            "artifact_sha1": "da39a3ee5e6b4b0d3255bfef95601890afd80709",
            "artifact_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
            "artifact_source_path": r"C:\Windows",
            "artifact_acquisition_time": '2021-05-09T10:25',
            "artifact_requested_time": '2021-05-09T10:15',
            "artifact_created_by_user_id": test_user_id,
            "artifact_modified_by_user_id": test_user_id,
        }
        # check for existence of object
        artifact_api_3_none = Artifact.objects.filter(artifact_name='artifact_api_3')
        # compare
        self.assertEqual(len(artifact_api_3_none), 0)
        # get response
        response = self.client.post('/api/artifact/', data=poststring, content_type='application/json')
        # compare
        self.assertEqual(response.status_code, 201)
        # get new object
        artifact_api_3 = Artifact.objects.get(artifact_name='artifact_api_3')
        # compare
        self.assertEqual(artifact_api_3.artifactpriority, artifactpriority_1)
        self.assertEqual(artifact_api_3.artifactstatus, artifactstatus_1)
        self.assertEqual(artifact_api_3.artifacttype, artifacttype_1)
        self.assertEqual(artifact_api_3.case, case_1)
        self.assertEqual(artifact_api_3.system, system_1)
        self.assertTrue(artifact_api_3.tag.filter(tag_name='tag_1').exists())
        self.assertEqual(artifact_api_3.artifact_md5, 'd41d8cd98f00b204e9800998ecf8427e')
        self.assertEqual(artifact_api_3.artifact_sha1, 'da39a3ee5e6b4b0d3255bfef95601890afd80709')
        self.assertEqual(artifact_api_3.artifact_sha256, 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855')
        self.assertEqual(artifact_api_3.artifact_requested_time, datetime(2021, 5, 9, 10, 15, tzinfo=timezone.utc))
        self.assertEqual(artifact_api_3.artifact_acquisition_time, datetime(2021, 5, 9, 10, 25, tzinfo=timezone.utc))
        self.assertEqual(artifact_api_3.artifact_source_path, r'C:\Windows')

    def test_artifact_list_api_redirect(self):
        """ test redirect with appending slash """

        # login testuser
        self.client.login(username='testuser_artifact_api', password='rQeyaRKd7Lt6D518TTzv')
        # create url
        destination = urllib.parse.quote('/api/artifact/', safe='/')
        # get response
        response = self.client.get('/api/artifact', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_artifact_detail_api_unauthorized (self):
        """ unauthorized access is forbidden"""

        # get object
        artifact_api_1 = Artifact.objects.get(artifact_name='artifact_api_1')
        # get response
        response = self.client.get('/api/artifact/' + str(artifact_api_1.artifact_id) + '/')
        # compare
        self.assertEqual(response.status_code, 401)

    def test_artifact_detail_api_method_get(self):
        """ GET is allowed """

        # get object
        artifact_api_1 = Artifact.objects.get(artifact_name='artifact_api_1')
        # login testuser
        self.client.login(username='testuser_artifact_api', password='rQeyaRKd7Lt6D518TTzv')
        # get response
        response = self.client.get('/api/artifact/' + str(artifact_api_1.artifact_id) + '/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_artifact_detail_api_method_delete(self):
        """ DELETE is forbidden """

        # get object
        artifact_api_1 = Artifact.objects.get(artifact_name='artifact_api_1')
        # login testuser
        self.client.login(username='testuser_artifact_api', password='rQeyaRKd7Lt6D518TTzv')
        # get response
        response = self.client.delete('/api/artifact/' + str(artifact_api_1.artifact_id) + '/')
        # compare
        self.assertEqual(response.status_code, 405)

    def test_artifact_detail_api_method_put(self):
        """ PUT is allowed """

        # login testuser
        self.client.login(username='testuser_artifact_api', password='rQeyaRKd7Lt6D518TTzv')
        # get user
        test_user_id = User.objects.get(username='testuser_artifact_api').id
        # get object
        artifact_api_1 = Artifact.objects.get(artifact_name='artifact_api_1')
        # create objects
        artifactpriority_2 = Artifactpriority.objects.create(artifactpriority_name='artifactpriority_2')
        artifactstatus_2 = Artifactstatus.objects.create(artifactstatus_name='artifactstatus_2')
        artifacttype_2 = Artifacttype.objects.create(artifacttype_name='artifacttype_2')
        # get object
        system_1 = System.objects.get(system_name='system_1')
        # create url
        destination = urllib.parse.quote('/api/artifact/' + str(artifact_api_1.artifact_id) + '/', safe='/')
        # create PUT string
        putstring = {
            "artifact_name": "new_artifact_api_1",
            "artifactpriority": artifactpriority_2.artifactpriority_id,
            "artifactstatus": artifactstatus_2.artifactstatus_id,
            "artifacttype": artifacttype_2.artifacttype_id,
            "system": system_1.system_id,
            "artifact_created_by_user_id": test_user_id,
            "artifact_modified_by_user_id": test_user_id,
        }
        # get response
        response = self.client.put(destination, data=putstring, content_type='application/json')
        # compare
        self.assertEqual(response.status_code, 200)
        # get new object
        new_artifact_api_1 = Artifact.objects.get(artifact_name='new_artifact_api_1')
        # compare
        self.assertEqual(new_artifact_api_1.artifactpriority, artifactpriority_2)
        self.assertEqual(new_artifact_api_1.artifactstatus, artifactstatus_2)
        self.assertEqual(new_artifact_api_1.artifacttype, artifacttype_2)
        self.assertEqual(new_artifact_api_1.system, system_1)

    def test_artifact_detail_api_method_put_all_id(self):
        """ PUT is allowed """

        # login testuser
        self.client.login(username='testuser_artifact_api', password='rQeyaRKd7Lt6D518TTzv')
        # get user
        test_user_id = User.objects.get(username='testuser_artifact_api').id
        # get object
        artifact_api_1 = Artifact.objects.get(artifact_name='artifact_api_1')
        # create objects
        artifactpriority_3 = Artifactpriority.objects.create(artifactpriority_name='artifactpriority_3')
        artifactstatus_3 = Artifactstatus.objects.create(artifactstatus_name='artifactstatus_3')
        artifacttype_3 = Artifacttype.objects.create(artifacttype_name='artifacttype_3')
        # get object
        case_1 = Case.objects.get(case_name='case_1')
        system_1 = System.objects.get(system_name='system_1')
        tag_1 = Tag.objects.get(tag_name='tag_1')
        # create url
        destination = urllib.parse.quote('/api/artifact/' + str(artifact_api_1.artifact_id) + '/', safe='/')
        # create PUT string
        putstring = {
            "artifact_name": "new_artifact_api_2",
            "artifactpriority": artifactpriority_3.artifactpriority_id,
            "artifactstatus": artifactstatus_3.artifactstatus_id,
            "artifacttype": artifacttype_3.artifacttype_id,
            "case": case_1.case_id,
            "system": system_1.system_id,
            "tag": [
                tag_1.tag_id,
            ],
            "artifact_md5": "93b885adfe0da089cdf634904fd59f71",
            "artifact_sha1": "5ba93c9db0cff93f52b521d7420e43f6eda2784f",
            "artifact_sha256": "6e340b9cffb37a989ca544e6bb780a2c78901d3fb33738768511a30617afa01d",
            "artifact_source_path": r"C:\Windows",
            "artifact_acquisition_time": '2021-05-09T10:45',
            "artifact_requested_time": '2021-05-09T10:35',
            "artifact_created_by_user_id": test_user_id,
            "artifact_modified_by_user_id": test_user_id,
        }
        # get response
        response = self.client.put(destination, data=putstring, content_type='application/json')
        # compare
        self.assertEqual(response.status_code, 200)
        # get new object
        new_artifact_api_2 = Artifact.objects.get(artifact_name='new_artifact_api_2')
        # compare
        self.assertEqual(new_artifact_api_2.artifactpriority, artifactpriority_3)
        self.assertEqual(new_artifact_api_2.artifactstatus, artifactstatus_3)
        self.assertEqual(new_artifact_api_2.artifacttype, artifacttype_3)
        self.assertEqual(new_artifact_api_2.case, case_1)
        self.assertEqual(new_artifact_api_2.system, system_1)
        self.assertTrue(new_artifact_api_2.tag.filter(tag_name='tag_1').exists())
        self.assertEqual(new_artifact_api_2.artifact_md5, '93b885adfe0da089cdf634904fd59f71')
        self.assertEqual(new_artifact_api_2.artifact_sha1, '5ba93c9db0cff93f52b521d7420e43f6eda2784f')
        self.assertEqual(new_artifact_api_2.artifact_sha256, '6e340b9cffb37a989ca544e6bb780a2c78901d3fb33738768511a30617afa01d')
        self.assertEqual(new_artifact_api_2.artifact_requested_time, datetime(2021, 5, 9, 10, 35, tzinfo=timezone.utc))
        self.assertEqual(new_artifact_api_2.artifact_acquisition_time, datetime(2021, 5, 9, 10, 45, tzinfo=timezone.utc))
        self.assertEqual(new_artifact_api_2.artifact_source_path, r'C:\Windows')

    def test_artifact_detail_api_redirect(self):
        """ test redirect with appending slash """

        # get object
        artifact_api_1 = Artifact.objects.get(artifact_name='artifact_api_1')
        # login testuser
        self.client.login(username='testuser_artifact_api', password='rQeyaRKd7Lt6D518TTzv')
        # create url
        destination = urllib.parse.quote('/api/artifact/' + str(artifact_api_1.artifact_id) + '/', safe='/')
        # get response
        response = self.client.get('/api/artifact/' + str(artifact_api_1.artifact_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)
