from django.contrib.auth.models import User
from django.test import TestCase

from dfirtrack_main.models import System, Systemstatus


class SystemStripModelTestCase(TestCase):
    """system strip model tests"""

    @classmethod
    def setUpTestData(cls):

        # create user
        User.objects.create_user(
            username='testuser_system_strip', password='43IcVLP2qSdrqGufkWOX'
        )

        # create objects
        Systemstatus.objects.create(systemstatus_name='systemstatus_1')

    def test_system_strip(self):
        """test strip"""

        # get objects
        systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')
        test_user = User.objects.get(username='testuser_system_strip')
        # create objects
        System.objects.create(
            system_name='system_strip_normal',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )
        System.objects.create(
            system_name='   system_strip_left',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )
        System.objects.create(
            system_name='system_strip_right   ',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )
        System.objects.create(
            system_name='   system_strip_both   ',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )
        # compare
        self.assertTrue(
            System.objects.filter(system_name='system_strip_normal').exists()
        )
        self.assertTrue(System.objects.filter(system_name='system_strip_left').exists())
        self.assertTrue(
            System.objects.filter(system_name='system_strip_right').exists()
        )
        self.assertTrue(System.objects.filter(system_name='system_strip_both').exists())
        self.assertFalse(
            System.objects.filter(system_name='   system_strip_left').exists()
        )
        self.assertFalse(
            System.objects.filter(system_name='system_strip_right   ').exists()
        )
        self.assertFalse(
            System.objects.filter(system_name='   system_strip_both   ').exists()
        )
