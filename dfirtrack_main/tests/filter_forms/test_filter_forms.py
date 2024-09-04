from django.contrib.auth.models import User
from django.test import TestCase

from dfirtrack_config.models import UserConfigModel
from dfirtrack_main.filter_forms import GeneralFilterForm
from dfirtrack_main.models import Notestatus


class GeneralFilterFormTestCase(TestCase):
    """system filter form tests"""

    @classmethod
    def setUpTestData(cls):
        # create user
        test_user = User.objects.create_user(
            username='testuser_filter_forms_general', password='LqShcoecDudasdRxhfKV'
        )

        # create config
        UserConfigModel.objects.get_or_create(
            user_config_username=test_user, filter_view='documentation'
        )

    def test_case_form_label(self):
        """test form label"""

        # get object
        form = GeneralFilterForm()
        # compare
        self.assertEqual(form.fields['filter_query'].label, 'Filter query')

    def test_system_filter_form_empty(self):
        """test minimum form requirements / VALID"""

        # create user
        test_user = User.objects.get(username='testuser_filter_forms_general')

        # create config
        user_config = UserConfigModel.objects.get(
            user_config_username=test_user, filter_view='documentation'
        )

        # get object
        form = GeneralFilterForm(data={'user_config_id': user_config.user_config_id})
        # compare
        self.assertTrue(form.is_valid())
