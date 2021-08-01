from django.contrib.auth.models import User
from django.test import TestCase

from dfirtrack_main.forms import CaseCreatorForm
from dfirtrack_main.models import Case, Casepriority, Casestatus, System, Systemstatus


class CaseCreatorFormTestCase(TestCase):
    """ case creator form tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_case_creator', password='NxJXVw8dpKA5AeoXSz2F')

        # create object
        systemstatus_1 = Systemstatus.objects.create(systemstatus_name='systemstatus_1')

        # create object
        System.objects.create(
            system_name = 'system_1',
            systemstatus = systemstatus_1,
            system_created_by_user_id = test_user,
            system_modified_by_user_id = test_user,
        )
        System.objects.create(
            system_name = 'system_2',
            systemstatus = systemstatus_1,
            system_created_by_user_id = test_user,
            system_modified_by_user_id = test_user,
        )

        # create object
        casepriority_1 = Casepriority.objects.create(casepriority_name='casepriority_1')
        casestatus_1 = Casestatus.objects.create(casestatus_name='casestatus_1')

        # create object
        Case.objects.create(
            case_name = 'case_1',
            casepriority = casepriority_1,
            casestatus = casestatus_1,
            case_is_incident = False,
            case_created_by_user_id = test_user,
            case_modified_by_user_id = test_user,
        )
        Case.objects.create(
            case_name = 'case_2',
            casepriority = casepriority_1,
            casestatus = casestatus_1,
            case_is_incident = False,
            case_created_by_user_id = test_user,
            case_modified_by_user_id = test_user,
        )

    def test_case_creator_case_form_label(self):
        """ test form label """

        # get object
        form = CaseCreatorForm()
        # compare
        self.assertEqual(form.fields['case'].label, 'Cases (*)')

    def test_case_creator_system_form_label(self):
        """ test form label """

        # get object
        form = CaseCreatorForm()
        # compare
        self.assertEqual(form.fields['system'].label, 'Systems (*)')

    def test_case_creator_form_empty(self):
        """ test minimum form requirements / INVALID """

        # get object
        form = CaseCreatorForm(data = {})
        # compare
        self.assertFalse(form.is_valid())

    def test_case_creator_system_form_filled(self):
        """ test minimum form requirements / INVALID """

        # get object
        system_1_id = System.objects.get(system_name='system_1').system_id
        system_2_id = System.objects.get(system_name='system_2').system_id
        # get object
        form = CaseCreatorForm(data = {
            'system': [system_1_id, system_2_id],
        })
        # compare
        self.assertFalse(form.is_valid())

    def test_case_creator_case_form_filled(self):
        """ test minimum form requirements / VALID """

        # get object
        case_1_id = Case.objects.get(case_name='case_1').case_id
        case_2_id = Case.objects.get(case_name='case_2').case_id
        # get object
        system_1_id = System.objects.get(system_name='system_1').system_id
        system_2_id = System.objects.get(system_name='system_2').system_id
        # get object
        form = CaseCreatorForm(data = {
            'system': [system_1_id, system_2_id],
            'case': [case_1_id, case_2_id],
        })
        # compare
        self.assertTrue(form.is_valid())
