from django.contrib.auth.models import User
from django.test import TestCase
from dfirtrack_main.models import Case
from dfirtrack_main.models import Casepriority
from dfirtrack_main.models import Casestatus
from dfirtrack_main.models import Headline
from dfirtrack_main.models import Notestatus
from dfirtrack_main.models import Reportitem
from dfirtrack_main.models import System
from dfirtrack_main.models import Systemstatus
from dfirtrack_main.models import Tag
from dfirtrack_main.models import Tagcolor
import urllib.parse


class ReportitemViewTestCase(TestCase):
    """ reportitem view tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')

        # create objects
        headline_1 = Headline.objects.create(headline_name='headline_1')
        Notestatus.objects.create(notestatus_name='notestatus_1')
        systemstatus_1 = Systemstatus.objects.create(systemstatus_name='systemstatus_1')

        # create object
        system_1 = System.objects.create(
            system_name='system_1',
            systemstatus = systemstatus_1,
            system_created_by_user_id = test_user,
            system_modified_by_user_id = test_user,
        )

        # create object
        Reportitem.objects.create(
            reportitem_note='lorem ipsum',
            system = system_1,
            headline = headline_1,
            reportitem_created_by_user_id = test_user,
            reportitem_modified_by_user_id = test_user,
        )

        # create object
        tagcolor_1 = Tagcolor.objects.create(tagcolor_name='tagcolor_1')
        # create object
        Tag.objects.create(tag_name='tag_1', tagcolor = tagcolor_1)

        # create objects
        casepriority_1 = Casepriority.objects.create(casepriority_name='casepriority_1')
        casestatus_1 = Casestatus.objects.create(casestatus_name='casestatus_1')

        # create object
        Case.objects.create(
            case_name='case_1',
            case_is_incident=True,
            case_created_by_user_id=test_user,
            casepriority = casepriority_1,
            casestatus = casestatus_1,
        )

    def test_reportitem_list_not_logged_in(self):
        """ test list view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/reportitem/', safe='')
        # get response
        response = self.client.get('/reportitem/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_reportitem_list_logged_in(self):
        """ test list view """

        # login testuser
        self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # get response
        response = self.client.get('/reportitem/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_reportitem_list_template(self):
        """ test list view """

        # login testuser
        self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # get response
        response = self.client.get('/reportitem/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/reportitem/reportitem_list.html')

    def test_reportitem_list_get_user_context(self):
        """ test list view """

        # login testuser
        self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # get response
        response = self.client.get('/reportitem/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_reportitem')

    def test_reportitem_list_redirect(self):
        """ test list view """

        # login testuser
        self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # create url
        destination = urllib.parse.quote('/reportitem/', safe='/')
        # get response
        response = self.client.get('/reportitem', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_reportitem_detail_not_logged_in(self):
        """ test detail view """

        # get object
        reportitem_1 = Reportitem.objects.get(reportitem_note='lorem ipsum')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/reportitem/' + str(reportitem_1.reportitem_id) + '/', safe='')
        # get response
        response = self.client.get('/reportitem/' + str(reportitem_1.reportitem_id) + '/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_reportitem_detail_logged_in(self):
        """ test detail view """

        # get object
        reportitem_1 = Reportitem.objects.get(reportitem_note='lorem ipsum')
        # login testuser
        self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # get response
        response = self.client.get('/reportitem/' + str(reportitem_1.reportitem_id) + '/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_reportitem_detail_template(self):
        """ test detail view """

        # get object
        reportitem_1 = Reportitem.objects.get(reportitem_note='lorem ipsum')
        # login testuser
        self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # get response
        response = self.client.get('/reportitem/' + str(reportitem_1.reportitem_id) + '/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/reportitem/reportitem_detail.html')

    def test_reportitem_detail_get_user_context(self):
        """ test detail view """

        # get object
        reportitem_1 = Reportitem.objects.get(reportitem_note='lorem ipsum')
        # login testuser
        self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # get response
        response = self.client.get('/reportitem/' + str(reportitem_1.reportitem_id) + '/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_reportitem')

    def test_reportitem_detail_redirect(self):
        """ test detail view """

        # get object
        reportitem_1 = Reportitem.objects.get(reportitem_note='lorem ipsum')
        # login testuser
        self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # create url
        destination = urllib.parse.quote('/reportitem/' + str(reportitem_1.reportitem_id) + '/', safe='/')
        # get response
        response = self.client.get('/reportitem/' + str(reportitem_1.reportitem_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_reportitem_add_not_logged_in(self):
        """ test add view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/reportitem/add/', safe='')
        # get response
        response = self.client.get('/reportitem/add/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_reportitem_add_logged_in(self):
        """ test add view """

        # login testuser
        self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # get response
        response = self.client.get('/reportitem/add/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_reportitem_add_system_selected(self):
        """ test add view """

        # login testuser
        self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # get object
        system_id = System.objects.get(system_name = 'system_1').system_id
        # get response
        response = self.client.get('/reportitem/add/?system=' + str(system_id))
        # compare
        self.assertEqual(response.status_code, 200)

    def test_reportitem_add_template(self):
        """ test add view """

        # login testuser
        self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # get response
        response = self.client.get('/reportitem/add/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/reportitem/reportitem_generic_form.html')

    def test_reportitem_add_get_user_context(self):
        """ test add view """

        # login testuser
        self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # get response
        response = self.client.get('/reportitem/add/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_reportitem')

    def test_reportitem_add_redirect(self):
        """ test add view """

        # login testuser
        self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # create url
        destination = urllib.parse.quote('/reportitem/add/', safe='/')
        # get response
        response = self.client.get('/reportitem/add', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_reportitem_add_post_redirect(self):
        """ test add view """

        # login testuser
        self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # get objects
        headline_id = Headline.objects.get(headline_name = 'headline_1').headline_id
        notestatus_id = Notestatus.objects.get(notestatus_name = 'notestatus_1').notestatus_id
        system_id = System.objects.get(system_name = 'system_1').system_id
        tag_id = Tag.objects.get(tag_name = 'tag_1').tag_id
        # create post data
        data_dict = {
            'reportitem_note': 'reportitem_add_post_test',
            'headline': headline_id,
            'notestatus': notestatus_id,
            'system': system_id,
            'tag': [tag_id, ],
        }
        # get response
        response = self.client.post('/reportitem/add/', data_dict)
        # create url
        destination = urllib.parse.quote('/system/' + str(system_id) + '/', safe='/')
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_reportitem_add_post_redirect_documentation(self):
        """ test add view """

        # login testuser
        self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # get objects
        headline_id = Headline.objects.get(headline_name = 'headline_1').headline_id
        notestatus_id = Notestatus.objects.get(notestatus_name = 'notestatus_1').notestatus_id
        system_id = System.objects.get(system_name = 'system_1').system_id
        tag_id = Tag.objects.get(tag_name = 'tag_1').tag_id
        # create post data
        data_dict = {
            'reportitem_note': 'reportitem_add_post_test_documentation',
            'headline': headline_id,
            'notestatus': notestatus_id,
            'system': system_id,
            'tag': [tag_id, ],
        }
        # get response
        response = self.client.post('/reportitem/add/?documentation', data_dict)
        # get object
        reportitem_id = Reportitem.objects.get(reportitem_note='reportitem_add_post_test_documentation').reportitem_id
        # create url
        destination = urllib.parse.quote(f'/documentation/#reportitem_id_{str(reportitem_id)}', safe='#/')
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_reportitem_add_post_invalid_reload(self):
        """ test add view """

        # login testuser
        self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # create post data
        data_dict = {}
        # get response
        response = self.client.post('/reportitem/add/', data_dict)
        # compare
        self.assertEqual(response.status_code, 200)

    def test_reportitem_add_post_invalid_template(self):
        """ test add view """

        # login testuser
        self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # create post data
        data_dict = {}
        # get response
        response = self.client.post('/reportitem/add/', data_dict)
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/reportitem/reportitem_generic_form.html')

    def test_reportitem_edit_not_logged_in(self):
        """ test edit view """

        # get object
        reportitem_1 = Reportitem.objects.get(reportitem_note='lorem ipsum')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/reportitem/' + str(reportitem_1.reportitem_id) + '/edit/', safe='')
        # get response
        response = self.client.get('/reportitem/' + str(reportitem_1.reportitem_id) + '/edit/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_reportitem_edit_logged_in(self):
        """ test edit view """

        # get object
        reportitem_1 = Reportitem.objects.get(reportitem_note='lorem ipsum')
        # login testuser
        self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # get response
        response = self.client.get('/reportitem/' + str(reportitem_1.reportitem_id) + '/edit/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_reportitem_edit_template(self):
        """ test edit view """

        # get object
        reportitem_1 = Reportitem.objects.get(reportitem_note='lorem ipsum')
        # login testuser
        self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # get response
        response = self.client.get('/reportitem/' + str(reportitem_1.reportitem_id) + '/edit/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/reportitem/reportitem_generic_form.html')

    def test_reportitem_edit_get_user_context(self):
        """ test edit view """

        # get object
        reportitem_1 = Reportitem.objects.get(reportitem_note='lorem ipsum')
        # login testuser
        self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # get response
        response = self.client.get('/reportitem/' + str(reportitem_1.reportitem_id) + '/edit/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_reportitem')

    def test_reportitem_edit_redirect(self):
        """ test edit view """

        # get object
        reportitem_1 = Reportitem.objects.get(reportitem_note='lorem ipsum')
        # login testuser
        self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # create url
        destination = urllib.parse.quote('/reportitem/' + str(reportitem_1.reportitem_id) + '/edit/', safe='/')
        # get response
        response = self.client.get('/reportitem/' + str(reportitem_1.reportitem_id) + '/edit', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_reportitem_edit_post_redirect(self):
        """ test edit view """

        # login testuser
        self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # get user
        test_user = User.objects.get(username='testuser_reportitem')
        # get objects
        headline_1 = Headline.objects.get(headline_name = 'headline_1')
        notestatus_1 = Notestatus.objects.get(notestatus_name = 'notestatus_1')
        system_1 = System.objects.get(system_name = 'system_1')
        tag_id = Tag.objects.get(tag_name = 'tag_1').tag_id
        # create object
        reportitem_1 = Reportitem.objects.create(
            reportitem_note = 'reportitem_edit_post_test_1',
            headline = headline_1,
            notestatus = notestatus_1,
            system = system_1,
            reportitem_created_by_user_id = test_user,
            reportitem_modified_by_user_id = test_user,
        )
        # create post data
        data_dict = {
            'reportitem_note': 'reportitem_edit_post_test_2',
            'headline': headline_1.headline_id,
            'notestatus': notestatus_1.notestatus_id,
            'system': system_1.system_id,
            'tag': [tag_id, ],
        }
        # get response
        response = self.client.post('/reportitem/' + str(reportitem_1.reportitem_id) + '/edit/', data_dict)
        # create url
        destination = urllib.parse.quote('/system/' + str(system_1.system_id) + '/', safe='/')
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_reportitem_edit_post_redirect_documentation(self):
        """ test edit view """

        # login testuser
        self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # get user
        test_user = User.objects.get(username='testuser_reportitem')
        # get objects
        headline_1 = Headline.objects.get(headline_name = 'headline_1')
        notestatus_1 = Notestatus.objects.get(notestatus_name = 'notestatus_1')
        system_1 = System.objects.get(system_name = 'system_1')
        tag_id = Tag.objects.get(tag_name = 'tag_1').tag_id
        # create object
        reportitem_1 = Reportitem.objects.create(
            reportitem_note = 'reportitem_edit_post_test_1_documentation',
            headline = headline_1,
            notestatus = notestatus_1,
            system = system_1,
            reportitem_created_by_user_id = test_user,
            reportitem_modified_by_user_id = test_user,
        )
        # create post data
        data_dict = {
            'reportitem_note': 'reportitem_edit_post_test_2_documentation',
            'headline': headline_1.headline_id,
            'notestatus': notestatus_1.notestatus_id,
            'system': system_1.system_id,
            'tag': [tag_id, ],
        }
        # get response
        response = self.client.post('/reportitem/' + str(reportitem_1.reportitem_id) + '/edit/?documentation', data_dict)
        # get object
        reportitem_id = Reportitem.objects.get(reportitem_note='reportitem_edit_post_test_2_documentation').reportitem_id
        # create url
        destination = urllib.parse.quote(f'/documentation/#reportitem_id_{str(reportitem_id)}', safe='#/')
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_reportitem_edit_post_invalid_reload(self):
        """ test edit view """

        # login testuser
        self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # get object
        reportitem_id = Reportitem.objects.get(reportitem_note='lorem ipsum').reportitem_id
        # create post data
        data_dict = {}
        # get response
        response = self.client.post('/reportitem/' + str(reportitem_id) + '/edit/', data_dict)
        # compare
        self.assertEqual(response.status_code, 200)

    def test_reportitem_edit_post_invalid_template(self):
        """ test edit view """

        # login testuser
        self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # get object
        reportitem_id = Reportitem.objects.get(reportitem_note='lorem ipsum').reportitem_id
        # create post data
        data_dict = {}
        # get response
        response = self.client.post('/reportitem/' + str(reportitem_id) + '/edit/', data_dict)
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/reportitem/reportitem_generic_form.html')

    def test_reportitem_edit_post_system_case_assigned_message(self):
        """ test edit view """

        # login testuser
        self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # get user
        test_user = User.objects.get(username='testuser_reportitem')
        # get objects
        headline_1 = Headline.objects.get(headline_name = 'headline_1')
        notestatus_1 = Notestatus.objects.get(notestatus_name = 'notestatus_1')
        system_1 = System.objects.get(system_name = 'system_1')
        case_1 = Case.objects.get(case_name = 'case_1')
        # create object
        reportitem_1 = Reportitem.objects.create(
            reportitem_note = 'reportitem_edit_post_case_test_1',
            headline = headline_1,
            notestatus = notestatus_1,
            system = system_1,
            reportitem_created_by_user_id = test_user,
            reportitem_modified_by_user_id = test_user,
        )
        # create post data
        data_dict = {
            'reportitem_note': 'reportitem_edit_post_case_test_2',
            'headline': headline_1.headline_id,
            'notestatus': notestatus_1.notestatus_id,
            'system': system_1.system_id,
            'case': [case_1.case_id, ],
        }
        # get response
        response = self.client.post('/reportitem/' + str(reportitem_1.reportitem_id) + '/edit/', data_dict, follow=True)
        # create url
        destination = urllib.parse.quote('/system/' + str(system_1.system_id) + '/', safe='/')
        
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
        self.assertContains(response, f"System &#x27;{system_1.system_name}&#x27; was assigned to case &#x27;{case_1.case_name}&#x27; due to reportitem assignment.")