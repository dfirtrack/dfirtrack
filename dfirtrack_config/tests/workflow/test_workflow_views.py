from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone
from dfirtrack_config.models import Workflow
from dfirtrack_main.models import System, Systemstatus, Taskname
from dfirtrack_artifacts.models import Artifacttype
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
        self.client.login(username='testuser_workflow', password='QVe1EH1Z5MshOW2GHS4b')
        return self.client.get(uri)

    def help_create_workflow(self, workflow_name):
        test_user = User.objects.get(username='testuser_workflow')
        return Workflow.objects.create(
            workflow_name=workflow_name,
            workflow_created_by_user_id = test_user,
            workflow_modified_by_user_id = test_user,
        )

    def test_workflow_list_not_logged_in(self):
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/config/workflow/', safe='')
        # get response
        response = self.client.get('/config/workflow', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_workflow_list_logged_in(self):
        # get response
        response = self.help_client_logedin_request('/config/workflow/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_workflow_list_template(self):
        # get response
        response = self.help_client_logedin_request('/config/workflow/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_config/workflow/workflows.html')

    def test_workflow_list_get_user_context(self):
        # get response
        response = self.help_client_logedin_request('/config/workflow/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_workflow')

    def test_workflow_list_redirect(self):
        destination = urllib.parse.quote('/config/workflow/', safe='/')
        # get response
        response = self.help_client_logedin_request('/config/workflow')
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_workflow_detail_not_logged_in(self):
        # get object
        workflow_1 = Workflow.objects.get(workflow_name='workflow_1').workflow_id
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/config/workflow/{}/'.format(workflow_1), safe='')
        # get response
        response = self.client.get('/config/workflow/{}/'.format(workflow_1), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_workflow_detail_logged_in(self):
        # get object
        workflow_1 = Workflow.objects.get(workflow_name='workflow_1').workflow_id
        # get response
        response = self.help_client_logedin_request('/config/workflow/{}/'.format(workflow_1))
        # compare
        self.assertEqual(response.status_code, 200)

    def test_workflow_detail_template(self):
        # get object
        workflow_1 = Workflow.objects.get(workflow_name='workflow_1').workflow_id
        # get response
        response = self.help_client_logedin_request('/config/workflow/{}/'.format(workflow_1))
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_config/workflow/workflow_detail.html')

    def test_workflow_detail_get_user_context(self):
        # get object
        workflow_1 = Workflow.objects.get(workflow_name='workflow_1').workflow_id
        # get response
        response = self.help_client_logedin_request('/config/workflow/{}/'.format(workflow_1))
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_workflow')

    def testworkflow_detail_redirect(self):
        # get object
        workflow_1 = Workflow.objects.get(workflow_name='workflow_1').workflow_id
        # create url
        destination = urllib.parse.quote('/config/workflow/{}/'.format(workflow_1), safe='/')
        # get response
        response = self.help_client_logedin_request('/config/workflow/{}'.format(workflow_1))
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_workflow_add_not_logged_in(self):
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/config/workflow/add/', safe='')
        # get response
        response = self.client.get('/config/workflow/add', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_workflow_add_logged_in(self):
        # get response
        response = self.help_client_logedin_request('/config/workflow/add/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_workflow_add_template(self):
        # get response
        response = self.help_client_logedin_request('/config/workflow/add/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_config/workflow/workflow_generic_form.html')

    def test_workflow_add_tasknames(self):
        #get objects
        taskname = Taskname.objects.get(taskname_name='taskname_1')
        # get response
        response = self.help_client_logedin_request('/config/workflow/add/')
        # compare
        qs = response.context['form'].fields['tasknames'].queryset 
        self.assertEquals(str(qs[0]), str(taskname))

    def test_workflow_add_artifacctypes(self):
        #get objects
        artifacttypes = Artifacttype.objects.all()
        # get response
        response = self.help_client_logedin_request('/config/workflow/add/')
        # compare
        qs = response.context['artifacttypes_formset'].forms[0].fields['artifacttype'].queryset
        self.assertEquals(list(qs), list(artifacttypes))

    def test_workflow_add_get_user_context(self):
        # get response
        response = self.help_client_logedin_request('/config/workflow/add/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_workflow')

    def test_workflow_add_redirect(self):
        # create url
        destination = urllib.parse.quote('/config/workflow/add/', safe='/')
        # get response
        response = self.help_client_logedin_request('/config/workflow/add')
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_workflow_add_post_redirect(self):
        # login testuser
        self.client.login(username='testuser_workflow', password='QVe1EH1Z5MshOW2GHS4b')
        # get object
        taskname_id = Taskname.objects.get(taskname_name='taskname_1').taskname_id
        artifacttype_id = Artifacttype.objects.get(artifacttype_name='artifacttype_1').artifacttype_id
        # create post data
        data_dict = {
            'workflow_name': 'workflow_add_post_test',
            'tasknames': [taskname_id],
            'form-TOTAL_FORMS': '1',
            'form-INITIAL_FORMS': '0',
            'form-0-artifacttype': artifacttype_id,
            'form-0-artifact_default_name': 'default_name_1'
        }
        # get response
        response = self.client.post('/config/workflow/add/', data_dict)
        # get object
        workflow_id = Workflow.objects.get(workflow_name = 'workflow_add_post_test').workflow_id
        # create url
        destination = urllib.parse.quote('/config/workflow/{}/'.format(workflow_id), safe='/')
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_workflow_add_post_invalid(self):
        # login testuser
        self.client.login(username='testuser_workflow', password='QVe1EH1Z5MshOW2GHS4b')
        # create post data
        data_dict = {}
        # get response
        response = self.client.post('/config/workflow/add/', data_dict)
        # compare
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dfirtrack_config/workflow/workflow_generic_form.html')

    def test_workflow_update_not_logged_in(self):
        # get object
        workflow_1 = Workflow.objects.get(workflow_name='workflow_1').workflow_id
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/config/workflow/{}/update/'.format(workflow_1), safe='')
        # get response
        response = self.client.get('/config/workflow/{}/update/'.format(workflow_1), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_workflow_update_logged_in(self):
        # get object
        workflow_1 = Workflow.objects.get(workflow_name='workflow_1').workflow_id
        # get response
        response = self.help_client_logedin_request('/config/workflow/{}/update/'.format(workflow_1))
        # compare
        self.assertEqual(response.status_code, 200)

    def test_workflow_update_template(self):
        # get object
        workflow_1 = Workflow.objects.get(workflow_name='workflow_1').workflow_id
        # get response
        response = self.help_client_logedin_request('/config/workflow/{}/update/'.format(workflow_1))
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_config/workflow/workflow_generic_form.html')

    def test_workflow_update_get_user_context(self):
        # get object
        workflow_1 = Workflow.objects.get(workflow_name='workflow_1').workflow_id
        # get response
        response = self.help_client_logedin_request('/config/workflow/{}/update/'.format(workflow_1))
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_workflow')

    def test_workflow_update_post_redirect(self):
        # login testuser
        self.client.login(username='testuser_workflow', password='QVe1EH1Z5MshOW2GHS4b')
        # create object
        workflow_1 = self.help_create_workflow('workflow_update_post_test_1')
        # create post data
        data_dict = {
            'workflow_name': 'workflow_update_post_test_2',
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
        # login testuser
        self.client.login(username='testuser_workflow', password='QVe1EH1Z5MshOW2GHS4b')
        # get object
        taskname_id = Taskname.objects.get(taskname_name='taskname_1').taskname_id
        artifacttype_id = Artifacttype.objects.get(artifacttype_name='artifacttype_1').artifacttype_id
        workflow_1 = Workflow.objects.get(workflow_name='workflow_1').workflow_id
        # create post data
        data_dict = {
            'workflow_name': 'workflow_1',
            'tasknames': [taskname_id],
            'form-TOTAL_FORMS': '1',
            'form-INITIAL_FORMS': '0',
            'form-0-artifacttype': artifacttype_id,
            'form-0-artifact_default_name': 'default_name_1'
        }
        # get response
        response = self.client.post('/config/workflow/{}/update/'.format(workflow_1), data_dict, follow=True)
        artifacttype_workflow_id = Workflow.objects.get(workflow_name='workflow_1').artifacttypes.all()
        # get object
        self.assertContains(response, 'default_name_1')
        self.assertEqual(artifacttype_id, artifacttype_workflow_id[0].artifacttype_id)


    def test_workflow_delete_not_logged_in(self):
        # get object
        workflow_1 = Workflow.objects.get(workflow_name='workflow_1').workflow_id
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/config/workflow/{}/delete/'.format(workflow_1), safe='')
        # get response
        response = self.client.get('/config/workflow/{}/delete'.format(workflow_1), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_workflow_delete_logged_in(self):
        # get object
        workflow_1 = Workflow.objects.get(workflow_name='workflow_1').workflow_id
        # get response
        response = self.help_client_logedin_request('/config/workflow/{}/delete/'.format(workflow_1))
        # compare
        self.assertEqual(response.status_code, 200)

    def test_workflow_delete_template(self):
        # get object
        workflow_1 = Workflow.objects.get(workflow_name='workflow_1').workflow_id
        # get response
        response = self.help_client_logedin_request('/config/workflow/{}/delete/'.format(workflow_1))
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_config/workflow/workflow_delete.html')

    def test_workflow_delete_get_user_context(self):
        # get object
        workflow_1 = Workflow.objects.get(workflow_name='workflow_1').workflow_id
        # get response
        response = self.help_client_logedin_request('/config/workflow/{}/delete/'.format(workflow_1))
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_workflow')

    def test_workflow_delete_post_redirect(self):
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
        # get object
        system = System.objects.get(system_name='system_1').system_id
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/config/workflow/apply/{}/'.format(system), safe='')
        # get response
        response = self.client.post('/config/workflow/apply/{}/'.format(system), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_workflow_apply_logged_in(self):
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