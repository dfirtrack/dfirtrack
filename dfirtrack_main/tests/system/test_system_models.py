from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone

from dfirtrack_main.models import System, Systemstatus


class SystemModelTestCase(TestCase):
    """system model tests"""

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(
            username='testuser_system', password='6rGHXEkDxRYuRsUeT7DW'
        )

        # create object
        systemstatus_1 = Systemstatus.objects.create(systemstatus_name='systemstatus_1')

        # create object
        System.objects.create(
            system_name='system_1',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )

        # create object
        System.objects.create(
            system_name='system_2',
            systemstatus=systemstatus_1,
            system_install_time=timezone.now(),
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )

    def test_system_string_without_install_time(self):
        """test string representation"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # compare
        self.assertEqual(
            str(system_1), '[' + str(system_1.system_id) + '] ' + system_1.system_name
        )

    def test_system_string_withinstall_time(self):
        """test string representation"""

        # get object
        system_2 = System.objects.get(system_name='system_2')
        # format time string
        installtime = system_2.system_install_time.strftime('%Y-%m-%d')
        # compare
        self.assertEqual(
            str(system_2),
            '['
            + str(system_2.system_id)
            + '] '
            + system_2.system_name
            + ' ('
            + installtime
            + ')',
        )

    def test_system_id_attribute_label(self):
        """test attribute label"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # get label
        field_label = system_1._meta.get_field('system_id').verbose_name
        # compare
        self.assertEqual(field_label, 'system id')

    def test_system_systemstatus_attribute_label(self):
        """test attribute label"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # get label
        field_label = system_1._meta.get_field('systemstatus').verbose_name
        # compare
        self.assertEqual(field_label, 'systemstatus')

    def test_system_analysisstatus_attribute_label(self):
        """test attribute label"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # get label
        field_label = system_1._meta.get_field('analysisstatus').verbose_name
        # compare
        self.assertEqual(field_label, 'analysisstatus')

    def test_system_reason_attribute_label(self):
        """test attribute label"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # get label
        field_label = system_1._meta.get_field('reason').verbose_name
        # compare
        self.assertEqual(field_label, 'reason')

    def test_system_recommendation_attribute_label(self):
        """test attribute label"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # get label
        field_label = system_1._meta.get_field('recommendation').verbose_name
        # compare
        self.assertEqual(field_label, 'recommendation')

    def test_system_systemtype_attribute_label(self):
        """test attribute label"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # get label
        field_label = system_1._meta.get_field('systemtype').verbose_name
        # compare
        self.assertEqual(field_label, 'systemtype')

    def test_system_ip_attribute_label(self):
        """test attribute label"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # get label
        field_label = system_1._meta.get_field('ip').verbose_name
        # compare
        self.assertEqual(field_label, 'ip')

    def test_system_domain_attribute_label(self):
        """test attribute label"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # get label
        field_label = system_1._meta.get_field('domain').verbose_name
        # compare
        self.assertEqual(field_label, 'domain')

    def test_system_dnsname_attribute_label(self):
        """test attribute label"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # get label
        field_label = system_1._meta.get_field('dnsname').verbose_name
        # compare
        self.assertEqual(field_label, 'dnsname')

    def test_system_os_attribute_label(self):
        """test attribute label"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # get label
        field_label = system_1._meta.get_field('os').verbose_name
        # compare
        self.assertEqual(field_label, 'os')

    def test_system_osarch_attribute_label(self):
        """test attribute label"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # get label
        field_label = system_1._meta.get_field('osarch').verbose_name
        # compare
        self.assertEqual(field_label, 'osarch')

    def test_system_host_system_attribute_label(self):
        """test attribute label"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # get label
        field_label = system_1._meta.get_field('host_system').verbose_name
        # compare
        self.assertEqual(field_label, 'host system')

    def test_system_company_attribute_label(self):
        """test attribute label"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # get label
        field_label = system_1._meta.get_field('company').verbose_name
        # compare
        self.assertEqual(field_label, 'company')

    def test_system_location_attribute_label(self):
        """test attribute label"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # get label
        field_label = system_1._meta.get_field('location').verbose_name
        # compare
        self.assertEqual(field_label, 'location')

    def test_system_serviceprovider_attribute_label(self):
        """test attribute label"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # get label
        field_label = system_1._meta.get_field('serviceprovider').verbose_name
        # compare
        self.assertEqual(field_label, 'serviceprovider')

    def test_system_contact_attribute_label(self):
        """test attribute label"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # get label
        field_label = system_1._meta.get_field('contact').verbose_name
        # compare
        self.assertEqual(field_label, 'contact')

    def test_system_tag_attribute_label(self):
        """test attribute label"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # get label
        field_label = system_1._meta.get_field('tag').verbose_name
        # compare
        self.assertEqual(field_label, 'tag')

    def test_system_case_attribute_label(self):
        """test attribute label"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # get label
        field_label = system_1._meta.get_field('case').verbose_name
        # compare
        self.assertEqual(field_label, 'case')

    def test_system_uuid_attribute_label(self):
        """test attribute label"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # get label
        field_label = system_1._meta.get_field('system_uuid').verbose_name
        # compare
        self.assertEqual(field_label, 'system uuid')

    def test_system_name_attribute_label(self):
        """test attribute label"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # get label
        field_label = system_1._meta.get_field('system_name').verbose_name
        # compare
        self.assertEqual(field_label, 'system name')

    def test_system_install_time_attribute_label(self):
        """test attribute label"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # get label
        field_label = system_1._meta.get_field('system_install_time').verbose_name
        # compare
        self.assertEqual(field_label, 'system install time')

    def test_system_lastbooted_time_attribute_label(self):
        """test attribute label"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # get label
        field_label = system_1._meta.get_field('system_lastbooted_time').verbose_name
        # compare
        self.assertEqual(field_label, 'system lastbooted time')

    def test_system_deprecated_time_attribute_label(self):
        """test attribute label"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # get label
        field_label = system_1._meta.get_field('system_deprecated_time').verbose_name
        # compare
        self.assertEqual(field_label, 'system deprecated time')

    def test_system_is_vm_attribute_label(self):
        """test attribute label"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # get label
        field_label = system_1._meta.get_field('system_is_vm').verbose_name
        # compare
        self.assertEqual(field_label, 'system is vm')

    def test_system_create_time_attribute_label(self):
        """test attribute label"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # get label
        field_label = system_1._meta.get_field('system_create_time').verbose_name
        # compare
        self.assertEqual(field_label, 'system create time')

    def test_system_modify_time_attribute_label(self):
        """test attribute label"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # get label
        field_label = system_1._meta.get_field('system_modify_time').verbose_name
        # compare
        self.assertEqual(field_label, 'system modify time')

    def test_system_created_by_user_id_attribute_label(self):
        """test attribute label"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # get label
        field_label = system_1._meta.get_field('system_created_by_user_id').verbose_name
        # compare
        self.assertEqual(field_label, 'system created by user id')

    def test_system_modified_by_user_id_attribute_label(self):
        """test attribute label"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # get label
        field_label = system_1._meta.get_field(
            'system_modified_by_user_id'
        ).verbose_name
        # compare
        self.assertEqual(field_label, 'system modified by user id')

    def test_system_assigned_to_user_id_attribute_label(self):
        """test attribute label"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # get label
        field_label = system_1._meta.get_field(
            'system_assigned_to_user_id'
        ).verbose_name
        # compare
        self.assertEqual(field_label, 'system assigned to user id')

    def test_system_name_length(self):
        """test for max length"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # get max length
        max_length = system_1._meta.get_field('system_name').max_length
        # compare
        self.assertEqual(max_length, 255)

    def test_system_get_set_user_url(self):
        """test URL method"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # compare
        self.assertEqual(system_1.get_set_user_url(), f'/system/{system_1.system_id}/set_user/')

    def test_system_get_unset_user_url(self):
        """test URL method"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # compare
        self.assertEqual(system_1.get_unset_user_url(), f'/system/{system_1.system_id}/unset_user/')

    def test_system_toggle_artifact_url(self):
        """test URL method"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # compare
        self.assertEqual(system_1.get_toggle_artifact_url(), f'/system/{system_1.system_id}/toggle_artifact/')

    def test_system_toggle_artifact_closed_url(self):
        """test URL method"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # compare
        self.assertEqual(system_1.get_toggle_artifact_closed_url(), f'/system/{system_1.system_id}/toggle_artifact_closed/')

    def test_system_toggle_task_url(self):
        """test URL method"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # compare
        self.assertEqual(system_1.get_toggle_task_url(), f'/system/{system_1.system_id}/toggle_task/')

    def test_system_toggle_task_closed_url(self):
        """test URL method"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # compare
        self.assertEqual(system_1.get_toggle_task_closed_url(), f'/system/{system_1.system_id}/toggle_task_closed/')

    def test_system_toggle_technical_information_url(self):
        """test URL method"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # compare
        self.assertEqual(system_1.get_toggle_technical_information_url(), f'/system/{system_1.system_id}/toggle_technical_information/')

    def test_system_toggle_timeline_url(self):
        """test URL method"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # compare
        self.assertEqual(system_1.get_toggle_timeline_url(), f'/system/{system_1.system_id}/toggle_timeline/')

    def test_system_toggle_virtualization_information_url(self):
        """test URL method"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # compare
        self.assertEqual(system_1.get_toggle_virtualization_information_url(), f'/system/{system_1.system_id}/toggle_virtualization_information/')

    def test_system_toggle_company_information_url(self):
        """test URL method"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # compare
        self.assertEqual(system_1.get_toggle_company_information_url(), f'/system/{system_1.system_id}/toggle_company_information/')

    def test_system_toggle_systemuser_url(self):
        """test URL method"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # compare
        self.assertEqual(system_1.get_toggle_systemuser_url(), f'/system/{system_1.system_id}/toggle_systemuser/')

    def test_system_toggle_analystmemo_url(self):
        """test URL method"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # compare
        self.assertEqual(system_1.get_toggle_analystmemo_url(), f'/system/{system_1.system_id}/toggle_analystmemo/')

    def test_system_toggle_reportitem_url(self):
        """test URL method"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # compare
        self.assertEqual(system_1.get_toggle_reportitem_url(), f'/system/{system_1.system_id}/toggle_reportitem/')
