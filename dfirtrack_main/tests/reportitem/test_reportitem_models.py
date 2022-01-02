from django.contrib.auth.models import User
from django.test import TestCase

from dfirtrack_main.models import (
    Case,
    Casepriority,
    Casestatus,
    Headline,
    Reportitem,
    System,
    Systemstatus,
)


class ReportitemModelTestCase(TestCase):
    """reportitem model tests"""

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(
            username='testuser_reportitem', password='n26RCEzVtmtmpAHa5g1M'
        )

        # create object
        systemstatus_1 = Systemstatus.objects.create(systemstatus_name='systemstatus_1')

        # create object
        system_1 = System.objects.create(
            system_name='system_1',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )

        # create object
        headline_1 = Headline.objects.create(headline_name='headline_1')

        # create object
        Reportitem.objects.create(
            reportitem_note='lorem ipsum',
            system=system_1,
            headline=headline_1,
            reportitem_created_by_user_id=test_user,
            reportitem_modified_by_user_id=test_user,
        )

        # create objects
        casepriority_1 = Casepriority.objects.create(casepriority_name='casepriority_1')
        casestatus_1 = Casestatus.objects.create(casestatus_name='casestatus_1')

        # create object
        Case.objects.create(
            case_name='case_1',
            case_is_incident=True,
            case_created_by_user_id=test_user,
            casepriority=casepriority_1,
            casestatus=casestatus_1,
        )

    def test_reportitem_string(self):
        """test string representation"""

        # get object
        reportitem_1 = Reportitem.objects.get(reportitem_note='lorem ipsum')
        # compare
        self.assertEqual(
            str(reportitem_1),
            str(reportitem_1.system)
            + ' | '
            + str(reportitem_1.headline.headline_name)
            + ' | '
            + str(reportitem_1.reportitem_subheadline),
        )

    def test_reportitem_id_attribute_label(self):
        """test attribute label"""

        # get object
        reportitem_1 = Reportitem.objects.get(reportitem_note='lorem ipsum')
        # get label
        field_label = reportitem_1._meta.get_field('reportitem_id').verbose_name
        # compare
        self.assertEqual(field_label, 'reportitem id')

    def test_reportitem_case_attribute_label(self):
        """test attribute label"""

        # get object
        reportitem_1 = Reportitem.objects.get(reportitem_note='lorem ipsum')
        # get label
        field_label = reportitem_1._meta.get_field('case').verbose_name
        # compare
        self.assertEqual(field_label, 'case')

    def test_reportitem_headline_attribute_label(self):
        """test attribute label"""

        # get object
        reportitem_1 = Reportitem.objects.get(reportitem_note='lorem ipsum')
        # get label
        field_label = reportitem_1._meta.get_field('headline').verbose_name
        # compare
        self.assertEqual(field_label, 'headline')

    def test_reportitem_notestatus_attribute_label(self):
        """test attribute label"""

        # get object
        reportitem_1 = Reportitem.objects.get(reportitem_note='lorem ipsum')
        # get label
        field_label = reportitem_1._meta.get_field('notestatus').verbose_name
        # compare
        self.assertEqual(field_label, 'notestatus')

    def test_reportitem_system_attribute_label(self):
        """test attribute label"""

        # get object
        reportitem_1 = Reportitem.objects.get(reportitem_note='lorem ipsum')
        # get label
        field_label = reportitem_1._meta.get_field('system').verbose_name
        # compare
        self.assertEqual(field_label, 'system')

    def test_reportitem_tag_attribute_label(self):
        """test attribute label"""

        # get object
        reportitem_1 = Reportitem.objects.get(reportitem_note='lorem ipsum')
        # get label
        field_label = reportitem_1._meta.get_field('tag').verbose_name
        # compare
        self.assertEqual(field_label, 'tag')

    def test_reportitem_subheadline_attribute_label(self):
        """test attribute label"""

        # get object
        reportitem_1 = Reportitem.objects.get(reportitem_note='lorem ipsum')
        # get label
        field_label = reportitem_1._meta.get_field(
            'reportitem_subheadline'
        ).verbose_name
        # compare
        self.assertEqual(field_label, 'reportitem subheadline')

    def test_reportitem_note_attribute_label(self):
        """test attribute label"""

        # get object
        reportitem_1 = Reportitem.objects.get(reportitem_note='lorem ipsum')
        # get label
        field_label = reportitem_1._meta.get_field('reportitem_note').verbose_name
        # compare
        self.assertEqual(field_label, 'reportitem note')

    def test_reportitem_create_time_attribute_label(self):
        """test attribute label"""

        # get object
        reportitem_1 = Reportitem.objects.get(reportitem_note='lorem ipsum')
        # get label
        field_label = reportitem_1._meta.get_field(
            'reportitem_create_time'
        ).verbose_name
        # compare
        self.assertEqual(field_label, 'reportitem create time')

    def test_reportitem_modify_time_attribute_label(self):
        """test attribute label"""

        # get object
        reportitem_1 = Reportitem.objects.get(reportitem_note='lorem ipsum')
        # get label
        field_label = reportitem_1._meta.get_field(
            'reportitem_modify_time'
        ).verbose_name
        # compare
        self.assertEqual(field_label, 'reportitem modify time')

    def test_reportitem_created_by_user_id_attribute_label(self):
        """test attribute label"""

        # get object
        reportitem_1 = Reportitem.objects.get(reportitem_note='lorem ipsum')
        # get label
        field_label = reportitem_1._meta.get_field(
            'reportitem_created_by_user_id'
        ).verbose_name
        # compare
        self.assertEqual(field_label, 'reportitem created by user id')

    def test_reportitem_modified_by_user_id_attribute_label(self):
        """test attribute label"""

        # get object
        reportitem_1 = Reportitem.objects.get(reportitem_note='lorem ipsum')
        # get label
        field_label = reportitem_1._meta.get_field(
            'reportitem_modified_by_user_id'
        ).verbose_name
        # compare
        self.assertEqual(field_label, 'reportitem modified by user id')

    def test_reportitem_assigned_to_user_id_attribute_label(self):
        """test attribute label"""

        # get object
        reportitem_1 = Reportitem.objects.get(reportitem_note='lorem ipsum')
        # get label
        field_label = reportitem_1._meta.get_field(
            'reportitem_assigned_to_user_id'
        ).verbose_name
        # compare
        self.assertEqual(field_label, 'reportitem assigned to user id')

    def test_reportitem_subheadline_length(self):
        """test for max length"""

        # get object
        reportitem_1 = Reportitem.objects.get(reportitem_note='lorem ipsum')
        # get max length
        max_length = reportitem_1._meta.get_field('reportitem_subheadline').max_length
        # compare
        self.assertEqual(max_length, 255)

    def test_reportitem_post_save_signal(self):
        """test report item post save signal"""

        # get object
        reportitem_1 = Reportitem.objects.get(reportitem_note='lorem ipsum')
        system_1 = System.objects.get(system_name='system_1')
        case_1 = Case.objects.get(case_name='case_1')

        # check reportitem and system should not be part of the case
        self.assertIsNone(reportitem_1.case)
        self.assertQuerysetEqual(system_1.case.all(), [])

        reportitem_1.case = case_1
        reportitem_1.save()

        # check reportitem and system should be part of the case
        self.assertEqual(reportitem_1.case.case_name, case_1.case_name)
        self.assertQuerysetEqual(
            system_1.case.all(),
            [
                case_1,
            ],
        )

    def test_reportitem_get_set_user_url(self):
        """test URL method"""

        # get object
        reportitem_1 = Reportitem.objects.get(reportitem_note='lorem ipsum')
        # compare
        self.assertEqual(reportitem_1.get_set_user_url(), f'/reportitem/{reportitem_1.reportitem_id}/set_user/')

    def test_reportitem_get_unset_user_url(self):
        """test URL method"""

        # get object
        reportitem_1 = Reportitem.objects.get(reportitem_note='lorem ipsum')
        # compare
        self.assertEqual(reportitem_1.get_unset_user_url(), f'/reportitem/{reportitem_1.reportitem_id}/unset_user/')
