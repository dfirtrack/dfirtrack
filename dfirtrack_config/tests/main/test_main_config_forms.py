from django.test import TestCase
from dfirtrack_artifacts.models import Artifactstatus
from dfirtrack_main.models import Casestatus
from dfirtrack_config.forms import MainConfigForm

class MainConfigFormTestCase(TestCase):
    """ main config form tests """

    @classmethod
    def setUpTestData(cls):

        pass

    def test_main_config_system_name_editable_form_label(self):
        """ test form label """

        # get object
        form = MainConfigForm()
        # compare
        self.assertEqual(form.fields['system_name_editable'].label, 'Make system name editable (may require service restart)')

    def test_main_config_main_overview_form_label(self):
        """ test form label """

        # get object
        form = MainConfigForm()
        # compare
        self.assertEqual(form.fields['main_overview'].label, 'Main overview page')

    def test_main_config_artifactstatus_form_label(self):
        """ test form label """

        # get object
        form = MainConfigForm()
        # compare
        self.assertEqual(form.fields['artifactstatus_open'].label, 'Artifactstatus to be considered open')
        self.assertEqual(form.fields['artifactstatus_requested'].label, 'Artifactstatus setting the artifact requested time')
        self.assertEqual(form.fields['artifactstatus_acquisition'].label, 'Artifactstatus setting the artifact acquisition time')

    def test_main_config_casestatus_form_label(self):
        """ test form label """

        # get object
        form = MainConfigForm()
        # compare
        self.assertEqual(form.fields['casestatus_open'].label, 'Casestatus to be considered open')
        self.assertEqual(form.fields['casestatus_start'].label, 'Casestatus setting the case start time')
        self.assertEqual(form.fields['casestatus_end'].label, 'Casestatus setting the case end time')

    def test_main_config_statushistory_entry_numbers_form_label(self):
        """ test form label """

        # get object
        form = MainConfigForm()
        # compare
        self.assertEqual(form.fields['statushistory_entry_numbers'].label, 'Show only this number of last statushistory entries')

    def test_main_config_cron_form_label(self):
        """ test form label """

        # get object
        form = MainConfigForm()
        # compare
        self.assertEqual(form.fields['cron_export_path'].label, 'Export files created by scheduled tasks to this path')
        self.assertEqual(form.fields['cron_username'].label, 'Use this username for scheduled tasks (just for logging, does not have to exist)')

    def test_main_config_form_empty(self):
        """ test minimum form requirements / INVALID """

        # get object
        form = MainConfigForm(data = {
            'cron_export_path': '/tmp',
        })
        # compare
        self.assertFalse(form.is_valid())

    def test_main_config_form_statushistory_entry_numbers_filled(self):
        """ test minimum form requirements / INVALID """

        # get object
        form = MainConfigForm(data = {
            'statushistory_entry_numbers': 9,
            'cron_export_path': '/tmp',
        })
        # compare
        self.assertFalse(form.is_valid())

    def test_main_config_form_cron_export_path_filled(self):
        """ test minimum form requirements / INVALID """

        # get object
        form = MainConfigForm(data = {
            'statushistory_entry_numbers': 8,
            'cron_export_path': '/tmp',
        })
        # compare
        self.assertFalse(form.is_valid())

    def test_main_config_form_cron_username_filled(self):
        """ test minimum form requirements / INVALID """

        # get object
        form = MainConfigForm(data = {
            'statushistory_entry_numbers': 7,
            'cron_export_path': '/tmp',
            'cron_username': 'cron',
        })
        # compare
        self.assertFalse(form.is_valid())

    def test_main_config_form_main_overview_filled(self):
        """ test minimum form requirements / VALID """

        # get object
        form = MainConfigForm(data = {
            'statushistory_entry_numbers': 6,
            'cron_export_path': '/tmp',
            'cron_username': 'cron',
            'main_overview': 'main_overview_system',
        })
        # compare
        self.assertTrue(form.is_valid())

    def test_main_config_form_different_artifactstatus(self):
        """ test custom field validation """

        # create obects
        artifactstatus_1 = Artifactstatus.objects.create(artifactstatus_name='artifactstatus_1').artifactstatus_id
        artifactstatus_2 = Artifactstatus.objects.create(artifactstatus_name='artifactstatus_2').artifactstatus_id
        artifactstatus_3 = Artifactstatus.objects.create(artifactstatus_name='artifactstatus_3').artifactstatus_id
        artifactstatus_4 = Artifactstatus.objects.create(artifactstatus_name='artifactstatus_4').artifactstatus_id
        artifactstatus_5 = Artifactstatus.objects.create(artifactstatus_name='artifactstatus_5').artifactstatus_id
        artifactstatus_6 = Artifactstatus.objects.create(artifactstatus_name='artifactstatus_6').artifactstatus_id
        # get object
        form = MainConfigForm(data = {
            'statushistory_entry_numbers': 5,
            'cron_export_path': '/tmp',
            'cron_username': 'cron',
            'main_overview': 'main_overview_system',
            'artifactstatus_requested': [artifactstatus_1, artifactstatus_2, artifactstatus_3,],
            'artifactstatus_acquisition': [artifactstatus_4, artifactstatus_5, artifactstatus_6,],
        })
        # compare
        self.assertTrue(form.is_valid())

    def test_main_config_form_same_artifactstatus(self):
        """ test custom field validation """

        # create obects
        artifactstatus_1 = Artifactstatus.objects.create(artifactstatus_name='artifactstatus_1').artifactstatus_id
        artifactstatus_2 = Artifactstatus.objects.create(artifactstatus_name='artifactstatus_2').artifactstatus_id
        artifactstatus_3 = Artifactstatus.objects.create(artifactstatus_name='artifactstatus_3').artifactstatus_id
        artifactstatus_4 = Artifactstatus.objects.create(artifactstatus_name='artifactstatus_4').artifactstatus_id
        artifactstatus_5 = Artifactstatus.objects.create(artifactstatus_name='artifactstatus_5').artifactstatus_id
        # get object
        form = MainConfigForm(data = {
            'statushistory_entry_numbers': 4,
            'cron_export_path': '/tmp',
            'cron_username': 'cron',
            'main_overview': 'main_overview_system',
            'artifactstatus_requested': [artifactstatus_1, artifactstatus_2, artifactstatus_3,],
            'artifactstatus_acquisition': [artifactstatus_3, artifactstatus_4, artifactstatus_5,],
        })
        # compare
        self.assertFalse(form.is_valid())

    def test_main_config_form_different_casestatus(self):
        """ test custom field validation """

        # create obects
        casestatus_1 = Casestatus.objects.create(casestatus_name='casestatus_1').casestatus_id
        casestatus_2 = Casestatus.objects.create(casestatus_name='casestatus_2').casestatus_id
        casestatus_3 = Casestatus.objects.create(casestatus_name='casestatus_3').casestatus_id
        casestatus_4 = Casestatus.objects.create(casestatus_name='casestatus_4').casestatus_id
        casestatus_5 = Casestatus.objects.create(casestatus_name='casestatus_5').casestatus_id
        casestatus_6 = Casestatus.objects.create(casestatus_name='casestatus_6').casestatus_id
        # get object
        form = MainConfigForm(data = {
            'statushistory_entry_numbers': 3,
            'cron_export_path': '/tmp',
            'cron_username': 'cron',
            'main_overview': 'main_overview_system',
            'casestatus_start': [casestatus_1, casestatus_2, casestatus_3,],
            'casestatus_end': [casestatus_4, casestatus_5, casestatus_6,],
        })
        # compare
        self.assertTrue(form.is_valid())

    def test_main_config_form_same_casestatus(self):
        """ test custom field validation """

        # create obects
        casestatus_1 = Casestatus.objects.create(casestatus_name='casestatus_1').casestatus_id
        casestatus_2 = Casestatus.objects.create(casestatus_name='casestatus_2').casestatus_id
        casestatus_3 = Casestatus.objects.create(casestatus_name='casestatus_3').casestatus_id
        casestatus_4 = Casestatus.objects.create(casestatus_name='casestatus_4').casestatus_id
        casestatus_5 = Casestatus.objects.create(casestatus_name='casestatus_5').casestatus_id
        # get object
        form = MainConfigForm(data = {
            'statushistory_entry_numbers': 2,
            'cron_export_path': '/tmp',
            'cron_username': 'cron',
            'main_overview': 'main_overview_system',
            'casestatus_start': [casestatus_1, casestatus_2, casestatus_3,],
            'casestatus_end': [casestatus_3, casestatus_4, casestatus_5,],
        })
        # compare
        self.assertFalse(form.is_valid())
