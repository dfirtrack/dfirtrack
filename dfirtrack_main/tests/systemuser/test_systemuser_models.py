from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone
from dfirtrack_main.models import System, Systemstatus, Systemuser

class SystemuserModelTestCase(TestCase):
    """ systemuser model tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_systemuser', password='u6YexpBiCjk1fdx68uHY')
        test_user.save()

        # create object
        systemstatus_1 = Systemstatus.objects.create(systemstatus_name='systemstatus_1')

        # create object
        system_1 = System.objects.create(
            system_name='system_1',
            systemstatus = systemstatus_1,
            system_modify_time = timezone.now(),
            system_created_by_user_id = test_user,
            system_modified_by_user_id = test_user,
        )

        # create object
        Systemuser.objects.create(systemuser_name='systemuser_1', system = system_1)

    def test_systemuser_string(self):

        # get object
        systemuser_1 = Systemuser.objects.get(systemuser_name='systemuser_1')
        # compare
        self.assertEqual(str(systemuser_1), systemuser_1.systemuser_name + ' (' + str(systemuser_1.system) + ')')

    def test_systemuser_name_label(self):

        # get object
        systemuser_1 = Systemuser.objects.get(systemuser_name='systemuser_1')
        # get label
        field_label = systemuser_1._meta.get_field('systemuser_name').verbose_name
        # compare
        self.assertEquals(field_label, 'systemuser name')

    def test_systemuser_lastlogon_time_label(self):

        # get object
        systemuser_1 = Systemuser.objects.get(systemuser_name='systemuser_1')
        # get label
        field_label = systemuser_1._meta.get_field('systemuser_lastlogon_time').verbose_name
        # compare
        self.assertEquals(field_label, 'systemuser lastlogon time')

    def test_systemuser_system_label(self):

        # get object
        systemuser_1 = Systemuser.objects.get(systemuser_name='systemuser_1')
        # get label
        field_label = systemuser_1._meta.get_field('system').verbose_name
        # compare
        self.assertEquals(field_label, 'system')

    def test_systemuser_name_length(self):

        # get object
        systemuser_1 = Systemuser.objects.get(systemuser_name='systemuser_1')
        # get max length
        max_length = systemuser_1._meta.get_field('systemuser_name').max_length
        # compare
        self.assertEquals(max_length, 50)
