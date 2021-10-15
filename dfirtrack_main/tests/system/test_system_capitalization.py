from django.contrib.auth.models import User
from django.test import TestCase

from dfirtrack_config.models import MainConfigModel
from dfirtrack_main.models import System, Systemstatus


def set_capitalization_config(capitalization):
    """change main config"""

    # get config
    main_config = MainConfigModel.objects.get(main_config_name='MainConfig')
    # set values
    main_config.capitalization = capitalization
    # save config
    main_config.save()

    # return to test
    return

class SystemCapitalizationModelTestCase(TestCase):
    """system capitalization model tests"""

    @classmethod
    def setUpTestData(cls):

        # create user
        User.objects.create_user(
            username='testuser_system_capitalization', password='tk24SP86CP6pnIGSZpNP'
        )

        # create objects
        Systemstatus.objects.create(systemstatus_name='systemstatus_1')

    def test_system_capitalization_keep(self):
        """test capitalization"""

        # change config
        set_capitalization_config('capitalization_keep')
        # get objects
        systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')
        test_user = User.objects.get(username='testuser_system_capitalization')
        # create objects
        System.objects.create(
            system_name='cap_system_11',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )
        System.objects.create(
            system_name='CAP_SYSTEM_12',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )
        System.objects.create(
            system_name='Cap_System_13',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )
        System.objects.create(
            system_name='CaP_SyStem_14',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )
        # compare
        self.assertTrue(System.objects.filter(system_name='cap_system_11').exists())
        self.assertTrue(System.objects.filter(system_name='CAP_SYSTEM_12').exists())
        self.assertTrue(System.objects.filter(system_name='Cap_System_13').exists())
        self.assertTrue(System.objects.filter(system_name='CaP_SyStem_14').exists())

    def test_system_capitalization_lower(self):
        """test capitalization"""

        # change config
        set_capitalization_config('capitalization_lower')
        # get objects
        systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')
        test_user = User.objects.get(username='testuser_system_capitalization')
        # create objects
        System.objects.create(
            system_name='cap_system_21',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )
        System.objects.create(
            system_name='CAP_SYSTEM_22',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )
        System.objects.create(
            system_name='Cap_System_23',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )
        System.objects.create(
            system_name='CaP_SyStem_24',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )
        # compare
        self.assertTrue(System.objects.filter(system_name='cap_system_21').exists())
        self.assertTrue(System.objects.filter(system_name='cap_system_22').exists())
        self.assertTrue(System.objects.filter(system_name='cap_system_23').exists())
        self.assertTrue(System.objects.filter(system_name='cap_system_24').exists())

    def test_system_capitalization_upper(self):
        """test capitalization"""

        # change config
        set_capitalization_config('capitalization_upper')
        # get objects
        systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')
        test_user = User.objects.get(username='testuser_system_capitalization')
        # create objects
        System.objects.create(
            system_name='cap_system_31',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )
        System.objects.create(
            system_name='CAP_SYSTEM_32',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )
        System.objects.create(
            system_name='Cap_System_33',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )
        System.objects.create(
            system_name='CaP_SyStem_34',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )
        # compare
        self.assertTrue(System.objects.filter(system_name='CAP_SYSTEM_31').exists())
        self.assertTrue(System.objects.filter(system_name='CAP_SYSTEM_32').exists())
        self.assertTrue(System.objects.filter(system_name='CAP_SYSTEM_33').exists())
        self.assertTrue(System.objects.filter(system_name='CAP_SYSTEM_34').exists())
