from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone
from dfirtrack_config.models import Workflow
from dfirtrack_main.models import System
from dfirtrack_main.models import Systemstatus
from dfirtrack_main.models import Taskname
from dfirtrack_main.models import Taskpriority
from dfirtrack_main.models import Taskstatus
from dfirtrack_artifacts.models import Artifacttype
from dfirtrack_artifacts.models import Artifactstatus
from dfirtrack_artifacts.models import Artifactpriority
import urllib.parse


class WorkflowViewTestCase(TestCase):
    """ workflow view tests """

    @classmethod
    def setUpTestData(cls):

        # create objects
        test_user = User.objects.create_user(username='testuser_workflow', password='QVe1EH1Z5MshOW2GHS4b')

        Workflow.objects.create(
            workflow_name='workflow_1',
            workflow_created_by_user_id = test_user,
            workflow_modified_by_user_id = test_user,
        )

        Taskname.objects.create(taskname_name='taskname_1')

        Artifacttype.objects.create(artifacttype_name='artifacttype_1')

        systemstatus = Systemstatus.objects.create(systemstatus_name='systemstatus_1')

        System.objects.create(
            system_name = 'system_1',
            systemstatus = systemstatus,
            system_modify_time = timezone.now(),
            system_created_by_user_id = test_user,
            system_modified_by_user_id = test_user,
        )

    def help_client_logedin_request(self, uri):
        """ helper function """

        self.client.login(username='testuser_workflow', password='QVe1EH1Z5MshOW2GHS4b')
        return self.client.get(uri)

    def help_create_workflow(self, workflow_name):
        """ helper function """

        test_user = User.objects.get(username='testuser_workflow')
        return Workflow.objects.create(
            workflow_name=workflow_name,
            workflow_created_by_user_id = test_user,
            workflow_modified_by_user_id = test_user,
        )

    def test_workflow_list_not_logged_in(self):
        """ test view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/config/workflow/', safe='')
        # get response
        response = self.client.get('/config/workflow/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_workflow_list_logged_in(self):
        """ test view """

        # get response
        response = self.help_client_logedin_request('/config/workflow/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_workflow_list_template(self):
        """ test view """

        # get response
        response = self.help_client_logedin_request('/config/workflow/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_config/workflow/workflows.html')

    def test_workflow_list_get_user_context(self):
        """ test view """

        # get response
        response = self.help_client_logedin_request('/config/workflow/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_workflow')

    def test_workflow_list_redirect(self):
        """ test view """

        # create url
        destination = urllib.parse.quote('/config/workflow/', safe='/')
        # get response
        response = self.help_client_logedin_request('/config/workflow')
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_workflow_detail_not_logged_in(self):
        """ test view """

        # get object
        workflow_1 = Workflow.objects.get(workflow_name='workflow_1').workflow_id
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/config/workflow/{}/'.format(workflow_1), safe='')
        # get response
        response = self.client.get('/config/workflow/{}/'.format(workflow_1), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_workflow_detail_logged_in(self):
        """ test view """

        # get object
        workflow_1 = Workflow.objects.get(workflow_name='workflow_1').workflow_id
        # get response
        response = self.help_client_logedin_request('/config/workflow/{}/'.format(workflow_1))
        # compare
        self.assertEqual(response.status_code, 200)

    def test_workflow_detail_template(self):
        """ test view """

        # get object
        workflow_1 = Workflow.objects.get(workflow_name='workflow_1').workflow_id
        # get response
        response = self.help_client_logedin_request('/config/workflow/{}/'.format(workflow_1))
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_config/workflow/workflow_detail.html')

    def test_workflow_detail_get_user_context(self):
        """ test view """

        # get object
        workflow_1 = Workflow.objects.get(workflow_name='workflow_1').workflow_id
        # get response
        response = self.help_client_logedin_request('/config/workflow/{}/'.format(workflow_1))
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_workflow')

    def test_workflow_detail_redirect(self):
        """ test view """

        # get object
        workflow_1 = Workflow.objects.get(workflow_name='workflow_1').workflow_id
        # create url
        destination = urllib.parse.quote('/config/workflow/{}/'.format(workflow_1), safe='/')
        # get response
        response = self.help_client_logedin_request('/config/workflow/{}'.format(workflow_1))
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_workflow_add_not_logged_in(self):
        """ test view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/config/workflow/add/', safe='')
        # get response
        response = self.client.get('/config/workflow/add/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_workflow_add_logged_in(self):
        """ test view """

        # get response
        response = self.help_client_logedin_request('/config/workflow/add/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_workflow_add_template(self):
        """ test view """

        # get response
        response = self.help_client_logedin_request('/config/workflow/add/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_config/workflow/workflow_generic_form.html')

    def test_workflow_add_tasknames(self):
        """ test view """

        # get objects
        tasknames = Taskname.objects.all()
        # get response
        response = self.help_client_logedin_request('/config/workflow/add/')
        # compare
        qs = response.context['tasknames_formset'].forms[0].fields['taskname'].queryset
        self.assertEquals(list(qs), list(tasknames))

    def test_workflow_add_artifacctypes(self):
        """ test view """

        # get objects
        artifacttypes = Artifacttype.objects.all()
        # get response
        response = self.help_client_logedin_request('/config/workflow/add/')
        # compare
        qs = response.context['artifacttypes_formset'].forms[0].fields['artifacttype'].queryset
        self.assertEquals(list(qs), list(artifacttypes))

    def test_workflow_add_get_user_context(self):
        """ test view """

        # get response
        response = self.help_client_logedin_request('/config/workflow/add/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_workflow')

    def test_workflow_add_redirect(self):
        """ test view """

        # create url
        destination = urllib.parse.quote('/config/workflow/add/', safe='/')
        # get response
        response = self.help_client_logedin_request('/config/workflow/add')
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_workflow_add_post_redirect(self):
        """ test view """

        # login testuser
        self.client.login(username='testuser_workflow', password='QVe1EH1Z5MshOW2GHS4b')
        # get object
        taskname_id = Taskname.objects.get(taskname_name='taskname_1').taskname_id
        taskstatus_id = Taskstatus.objects.get(taskstatus_name='10_pending').taskstatus_id
        taskpriority_id = Taskpriority.objects.get(taskpriority_name='10_low').taskpriority_id
        
        artifacttype_id = Artifacttype.objects.get(artifacttype_name='artifacttype_1').artifacttype_id
        artfactstatus_id = Artifactstatus.objects.get(artifactstatus_name='10_needs_analysis').artifactstatus_id
        artfactpriority_id = Artifactpriority.objects.get(artifactpriority_name='10_low').artifactpriority_id

        # create post data
        data_dict = {
            'workflow_name': 'workflow_add_post_test',
            'artifact-TOTAL_FORMS': '1',
            'artifact-INITIAL_FORMS': '0',
            'artifact-MIN_NUM_FORMS': 0,
            'artifact-MAX_NUM_FORMS': 1000,
            'artifact-0-artifacttype': artifacttype_id,
            'artifact-0-artifact_default_name': 'default_name_1',
            'artifact-0-artifact_default_priority': artfactpriority_id,
            'artifact-0-artifact_default_status': artfactstatus_id,
            'artifact-0-workflow_default_artifactname_id':'',
            'taskname-TOTAL_FORMS': '1',
            'taskname-INITIAL_FORMS': '0',
            'taskname-MIN_NUM_FORMS': 0,
            'taskname-MAX_NUM_FORMS': 1000,
            'taskname-0-taskname': taskname_id,
            'taskname-0-task_default_priority': taskpriority_id,
            'taskname-0-task_default_status': taskstatus_id,
            'taskname-0-workflow_default_taskname_id':'',
        }
        # get response
        response = self.client.post('/config/workflow/add/', data_dict, follow=True)
        # get object
        workflow_id = Workflow.objects.get(workflow_name = 'workflow_add_post_test').workflow_id
        # create url
        destination = urllib.parse.quote('/config/workflow/{}/'.format(workflow_id), safe='/')
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_workflow_add_post_invalid(self):
        """ test view """

        # login testuser
        self.client.login(username='testuser_workflow', password='QVe1EH1Z5MshOW2GHS4b')
        # create post data
        data_dict = {}
        # get response
        response = self.client.post('/config/workflow/add/', data_dict)
        # compare
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dfirtrack_config/workflow/workflow_generic_form.html')

    def test_workflow_add_post_invalid_workflow_name_only(self):
        """ test view """

        # login testuser
        self.client.login(username='testuser_workflow', password='QVe1EH1Z5MshOW2GHS4b')
        # create post data
        data_dict = {
            'workflow_name': 'workflow_add_post_name_only',
        }
        # get response
        response = self.client.post('/config/workflow/add/', data_dict)
        # compare
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dfirtrack_config/workflow/workflow_generic_form.html')

    def test_workflow_update_not_logged_in(self):
        """ test view """

        # get object
        workflow_1 = Workflow.objects.get(workflow_name='workflow_1').workflow_id
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/config/workflow/{}/update/'.format(workflow_1), safe='')
        # get response
        response = self.client.get('/config/workflow/{}/update/'.format(workflow_1), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_workflow_update_logged_in(self):
        """ test view """

        # get object
        workflow_1 = Workflow.objects.get(workflow_name='workflow_1').workflow_id
        # get response
        response = self.help_client_logedin_request('/config/workflow/{}/update/'.format(workflow_1))
        # compare
        self.assertEqual(response.status_code, 200)

    def test_workflow_update_template(self):
        """ test view """

        # get object
        workflow_1 = Workflow.objects.get(workflow_name='workflow_1').workflow_id
        # get response
        response = self.help_client_logedin_request('/config/workflow/{}/update/'.format(workflow_1))
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_config/workflow/workflow_generic_form.html')

    def test_workflow_update_get_user_context(self):
        """ test view """

        # get object
        workflow_1 = Workflow.objects.get(workflow_name='workflow_1').workflow_id
        # get response
        response = self.help_client_logedin_request('/config/workflow/{}/update/'.format(workflow_1))
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_workflow')

    def test_workflow_update_post_redirect(self):
        """ test view """

        # login testuser
        self.client.login(username='testuser_workflow', password='QVe1EH1Z5MshOW2GHS4b')
        # create object
        workflow_1 = self.help_create_workflow('workflow_update_post_test_1')
        # create post data
        data_dict = {
            'workflow_name': 'workflow_update_post_test_2',
            'artifact-TOTAL_FORMS': '1',
            'artifact-INITIAL_FORMS': '0',
            'artifact-MIN_NUM_FORMS': 0,
            'artifact-MAX_NUM_FORMS': 1000,
            'artifact-0-artifacttype': '',
            'artifact-0-artifact_default_name': '',
            'artifact-0-artifact_default_priority': '',
            'artifact-0-artifact_default_status': '',
            'artifact-0-workflow_default_artifactname_id':'',
            'taskname-TOTAL_FORMS': '1',
            'taskname-INITIAL_FORMS': '0',
            'taskname-MIN_NUM_FORMS': 0,
            'taskname-MAX_NUM_FORMS': 1000,
            'taskname-0-taskname': '',
            'taskname-0-task_default_priority': '',
            'taskname-0-task_default_status': '',
            'taskname-0-workflow_default_taskname_id':'',
        }
        # get response
        response = self.client.post('/config/workflow/{}/update/'.format(workflow_1.workflow_id), data_dict)
        # get object
        workflow_2 = Workflow.objects.get(workflow_name='workflow_update_post_test_2')
        # create url
        destination = urllib.parse.quote('/config/workflow/{}/'.format(workflow_2.workflow_id), safe='/')
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_workflow_update_post_invalid(self):
        """ test view """

        # login testuser
        self.client.login(username='testuser_workflow', password='QVe1EH1Z5MshOW2GHS4b')
        # get object
        workflow_1 = Workflow.objects.get(workflow_name='workflow_1').workflow_id
        # create post data
        data_dict = {}
        # get response
        response = self.client.post('/config/workflow/{}/update/'.format(workflow_1), data_dict)
        # compare
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dfirtrack_config/workflow/workflow_generic_form.html')

    def test_workflow_update_post(self):
        """ test view """

        # login testuser
        self.client.login(username='testuser_workflow', password='QVe1EH1Z5MshOW2GHS4b')
        # get object
        taskname_id = Taskname.objects.get(taskname_name='taskname_1').taskname_id
        taskstatus_id = Taskstatus.objects.get(taskstatus_name='10_pending').taskstatus_id
        taskpriority_id = Taskpriority.objects.get(taskpriority_name='10_low').taskpriority_id
        
        artifacttype_id = Artifacttype.objects.get(artifacttype_name='artifacttype_1').artifacttype_id
        artfactstatus_id = Artifactstatus.objects.get(artifactstatus_name='10_needs_analysis').artifactstatus_id
        artfactpriority_id = Artifactpriority.objects.get(artifactpriority_name='10_low').artifactpriority_id

        workflow_1 = Workflow.objects.get(workflow_name='workflow_1').workflow_id
        # create post data
        data_dict = {
            'workflow_name': 'workflow_1',
            'artifact-TOTAL_FORMS': '1',
            'artifact-INITIAL_FORMS': '0',
            'artifact-MIN_NUM_FORMS': 0,
            'artifact-MAX_NUM_FORMS': 1000,
            'artifact-0-artifacttype': artifacttype_id,
            'artifact-0-artifact_default_name': 'default_name_1',
            'artifact-0-artifact_default_priority': artfactpriority_id,
            'artifact-0-artifact_default_status': artfactstatus_id,
            'artifact-0-workflow_default_artifactname_id':'',
            'taskname-TOTAL_FORMS': '1',
            'taskname-INITIAL_FORMS': '0',
            'taskname-MIN_NUM_FORMS': 0,
            'taskname-MAX_NUM_FORMS': 1000,
            'taskname-0-taskname': taskname_id,
            'taskname-0-task_default_priority': taskpriority_id,
            'taskname-0-task_default_status': taskstatus_id,
            'taskname-0-workflow_default_taskname_id':'',
        }
        # get response
        response = self.client.post('/config/workflow/{}/update/'.format(workflow_1), data_dict, follow=True)
        artifacttype_workflow_id = Workflow.objects.get(workflow_name='workflow_1').artifacttypes.all()
        tasknames_workflow_id = Workflow.objects.get(workflow_name='workflow_1').tasknames.all()
        # get object
        self.assertContains(response, 'default_name_1')
        self.assertEqual(artifacttype_id, artifacttype_workflow_id[0].artifacttype_id)
        self.assertEqual(taskname_id, tasknames_workflow_id[0].taskname_id)

    def test_workflow_delete_not_logged_in(self):
        """ test view """

        # get object
        workflow_1 = Workflow.objects.get(workflow_name='workflow_1').workflow_id
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/config/workflow/{}/delete/'.format(workflow_1), safe='')
        # get response
        response = self.client.get('/config/workflow/{}/delete/'.format(workflow_1), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_workflow_delete_logged_in(self):
        """ test view """

        # get object
        workflow_1 = Workflow.objects.get(workflow_name='workflow_1').workflow_id
        # get response
        response = self.help_client_logedin_request('/config/workflow/{}/delete/'.format(workflow_1))
        # compare
        self.assertEqual(response.status_code, 200)

    def test_workflow_delete_template(self):
        """ test view """

        # get object
        workflow_1 = Workflow.objects.get(workflow_name='workflow_1').workflow_id
        # get response
        response = self.help_client_logedin_request('/config/workflow/{}/delete/'.format(workflow_1))
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_config/workflow/workflow_delete.html')

    def test_workflow_delete_get_user_context(self):
        """ test view """

        # get object
        workflow_1 = Workflow.objects.get(workflow_name='workflow_1').workflow_id
        # get response
        response = self.help_client_logedin_request('/config/workflow/{}/delete/'.format(workflow_1))
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_workflow')

    def test_workflow_delete_post_redirect(self):
        """ test view """

        # login testuser
        self.client.login(username='testuser_workflow', password='QVe1EH1Z5MshOW2GHS4b')
        # create object
        workflow_1 = self.help_create_workflow('workflow_delete_post_test_1')
        # get response
        response = self.client.post('/config/workflow/{}/delete/'.format(workflow_1.workflow_id))
        # create url
        destination = urllib.parse.quote('/config/workflow/', safe='/')
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_workflow_apply_not_logged_in(self):
        """ test view """

        # get object
        system = System.objects.get(system_name='system_1').system_id
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/config/workflow/apply/{}/'.format(system), safe='')
        # get response
        response = self.client.post('/config/workflow/apply/{}/'.format(system), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_workflow_apply_logged_in(self):
        """ test view """

        # login testuser
        self.client.login(username='testuser_workflow', password='QVe1EH1Z5MshOW2GHS4b')
        # get object
        system = System.objects.get(system_name='system_1').system_id
        # create url
        destination = '/system/{}/'.format(system)
        # get response
        response = self.client.post('/config/workflow/apply/{}/'.format(system), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_workflow_apply_workflow(self):
        """ test view """

        # login testuser
        self.client.login(username='testuser_workflow', password='QVe1EH1Z5MshOW2GHS4b')
        # get object
        system = System.objects.get(system_name='system_1').system_id
        workflow = Workflow.objects.get(workflow_name='workflow_1').workflow_id
        # create url
        destination = '/system/{}/'.format(system)
        # dara dir
        data = {
            'workflow': workflow
        }
        # get response
        response = self.client.post('/config/workflow/apply/{}/'.format(system), follow=True, data=data)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
        self.assertContains(response, 'Workflow applied')

    def test_workflow_apply_nonexistent_system(self):
        """ test view """

        # login testuser
        self.client.login(username='testuser_workflow', password='QVe1EH1Z5MshOW2GHS4b')
        # create url
        destination = '/system/'
        # get response
        response = self.client.post('/config/workflow/apply/{}/'.format(99), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
        self.assertContains(response, 'System does not exist')

    def test_workflow_apply_nonexistent_workflow(self):
        """ test view """

        # login testuser
        self.client.login(username='testuser_workflow', password='QVe1EH1Z5MshOW2GHS4b')
        # get object
        system = System.objects.get(system_name='system_1').system_id
        # create url
        destination = '/config/workflow/'
        # data dir
        data = {
            'workflow': 99
        }
        # get response
        response = self.client.post('/config/workflow/apply/{}/'.format(system), follow=True, data=data)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
        self.assertContains(response, 'Could not apply workflow')
