import urllib.parse
from unittest.mock import patch

from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone

from dfirtrack.settings import INSTALLED_APPS as installed_apps
from dfirtrack_artifacts.models import (
    Artifact,
    Artifactpriority,
    Artifactstatus,
    Artifacttype,
)
from dfirtrack_config.models import MainConfigModel
from dfirtrack_main.models import Case, Casepriority, Casestatus, System, Systemstatus


class CaseViewTestCase(TestCase):
    """case view tests"""

    @classmethod
    def setUpTestData(cls):
        # create user
        test_user = User.objects.create_user(
            username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6'
        )

        # create objects
        casepriority_1 = Casepriority.objects.create(casepriority_name='casepriority_1')
        casestatus_1 = Casestatus.objects.create(casestatus_name='casestatus_1')

        # create object
        case_1 = Case.objects.create(
            case_name='case_1',
            case_is_incident=True,
            case_created_by_user_id=test_user,
            casepriority=casepriority_1,
            casestatus=casestatus_1,
        )

        # create objects
        systemstatus_1 = Systemstatus.objects.create(systemstatus_name='systemstatus_1')
        system_1 = System.objects.create(
            system_name='system_1',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )

        # create object
        artifactpriority_1 = Artifactpriority.objects.create(
            artifactpriority_name='artifactpriority_1'
        )

        # create objects
        artifactstatus_1 = Artifactstatus.objects.create(
            artifactstatus_name='artifactstatus_1'
        )

        # create object
        artifacttype_1 = Artifacttype.objects.create(
            artifacttype_name='artifacttype_1'
        )

        # create objects
        Artifact.objects.create(
            artifact_name='artifact_system_1',
            artifactpriority=artifactpriority_1,
            artifactstatus=artifactstatus_1,
            artifacttype=artifacttype_1,
            case=case_1,
            system=system_1,
            artifact_created_by_user_id=test_user,
            artifact_modified_by_user_id=test_user,
        )

    def test_case_list_not_logged_in(self):
        """test list view"""

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/case/', safe='')
        # get response
        response = self.client.get('/case/', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_case_list_logged_in(self):
        """test list view"""

        # login testuser
        self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # get response
        response = self.client.get('/case/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_case_list_template(self):
        """test list view"""

        # login testuser
        self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # get response
        response = self.client.get('/case/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/case/case_list.html')

    def test_case_list_get_user_context(self):
        """test list view"""

        # login testuser
        self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # get response
        response = self.client.get('/case/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_case')

    def test_case_list_redirect(self):
        """test list view"""

        # login testuser
        self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # create url
        destination = urllib.parse.quote('/case/', safe='/')
        # get response
        response = self.client.get('/case', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )

    def test_case_closed_not_logged_in(self):
        """test list view"""

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/case/closed/', safe='')
        # get response
        response = self.client.get('/case/closed/', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_case_closed_logged_in(self):
        """test list view"""

        # login testuser
        self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # get response
        response = self.client.get('/case/closed/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_case_closed_template(self):
        """test list view"""

        # login testuser
        self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # get response
        response = self.client.get('/case/closed/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/case/case_closed.html')

    def test_case_closed_get_user_context(self):
        """test list view"""

        # login testuser
        self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # get response
        response = self.client.get('/case/closed/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_case')

    def test_case_closed_redirect(self):
        """test list view"""

        # login testuser
        self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # create url
        destination = urllib.parse.quote('/case/closed/', safe='/')
        # get response
        response = self.client.get('/case/closed', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )

    def test_case_all_not_logged_in(self):
        """test list view"""

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/case/all/', safe='')
        # get response
        response = self.client.get('/case/all/', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_case_all_logged_in(self):
        """test list view"""

        # login testuser
        self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # get response
        response = self.client.get('/case/all/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_case_all_template(self):
        """test list view"""

        # login testuser
        self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # get response
        response = self.client.get('/case/all/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/case/case_all.html')

    def test_case_all_get_user_context(self):
        """test list view"""

        # login testuser
        self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # get response
        response = self.client.get('/case/all/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_case')

    def test_case_all_redirect(self):
        """test list view"""

        # login testuser
        self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # create url
        destination = urllib.parse.quote('/case/all/', safe='/')
        # get response
        response = self.client.get('/case/all', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )

    def test_case_detail_not_logged_in(self):
        """test detail view"""

        # get object
        case_1 = Case.objects.get(case_name='case_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote(
            '/case/' + str(case_1.case_id) + '/', safe=''
        )
        # get response
        response = self.client.get('/case/' + str(case_1.case_id) + '/', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_case_detail_logged_in(self):
        """test detail view"""

        # get object
        case_1 = Case.objects.get(case_name='case_1')
        # login testuser
        self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # get response
        response = self.client.get('/case/' + str(case_1.case_id) + '/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_case_detail_template(self):
        """test detail view"""

        # get object
        case_1 = Case.objects.get(case_name='case_1')
        # login testuser
        self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # get response
        response = self.client.get('/case/' + str(case_1.case_id) + '/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/case/case_detail.html')

    def test_case_detail_get_user_context(self):
        """test detail view"""

        # get object
        case_1 = Case.objects.get(case_name='case_1')
        # login testuser
        self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # get response
        response = self.client.get('/case/' + str(case_1.case_id) + '/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_case')

    def test_case_detail_redirect(self):
        """test detail view"""

        # get object
        case_1 = Case.objects.get(case_name='case_1')
        # login testuser
        self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # create url
        destination = urllib.parse.quote('/case/' + str(case_1.case_id) + '/', safe='/')
        # get response
        response = self.client.get('/case/' + str(case_1.case_id), follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )

    def test_case_detail_context_with_artifacts(self):
        """test detail view"""

        # add app to dfirtrack.settings
        if 'dfirtrack_artifacts' not in installed_apps:
            installed_apps.append('dfirtrack_artifacts')
        # get object
        case_1 = Case.objects.get(case_name='case_1')
        # login testuser
        self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # get response
        response = self.client.get('/case/' + str(case_1.case_id) + '/')
        # compare
        self.assertTrue(response.context['dfirtrack_artifacts'])

    def test_case_detail_context_without_artifacts(self):
        """test detail view"""

        # remove app from dfirtrack.settings
        if 'dfirtrack_artifacts' in installed_apps:
            installed_apps.remove('dfirtrack_artifacts')
        # get object
        case_1 = Case.objects.get(case_name='case_1')
        # login testuser
        self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # get response
        response = self.client.get('/case/' + str(case_1.case_id) + '/')
        # compare
        self.assertFalse(response.context['dfirtrack_artifacts'])

    def test_case_detail_context_artifact_number(self):
        """test detail view"""

        # add app to dfirtrack.settings
        if 'dfirtrack_artifacts' not in installed_apps:
            installed_apps.append('dfirtrack_artifacts')
        # get object
        case_1 = Case.objects.get(case_name='case_1')
        # login testuser
        self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # get response
        response = self.client.get('/case/' + str(case_1.case_id) + '/')
        # compare
        self.assertEqual(response.context['artifact_number'], 1)

    def test_case_add_not_logged_in(self):
        """test add view"""

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/case/add/', safe='')
        # get response
        response = self.client.get('/case/add/', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_case_add_logged_in(self):
        """test add view"""

        # login testuser
        self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # get response
        response = self.client.get('/case/add/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_case_add_template(self):
        """test add view"""

        # login testuser
        self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # get response
        response = self.client.get('/case/add/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/case/case_generic_form.html')

    def test_case_add_get_user_context(self):
        """test add view"""

        # login testuser
        self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # get response
        response = self.client.get('/case/add/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_case')

    def test_case_add_redirect(self):
        """test add view"""

        # login testuser
        self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # create url
        destination = urllib.parse.quote('/case/add/', safe='/')
        # get response
        response = self.client.get('/case/add', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )

    def test_case_add_post_redirect(self):
        """test add view"""

        # get objects
        casepriority_1 = Casepriority.objects.get(
            casepriority_name='casepriority_1'
        ).casepriority_id
        casestatus_1 = Casestatus.objects.get(
            casestatus_name='casestatus_1'
        ).casestatus_id

        # login testuser
        self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # create post data
        data_dict = {
            'case_name': 'case_add_post_test',
            'case_is_incident': 'on',
            'casepriority': casepriority_1,
            'casestatus': casestatus_1,
        }
        # get response
        response = self.client.post('/case/add/', data_dict)
        # get object
        case_id = Case.objects.get(case_name='case_add_post_test').case_id
        # create url
        destination = urllib.parse.quote('/case/' + str(case_id) + '/', safe='/')
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_case_add_post_invalid_reload(self):
        """test add view"""

        # login testuser
        self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # create post data
        data_dict = {}
        # get response
        response = self.client.post('/case/add/', data_dict)
        # compare
        self.assertEqual(response.status_code, 200)

    def test_case_add_post_invalid_template(self):
        """test add view"""

        # login testuser
        self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # create post data
        data_dict = {}
        # get response
        response = self.client.post('/case/add/', data_dict)
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/case/case_generic_form.html')

    def test_case_edit_not_logged_in(self):
        """test edit view"""

        # get object
        case_1 = Case.objects.get(case_name='case_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote(
            '/case/' + str(case_1.case_id) + '/edit/', safe=''
        )
        # get response
        response = self.client.get(
            '/case/' + str(case_1.case_id) + '/edit/', follow=True
        )
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_case_edit_logged_in(self):
        """test edit view"""

        # get object
        case_1 = Case.objects.get(case_name='case_1')
        # login testuser
        self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # get response
        response = self.client.get('/case/' + str(case_1.case_id) + '/edit/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_case_edit_template(self):
        """test edit view"""

        # get object
        case_1 = Case.objects.get(case_name='case_1')
        # login testuser
        self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # get response
        response = self.client.get('/case/' + str(case_1.case_id) + '/edit/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/case/case_generic_form.html')

    def test_case_edit_get_user_context(self):
        """test edit view"""

        # get object
        case_1 = Case.objects.get(case_name='case_1')
        # login testuser
        self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # get response
        response = self.client.get('/case/' + str(case_1.case_id) + '/edit/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_case')

    def test_case_edit_redirect(self):
        """test edit view"""

        # get object
        case_1 = Case.objects.get(case_name='case_1')
        # login testuser
        self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # create url
        destination = urllib.parse.quote(
            '/case/' + str(case_1.case_id) + '/edit/', safe='/'
        )
        # get response
        response = self.client.get(
            '/case/' + str(case_1.case_id) + '/edit', follow=True
        )
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )

    def test_case_edit_post_redirect(self):
        """test edit view"""

        # get objects
        casepriority_1 = Casepriority.objects.get(
            casepriority_name='casepriority_1'
        ).casepriority_id
        casestatus_1 = Casestatus.objects.get(
            casestatus_name='casestatus_1'
        ).casestatus_id

        # login testuser
        self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # get user
        test_user = User.objects.get(username='testuser_case')
        # create object
        case_1 = Case.objects.create(
            case_name='case_edit_post_test_1',
            case_is_incident=True,
            case_created_by_user_id=test_user,
        )
        # create post data
        data_dict = {
            'case_name': 'case_edit_post_test_2',
            'case_is_incident': 'on',
            'casepriority': casepriority_1,
            'casestatus': casestatus_1,
        }
        # get response
        response = self.client.post(
            '/case/' + str(case_1.case_id) + '/edit/', data_dict
        )
        # get object
        case_2 = Case.objects.get(case_name='case_edit_post_test_2')
        # create url
        destination = urllib.parse.quote('/case/' + str(case_2.case_id) + '/', safe='/')
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_case_edit_post_invalid_reload(self):
        """test edit view"""

        # login testuser
        self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # get object
        case_id = Case.objects.get(case_name='case_1').case_id
        # create post data
        data_dict = {}
        # get response
        response = self.client.post('/case/' + str(case_id) + '/edit/', data_dict)
        # compare
        self.assertEqual(response.status_code, 200)

    def test_case_edit_post_invalid_template(self):
        """test edit view"""

        # login testuser
        self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # get object
        case_id = Case.objects.get(case_name='case_1').case_id
        # create post data
        data_dict = {}
        # get response
        response = self.client.post('/case/' + str(case_id) + '/edit/', data_dict)
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/case/case_generic_form.html')

    def test_case_add_post_set_start_time(self):
        """creation of case with proper casestatus should set case_start_time"""

        # get object
        casestatus_1 = Casestatus.objects.get(casestatus_name='casestatus_1')
        # get config
        main_config_model = MainConfigModel.objects.get(main_config_name='MainConfig')
        # clean config
        main_config_model.casestatus_start.clear()
        main_config_model.casestatus_end.clear()
        # set config
        main_config_model.casestatus_start.add(casestatus_1)
        # login testuser
        self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # get objects
        casepriority_id = Casepriority.objects.get(
            casepriority_name='casepriority_1'
        ).casepriority_id
        casestatus_id = Casestatus.objects.get(
            casestatus_name='casestatus_1'
        ).casestatus_id
        # create post data
        data_dict = {
            'case_name': 'case_add_post_set_start_time',
            'casepriority': casepriority_id,
            'casestatus': casestatus_id,
        }

        # mock timezone.now()
        t2_now = timezone.now()
        with patch.object(timezone, 'now', return_value=t2_now):
            # get response
            self.client.post('/case/add/', data_dict)

        # get object
        case_add_post_set_start_time = Case.objects.get(
            case_name='case_add_post_set_start_time'
        )
        # compare
        self.assertEqual(case_add_post_set_start_time.case_start_time, t2_now)
        self.assertEqual(case_add_post_set_start_time.case_end_time, None)

    def test_case_add_post_set_end_time(self):
        """creation of case with proper casestatus should set case_start_time and case_end_time"""

        # get object
        casestatus_1 = Casestatus.objects.get(casestatus_name='casestatus_1')
        # get config
        main_config_model = MainConfigModel.objects.get(main_config_name='MainConfig')
        # clean config
        main_config_model.casestatus_start.clear()
        main_config_model.casestatus_end.clear()
        # set config
        main_config_model.casestatus_end.add(casestatus_1)
        # login testuser
        self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # get objects
        casepriority_id = Casepriority.objects.get(
            casepriority_name='casepriority_1'
        ).casepriority_id
        casestatus_id = Casestatus.objects.get(
            casestatus_name='casestatus_1'
        ).casestatus_id
        # create post data
        data_dict = {
            'case_name': 'case_add_post_set_end_time',
            'casepriority': casepriority_id,
            'casestatus': casestatus_id,
        }

        # mock timezone.now()
        t3_now = timezone.now()
        with patch.object(timezone, 'now', return_value=t3_now):
            # get response
            self.client.post('/case/add/', data_dict)

        # get object
        case_add_post_set_end_time = Case.objects.get(
            case_name='case_add_post_set_end_time'
        )
        # compare
        self.assertEqual(case_add_post_set_end_time.case_start_time, t3_now)
        self.assertEqual(case_add_post_set_end_time.case_end_time, t3_now)

    def test_case_edit_post_set_start_time(self):
        """update of case with proper casestatus should set case_start_time if not set before"""

        # get object
        casestatus_1 = Casestatus.objects.get(casestatus_name='casestatus_1')
        # get config
        main_config_model = MainConfigModel.objects.get(main_config_name='MainConfig')
        # clean config
        main_config_model.casestatus_start.clear()
        main_config_model.casestatus_end.clear()
        # set config
        main_config_model.casestatus_start.add(casestatus_1)
        # login testuser
        self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # get user
        test_user = User.objects.get(username='testuser_case')
        # get objects
        casepriority = Casepriority.objects.get(casepriority_name='casepriority_1')
        casestatus = Casestatus.objects.get(casestatus_name='casestatus_1')
        # create object
        case_edit_post_set_start_time = Case.objects.create(
            case_name='case_edit_post_set_start_time',
            casepriority=casepriority,
            casestatus=casestatus,
            case_is_incident=True,
            case_created_by_user_id=test_user,
            case_modified_by_user_id=test_user,
        )
        # compare (before POST, should be 'None' because model does not have 'auto_now' or 'auto_now_add', setting time is done via view, therefore redundantly using 'casestatus_1' is sufficient)
        self.assertEqual(case_edit_post_set_start_time.case_start_time, None)
        self.assertEqual(case_edit_post_set_start_time.case_end_time, None)
        # get objects
        casepriority_id = Casepriority.objects.get(
            casepriority_name='casepriority_1'
        ).casepriority_id
        casestatus_id = Casestatus.objects.get(
            casestatus_name='casestatus_1'
        ).casestatus_id
        # update post data
        data_dict = {
            'case_name': 'case_edit_post_set_start_time',
            'casepriority': casepriority_id,
            'casestatus': casestatus_id,
        }

        # mock timezone.now()
        t4_now = timezone.now()
        with patch.object(timezone, 'now', return_value=t4_now):
            # get response
            self.client.post(
                '/case/' + str(case_edit_post_set_start_time.case_id) + '/edit/',
                data_dict,
            )

        # refresh object
        case_edit_post_set_start_time.refresh_from_db()
        # compare
        self.assertEqual(case_edit_post_set_start_time.case_start_time, t4_now)
        self.assertEqual(case_edit_post_set_start_time.case_end_time, None)

    def test_case_edit_post_set_end_time(self):
        """update of case with proper casestatus should set case_start_time and case_end_time if not set before"""

        # get object
        casestatus_1 = Casestatus.objects.get(casestatus_name='casestatus_1')
        # get config
        main_config_model = MainConfigModel.objects.get(main_config_name='MainConfig')
        # clean config
        main_config_model.casestatus_start.clear()
        main_config_model.casestatus_end.clear()
        # set config
        main_config_model.casestatus_end.add(casestatus_1)
        # login testuser
        self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # get user
        test_user = User.objects.get(username='testuser_case')
        # get objects
        casepriority = Casepriority.objects.get(casepriority_name='casepriority_1')
        casestatus = Casestatus.objects.get(casestatus_name='casestatus_1')
        # create object
        case_edit_post_set_end_time = Case.objects.create(
            case_name='case_edit_post_set_end_time',
            casepriority=casepriority,
            casestatus=casestatus,
            case_is_incident=True,
            case_created_by_user_id=test_user,
            case_modified_by_user_id=test_user,
        )
        # compare (before POST, should be 'None' because model does not have 'auto_now' or 'auto_now_add', setting time is done via view, therefore redundantly using 'casestatus_1' is sufficient)
        self.assertEqual(case_edit_post_set_end_time.case_start_time, None)
        self.assertEqual(case_edit_post_set_end_time.case_end_time, None)
        # get objects
        casepriority_id = Casepriority.objects.get(
            casepriority_name='casepriority_1'
        ).casepriority_id
        casestatus_id = Casestatus.objects.get(
            casestatus_name='casestatus_1'
        ).casestatus_id
        # create post data
        data_dict = {
            'case_name': 'case_edit_post_set_end_time',
            'casepriority': casepriority_id,
            'casestatus': casestatus_id,
        }

        # mock timezone.now()
        t5_now = timezone.now()
        with patch.object(timezone, 'now', return_value=t5_now):
            # get response
            self.client.post(
                '/case/' + str(case_edit_post_set_end_time.case_id) + '/edit/',
                data_dict,
            )

        # refresh object
        case_edit_post_set_end_time.refresh_from_db()
        # compare
        self.assertEqual(case_edit_post_set_end_time.case_start_time, t5_now)
        self.assertEqual(case_edit_post_set_end_time.case_end_time, t5_now)

    def test_case_edit_post_retain_start_time(self):
        """update of case with proper casestatus should not set case_start_time if set before"""

        # get object
        casestatus_1 = Casestatus.objects.get(casestatus_name='casestatus_1')
        # get config
        main_config_model = MainConfigModel.objects.get(main_config_name='MainConfig')
        # clean config
        main_config_model.casestatus_start.clear()
        main_config_model.casestatus_end.clear()
        # set config
        main_config_model.casestatus_start.add(casestatus_1)
        # login testuser
        self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # get objects
        casepriority_id = Casepriority.objects.get(
            casepriority_name='casepriority_1'
        ).casepriority_id
        casestatus_id = Casestatus.objects.get(
            casestatus_name='casestatus_1'
        ).casestatus_id
        # create post data
        data_dict = {
            'case_name': 'case_edit_post_retain_start_time',
            'casepriority': casepriority_id,
            'casestatus': casestatus_id,
        }

        # mock timezone.now()
        t6_now = timezone.now()
        with patch.object(timezone, 'now', return_value=t6_now):
            # get response
            self.client.post('/case/add/', data_dict)

        # get object
        case_edit_post_retain_start_time = Case.objects.get(
            case_name='case_edit_post_retain_start_time'
        )
        # compare (after create)
        self.assertEqual(case_edit_post_retain_start_time.case_start_time, t6_now)
        self.assertEqual(case_edit_post_retain_start_time.case_end_time, None)

        # create object
        casestatus_2 = Casestatus.objects.create(casestatus_name='casestatus_2')
        # get config
        main_config_model = MainConfigModel.objects.get(main_config_name='MainConfig')
        # clean config
        main_config_model.casestatus_start.clear()
        main_config_model.casestatus_end.clear()
        # set config
        main_config_model.casestatus_start.add(casestatus_2)
        # create post data
        data_dict = {
            'case_name': 'case_edit_post_retain_start_time',
            'casepriority': casepriority_id,
            'casestatus': casestatus_2.casestatus_id,
        }

        # mock timezone.now()
        t7_now = timezone.now()
        with patch.object(timezone, 'now', return_value=t7_now):
            # get response
            self.client.post(
                '/case/' + str(case_edit_post_retain_start_time.case_id) + '/edit/',
                data_dict,
            )

        # refresh object
        case_edit_post_retain_start_time.refresh_from_db()
        # compare (after update)
        self.assertEqual(case_edit_post_retain_start_time.case_start_time, t6_now)
        self.assertEqual(case_edit_post_retain_start_time.case_end_time, None)

    def test_case_edit_post_retain_end_time(self):
        """update of case with proper casestatus should not set case_start_time and case_end_time if set before"""

        # get object
        casestatus_1 = Casestatus.objects.get(casestatus_name='casestatus_1')
        # get config
        main_config_model = MainConfigModel.objects.get(main_config_name='MainConfig')
        # clean config
        main_config_model.casestatus_start.clear()
        main_config_model.casestatus_end.clear()
        # set config
        main_config_model.casestatus_end.add(casestatus_1)
        # login testuser
        self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # get objects
        casepriority_id = Casepriority.objects.get(
            casepriority_name='casepriority_1'
        ).casepriority_id
        casestatus_id = Casestatus.objects.get(
            casestatus_name='casestatus_1'
        ).casestatus_id
        # create post data
        data_dict = {
            'case_name': 'case_edit_post_retain_end_time',
            'casepriority': casepriority_id,
            'casestatus': casestatus_id,
        }

        # mock timezone.now()
        t8_now = timezone.now()
        with patch.object(timezone, 'now', return_value=t8_now):
            # get response
            self.client.post('/case/add/', data_dict)

        # get object
        case_edit_post_retain_end_time = Case.objects.get(
            case_name='case_edit_post_retain_end_time'
        )
        # compare (after create)
        self.assertEqual(case_edit_post_retain_end_time.case_start_time, t8_now)
        self.assertEqual(case_edit_post_retain_end_time.case_end_time, t8_now)

        # create object
        casestatus_2 = Casestatus.objects.create(casestatus_name='casestatus_2')
        # get config
        main_config_model = MainConfigModel.objects.get(main_config_name='MainConfig')
        # clean config
        main_config_model.casestatus_start.clear()
        main_config_model.casestatus_end.clear()
        # set config
        main_config_model.casestatus_end.add(casestatus_2)
        # create post data
        data_dict = {
            'case_name': 'case_edit_post_retain_end_time',
            'casepriority': casepriority_id,
            'casestatus': casestatus_2.casestatus_id,
        }

        # mock timezone.now()
        t9_now = timezone.now()
        with patch.object(timezone, 'now', return_value=t9_now):
            # get response
            self.client.post(
                '/case/' + str(case_edit_post_retain_end_time.case_id) + '/edit/',
                data_dict,
            )

        # refresh object
        case_edit_post_retain_end_time.refresh_from_db()
        # compare (after update)
        self.assertEqual(case_edit_post_retain_end_time.case_start_time, t8_now)
        self.assertEqual(case_edit_post_retain_end_time.case_end_time, t8_now)

    def test_case_set_user_redirect(self):
        """test case set_user view"""

        # login testuser
        self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # get object
        case_1 = Case.objects.get(case_name='case_1')
        # create url
        destination = urllib.parse.quote('/case/' + str(case_1.case_id) + '/', safe='/')
        # get response
        response = self.client.get(
            '/case/' + str(case_1.case_id) + '/set_user/', follow=True
        )
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_case_set_user_user(self):
        """test case set_user view"""

        # login testuser
        self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # get user
        test_user = User.objects.get(username='testuser_case')
        # get object
        casepriority_1 = Casepriority.objects.get(casepriority_name='casepriority_1')
        # get object
        casestatus_1 = Casestatus.objects.get(casestatus_name='casestatus_1')
        # create object
        case_set_user = Case.objects.create(
            case_name='case_unassigned',
            case_is_incident=True,
            casepriority=casepriority_1,
            casestatus=casestatus_1,
            case_created_by_user_id=test_user,
            case_modified_by_user_id=test_user,
        )
        # compare
        self.assertEqual(None, case_set_user.case_assigned_to_user_id)
        # get response
        self.client.get('/case/' + str(case_set_user.case_id) + '/set_user/')
        # refresh object
        case_set_user.refresh_from_db()
        # compare
        self.assertEqual(test_user, case_set_user.case_assigned_to_user_id)

    def test_case_unset_user_redirect(self):
        """test case unset_user view"""

        # login testuser
        self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # get object
        case_1 = Case.objects.get(case_name='case_1')
        # create url
        destination = urllib.parse.quote('/case/' + str(case_1.case_id) + '/', safe='/')
        # get response
        response = self.client.get(
            '/case/' + str(case_1.case_id) + '/unset_user/', follow=True
        )
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_case_unset_user_user(self):
        """test case unset_user view"""

        # login testuser
        self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # get user
        test_user = User.objects.get(username='testuser_case')
        # get object
        casepriority_1 = Casepriority.objects.get(casepriority_name='casepriority_1')
        # get object
        casestatus_1 = Casestatus.objects.get(casestatus_name='casestatus_1')
        # create object
        case_unset_user = Case.objects.create(
            case_name='case_assigned',
            case_is_incident=True,
            casepriority=casepriority_1,
            casestatus=casestatus_1,
            case_created_by_user_id=test_user,
            case_modified_by_user_id=test_user,
            case_assigned_to_user_id=test_user,
        )
        # compare
        self.assertEqual(test_user, case_unset_user.case_assigned_to_user_id)
        # get response
        self.client.get('/case/' + str(case_unset_user.case_id) + '/unset_user/')
        # refresh object
        case_unset_user.refresh_from_db()
        # compare
        self.assertEqual(None, case_unset_user.case_assigned_to_user_id)

    def test_case_detail_artifact_filter_json_provider(self):
        """test artifact filter for case detail view in dfirtrack_main/views/json_provider_views.py"""

        # login testuser
        self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # get object
        case_1 = Case.objects.get(case_name='case_1')
        # get response
        response = self.client.post(f'/filter/artifact/?case={case_1.case_id}',
            {
                'order[0][column]': '1',
                'order[0][dir]': 'asc',
                'start': '0',
                'length': '25',
                'search[value]': '',
                'columns[1][data]': 'artifact_name',
                'draw': '1',
            },
        )
        # compare
        self.assertContains(response, 'artifact_system_1')
