from django.contrib.auth.models import User
from django.test import TestCase

from dfirtrack_config.models import UserConfigModel
from dfirtrack_main.filter_forms import DocumentationFilterForm, GeneralFilterForm
from dfirtrack_main.models import Notestatus


class DocumentationFilterFormTestCase(TestCase):
    """documentation filter form tests"""

    @classmethod
    def setUpTestData(cls):
        # create user
        test_user = User.objects.create_user(
            username='testuser_filter_forms', password='LqShcoecDudasdRxhfKV'
        )

        # create config
        user_config, created = UserConfigModel.objects.get_or_create(
            user_config_username=test_user, filter_view='documentation'
        )

        # create notestatus
        Notestatus.objects.create(notestatus_name='test_filter_forms_status')

    def test_notestatus_form_label(self):
        """test form label"""

        # get object
        form = DocumentationFilterForm()
        # compare
        self.assertEqual(
            form.fields['filter_list_status'].label, 'Filter for notestatus'
        )

    def test_notestatus_form_empty_label(self):
        """test form label"""

        # get object
        form = DocumentationFilterForm()
        # compare
        self.assertEqual(
            form.fields['filter_list_status'].empty_label, 'Filter for notestatus'
        )

    def test_documentation_filter_form_empty(self):
        """test minimum form requirements / VALID"""

        # get user
        test_user = User.objects.get(username='testuser_filter_forms')

        # get user config
        user_config = UserConfigModel.objects.get(
            user_config_username=test_user, filter_view='documentation'
        )

        # get object
        form = DocumentationFilterForm(
            data={'user_config_id': user_config.user_config_id}
        )
        # compare
        self.assertTrue(form.is_valid())

    def test_documentation_filter_form_init(self):
        """Test the init method of the documentation filter form"""

        # get user
        test_user = User.objects.get(username='testuser_filter_forms')

        # get user config
        user_config = UserConfigModel.objects.get(
            user_config_username=test_user, filter_view='documentation'
        )

        # get notestatus
        notestatus = Notestatus.objects.get(notestatus_name='test_filter_forms_status')

        # get object beofre assignment
        form_wo_notestatus = DocumentationFilterForm(
            data={'user_config_id': user_config.user_config_id}, instance=user_config
        )

        # assign notestatus
        user_config.filter_list_status = notestatus
        user_config.save()

        # get object
        form_with_notestatus = DocumentationFilterForm(
            data={'user_config_id': user_config.user_config_id}, instance=user_config
        )

        # compare
        self.assertFalse('filter_list_status' in form_wo_notestatus.initial)
        self.assertEqual(
            form_with_notestatus.initial['filter_list_status'], notestatus.notestatus_id
        )

    def test_documentation_filter_form_save(self):
        """Test the save method of the documentation filter form"""

        # get user
        test_user = User.objects.get(username='testuser_filter_forms')

        # get user config
        user_config = UserConfigModel.objects.get(
            user_config_username=test_user, filter_view='documentation'
        )

        # get notestatus
        notestatus = Notestatus.objects.create(notestatus_name='test_filter_form_save')

        # get object
        form = DocumentationFilterForm(
            data={
                'filter_list_status': notestatus.notestatus_id,
                'user_config_id': user_config.user_config_id,
            },
            instance=user_config,
        )
        # check if form is valid and save form to database
        self.assertTrue(form.is_valid())
        user_config = form.save(commit=False)
        user_config.save()
        form.save_m2m()

        # compare
        self.assertEqual(user_config.filter_list_status, notestatus)


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
        self.assertEqual(form.fields['filter_list_case'].label, 'Filter for case')

    def test_case_form_empty_label(self):
        """test form label"""

        # get object
        form = GeneralFilterForm()
        # compare
        self.assertEqual(form.fields['filter_list_case'].empty_label, 'Filter for case')

    def test_tag_form_label(self):
        """test form label"""

        # get object
        form = GeneralFilterForm()
        # compare
        self.assertEqual(form.fields['filter_list_tag'].label, 'Filter for tag')

    def test_filter_list_assigned_to_user_id_form_label(self):
        """test form label"""

        # get object
        form = GeneralFilterForm()
        # compare
        self.assertEqual(
            form.fields['filter_list_assigned_to_user_id'].label, 'Filter for user'
        )

    def test_filter_list_assigned_to_user_id_form_empty_label(self):
        """test form label"""

        # get object
        form = GeneralFilterForm()
        # compare
        self.assertEqual(
            form.fields['filter_list_assigned_to_user_id'].empty_label,
            'Filter for user',
        )

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
