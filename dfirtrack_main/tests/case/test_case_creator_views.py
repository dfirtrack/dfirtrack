import urllib.parse

from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import TestCase

from dfirtrack_main.models import Case, Casepriority, Casestatus, System, Systemstatus


class CaseCreatorViewTestCase(TestCase):
    """case creator view tests"""

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(
            username='testuser_case_creator', password='r3UOy6A3nUIF3507jksW'
        )

        # create object
        casepriority_1 = Casepriority.objects.create(casepriority_name='casepriority_1')
        casestatus_1 = Casestatus.objects.create(casestatus_name='casestatus_1')

        # create object
        Case.objects.create(
            case_name='case_creator_case_1',
            casepriority=casepriority_1,
            casestatus=casestatus_1,
            case_is_incident=False,
            case_created_by_user_id=test_user,
            case_modified_by_user_id=test_user,
        )
        Case.objects.create(
            case_name='case_creator_case_2',
            casepriority=casepriority_1,
            casestatus=casestatus_1,
            case_is_incident=False,
            case_created_by_user_id=test_user,
            case_modified_by_user_id=test_user,
        )
        Case.objects.create(
            case_name='case_creator_case_3',
            casepriority=casepriority_1,
            casestatus=casestatus_1,
            case_is_incident=False,
            case_created_by_user_id=test_user,
            case_modified_by_user_id=test_user,
        )

        # create object
        systemstatus_1 = Systemstatus.objects.create(
            systemstatus_name='case_creator_systemstatus_1'
        )

        # create objects
        System.objects.create(
            system_name='case_creator_system_1',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )
        System.objects.create(
            system_name='case_creator_system_2',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )
        System.objects.create(
            system_name='case_creator_system_3',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )

    def test_case_creator_not_logged_in(self):
        """test creator view"""

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/case/creator/', safe='')
        # get response
        response = self.client.get('/case/creator/', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_case_creator_logged_in(self):
        """test creator view"""

        # login testuser
        self.client.login(
            username='testuser_case_creator', password='r3UOy6A3nUIF3507jksW'
        )
        # get response
        response = self.client.get('/case/creator/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_case_creator_template(self):
        """test creator view"""

        # login testuser
        self.client.login(
            username='testuser_case_creator', password='r3UOy6A3nUIF3507jksW'
        )
        # get response
        response = self.client.get('/case/creator/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/case/case_creator.html')

    def test_case_creator_get_user_context(self):
        """test creator view"""

        # login testuser
        self.client.login(
            username='testuser_case_creator', password='r3UOy6A3nUIF3507jksW'
        )
        # get response
        response = self.client.get('/case/creator/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_case_creator')

    def test_case_creator_redirect(self):
        """test creator view"""

        # login testuser
        self.client.login(
            username='testuser_case_creator', password='r3UOy6A3nUIF3507jksW'
        )
        # create url
        destination = urllib.parse.quote('/case/creator/', safe='/')
        # get response
        response = self.client.get('/case/creator', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )

    def test_case_creator_post_redirect(self):
        """test creator view"""

        # login testuser
        self.client.login(
            username='testuser_case_creator', password='r3UOy6A3nUIF3507jksW'
        )
        # get objects
        case_1 = Case.objects.get(case_name='case_creator_case_1')
        system_1 = System.objects.get(system_name='case_creator_system_1')
        # create post data
        data_dict = {
            'system': [
                system_1.system_id,
            ],
            'case': [
                case_1.case_id,
            ],
        }
        # create url
        destination = '/case/'
        # get response
        response = self.client.post('/case/creator/', data_dict)
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_case_creator_post_system_and_cases(self):
        """test creator view"""

        # login testuser
        self.client.login(
            username='testuser_case_creator', password='r3UOy6A3nUIF3507jksW'
        )
        # get objects
        case_1 = Case.objects.get(case_name='case_creator_case_1')
        case_2 = Case.objects.get(case_name='case_creator_case_2')
        case_3 = Case.objects.get(case_name='case_creator_case_3')
        system_1 = System.objects.get(system_name='case_creator_system_1')
        system_2 = System.objects.get(system_name='case_creator_system_2')
        system_3 = System.objects.get(system_name='case_creator_system_3')
        # create post data
        data_dict = {
            'system': [system_1.system_id, system_2.system_id],
            'case': [case_1.case_id, case_2.case_id],
        }
        # get response
        self.client.post('/case/creator/', data_dict)
        # compare
        self.assertTrue(system_1.case.filter(case_name=case_1.case_name).exists())
        self.assertTrue(system_1.case.filter(case_name=case_2.case_name).exists())
        self.assertFalse(system_1.case.filter(case_name=case_3.case_name).exists())
        self.assertTrue(system_2.case.filter(case_name=case_1.case_name).exists())
        self.assertTrue(system_2.case.filter(case_name=case_2.case_name).exists())
        self.assertFalse(system_2.case.filter(case_name=case_3.case_name).exists())
        self.assertFalse(system_3.case.filter(case_name=case_1.case_name).exists())
        self.assertFalse(system_3.case.filter(case_name=case_2.case_name).exists())
        self.assertFalse(system_3.case.filter(case_name=case_3.case_name).exists())

    def test_case_creator_post_invalid_reload(self):
        """test creator view"""

        # login testuser
        self.client.login(
            username='testuser_case_creator', password='r3UOy6A3nUIF3507jksW'
        )
        # create post data
        data_dict = {}
        # get response
        response = self.client.post('/case/creator/', data_dict)
        # compare
        self.assertEqual(response.status_code, 200)

    def test_case_creator_post_invalid_template(self):
        """test creator view"""

        # login testuser
        self.client.login(
            username='testuser_case_creator', password='r3UOy6A3nUIF3507jksW'
        )
        # create post data
        data_dict = {}
        # get response
        response = self.client.post('/case/creator/', data_dict)
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/case/case_creator.html')

    def test_case_creator_post_messages(self):
        """test creator view"""

        # login testuser
        self.client.login(
            username='testuser_case_creator', password='r3UOy6A3nUIF3507jksW'
        )
        # get objects
        case_1 = Case.objects.get(case_name='case_creator_case_1')
        case_2 = Case.objects.get(case_name='case_creator_case_2')
        case_3 = Case.objects.get(case_name='case_creator_case_3')
        system_1 = System.objects.get(system_name='case_creator_system_1')
        system_2 = System.objects.get(system_name='case_creator_system_2')
        system_3 = System.objects.get(system_name='case_creator_system_3')
        # create post data
        data_dict = {
            'system': [system_1.system_id, system_2.system_id, system_3.system_id],
            'case': [case_1.case_id, case_2.case_id, case_3.case_id],
        }
        # get response
        response = self.client.post('/case/creator/', data_dict)
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(str(messages[0]), 'Case creator started')
        self.assertEqual(str(messages[1]), '3 cases assigned to 3 systems.')
