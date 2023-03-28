from django.contrib.auth.models import User
from django.test import TestCase

from dfirtrack_main.models import Case


class CaseModelTestCase(TestCase):
    """case model tests"""

    @classmethod
    def setUpTestData(cls):
        # create user
        test_user = User.objects.create_user(
            username='testuser_case', password='ubtMz0kJgkeBqBKNlNUG'
        )

        # create object
        Case.objects.create(
            case_name='case_1',
            case_is_incident=True,
            case_created_by_user_id=test_user,
        )

    def test_case_string(self):
        """test string representation"""

        # get object
        case_1 = Case.objects.get(case_name='case_1')
        # compare
        self.assertEqual(str(case_1), 'case_1')

    def test_case_id_attribute_label(self):
        """test attribute label"""

        # get object
        case_1 = Case.objects.get(case_name='case_1')
        # get label
        field_label = case_1._meta.get_field('case_id').verbose_name
        # compare
        self.assertEqual(field_label, 'case id')

    def test_case_id_external_attribute_label(self):
        """test attribute label"""

        # get object
        case_1 = Case.objects.get(case_name='case_1')
        # get label
        field_label = case_1._meta.get_field('case_id_external').verbose_name
        # compare
        self.assertEqual(field_label, 'case id external')

    def test_case_name_attribute_label(self):
        """test attribute label"""

        # get object
        case_1 = Case.objects.get(case_name='case_1')
        # get label
        field_label = case_1._meta.get_field('case_name').verbose_name
        # compare
        self.assertEqual(field_label, 'case name')

    def test_case_is_incident_attribute_label(self):
        """test attribute label"""

        # get object
        case_1 = Case.objects.get(case_name='case_1')
        # get label
        field_label = case_1._meta.get_field('case_is_incident').verbose_name
        # compare
        self.assertEqual(field_label, 'case is incident')

    def test_case_note_analysisresult_attribute_label(self):
        """test attribute label"""

        # get object
        case_1 = Case.objects.get(case_name='case_1')
        # get label
        field_label = case_1._meta.get_field('case_note_analysisresult').verbose_name
        # compare
        self.assertEqual(field_label, 'case note analysisresult')

    def test_case_note_external_attribute_label(self):
        """test attribute label"""

        # get object
        case_1 = Case.objects.get(case_name='case_1')
        # get label
        field_label = case_1._meta.get_field('case_note_external').verbose_name
        # compare
        self.assertEqual(field_label, 'case note external')

    def test_case_note_internal_attribute_label(self):
        """test attribute label"""

        # get object
        case_1 = Case.objects.get(case_name='case_1')
        # get label
        field_label = case_1._meta.get_field('case_note_internal').verbose_name
        # compare
        self.assertEqual(field_label, 'case note internal')

    def test_case_start_time_attribute_label(self):
        """test attribute label"""

        # get object
        case_1 = Case.objects.get(case_name='case_1')
        # get label
        field_label = case_1._meta.get_field('case_start_time').verbose_name
        # compare
        self.assertEqual(field_label, 'case start time')

    def test_case_end_time_attribute_label(self):
        """test attribute label"""

        # get object
        case_1 = Case.objects.get(case_name='case_1')
        # get label
        field_label = case_1._meta.get_field('case_end_time').verbose_name
        # compare
        self.assertEqual(field_label, 'case end time')

    def test_case_create_time_attribute_label(self):
        """test attribute label"""

        # get object
        case_1 = Case.objects.get(case_name='case_1')
        # get label
        field_label = case_1._meta.get_field('case_create_time').verbose_name
        # compare
        self.assertEqual(field_label, 'case create time')

    def test_case_modify_time_attribute_label(self):
        """test attribute label"""

        # get object
        case_1 = Case.objects.get(case_name='case_1')
        # get label
        field_label = case_1._meta.get_field('case_modify_time').verbose_name
        # compare
        self.assertEqual(field_label, 'case modify time')

    def test_case_created_by_user_id_attribute_label(self):
        """test attribute label"""

        # get object
        case_1 = Case.objects.get(case_name='case_1')
        # get label
        field_label = case_1._meta.get_field('case_created_by_user_id').verbose_name
        # compare
        self.assertEqual(field_label, 'case created by user id')

    def test_case_modified_by_user_id_attribute_label(self):
        """test attribute label"""

        # get object
        case_1 = Case.objects.get(case_name='case_1')
        # get label
        field_label = case_1._meta.get_field('case_modified_by_user_id').verbose_name
        # compare
        self.assertEqual(field_label, 'case modified by user id')

    def test_casepriority_attribute_label(self):
        """test attribute label"""

        # get object
        case_1 = Case.objects.get(case_name='case_1')
        # get label
        field_label = case_1._meta.get_field('casepriority').verbose_name
        # compare
        self.assertEqual(field_label, 'casepriority')

    def test_casestatus_attribute_label(self):
        """test attribute label"""

        # get object
        case_1 = Case.objects.get(case_name='case_1')
        # get label
        field_label = case_1._meta.get_field('casestatus').verbose_name
        # compare
        self.assertEqual(field_label, 'casestatus')

    def test_casetype_attribute_label(self):
        """test attribute label"""

        # get object
        case_1 = Case.objects.get(case_name='case_1')
        # get label
        field_label = case_1._meta.get_field('casetype').verbose_name
        # compare
        self.assertEqual(field_label, 'casetype')

    def test_tag_attribute_label(self):
        """test attribute label"""

        # get object
        case_1 = Case.objects.get(case_name='case_1')
        # get label
        field_label = case_1._meta.get_field('tag').verbose_name
        # compare
        self.assertEqual(field_label, 'tag')

    def test_case_assigned_to_user_id_attribute_label(self):
        """test attribute label"""

        # get object
        case_1 = Case.objects.get(case_name='case_1')
        # get label
        field_label = case_1._meta.get_field('case_assigned_to_user_id').verbose_name
        # compare
        self.assertEqual(field_label, 'case assigned to user id')

    def test_case_name_length(self):
        """test for max length"""

        # get object
        case_1 = Case.objects.get(case_name='case_1')
        # get max length
        max_length = case_1._meta.get_field('case_name').max_length
        # compare
        self.assertEqual(max_length, 255)

    def test_case_id_external_length(self):
        """test for max length"""

        # get object
        case_1 = Case.objects.get(case_name='case_1')
        # get max length
        max_length = case_1._meta.get_field('case_id_external').max_length
        # compare
        self.assertEqual(max_length, 255)

    def test_case_get_set_user_url(self):
        """test URL method"""

        # get object
        case_1 = Case.objects.get(case_name='case_1')
        # compare
        self.assertEqual(case_1.get_set_user_url(), f'/case/{case_1.case_id}/set_user/')

    def test_case_get_unset_user_url(self):
        """test URL method"""

        # get object
        case_1 = Case.objects.get(case_name='case_1')
        # compare
        self.assertEqual(
            case_1.get_unset_user_url(), f'/case/{case_1.case_id}/unset_user/'
        )
