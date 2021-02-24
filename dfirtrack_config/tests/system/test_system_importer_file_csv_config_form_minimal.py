from django.contrib.auth.models import User
from django.test import TestCase
from dfirtrack_config.forms import SystemImporterFileCsvConfigForm
from dfirtrack_main.models import Analysisstatus, Systemstatus


class SystemImporterFileCsvConfigFormMinimalTestCase(TestCase):
    """ system importer file CSV config form tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        User.objects.create_user(username='testuser_system_importer_file_csv_config', password='j1mNhkDDrKC57triHZTE')

        # create objects
        Analysisstatus.objects.create(analysisstatus_name = 'analysisstatus_1')
        Systemstatus.objects.create(systemstatus_name = 'systemstatus_1')

    def test_system_importer_file_csv_config_form_minimal(self):
        """ test minimum form requirements / VALID """

        # TODO: [maintenance] remove form fields

        # get user
        testuser = User.objects.get(username='testuser_system_importer_file_csv_config').id
        # get objects
        analysisstatus_1 = Analysisstatus.objects.get(analysisstatus_name = 'analysisstatus_1').analysisstatus_id
        systemstatus_1 = Systemstatus.objects.get(systemstatus_name = 'systemstatus_1').systemstatus_id
        # get form
        form = SystemImporterFileCsvConfigForm(data = {
            'csv_column_system': '1',
#            'csv_skip_existing_system',
#            'csv_headline',
            'csv_import_path': '/tmp',
            'csv_import_filename': 'systems.csv',
            'csv_import_username': str(testuser),
            'csv_default_systemstatus': str(systemstatus_1),
#            'csv_remove_systemstatus',
            'csv_default_analysisstatus': str(analysisstatus_1),
#            'csv_remove_analysisstatus',
#            'csv_choice_tagfree_systemstatus',
            'csv_default_tagfree_systemstatus': str(systemstatus_1),
#            'csv_choice_tagfree_analysisstatus',
            'csv_default_tagfree_analysisstatus': str(analysisstatus_1),
            'csv_tag_lock_systemstatus': 'LOCK_SYSTEMSTATUS',
            'csv_tag_lock_analysisstatus': 'LOCK_ANALYSISSTATUS',
#            'csv_choice_ip',
#            'csv_column_ip',
#            'csv_remove_ip',
#            'csv_choice_dnsname',
#            'csv_column_dnsname',
#            'csv_default_dnsname',
#            'csv_remove_dnsname',
#            'csv_choice_domain',
#            'csv_column_domain',
#            'csv_default_domain',
#            'csv_remove_domain',
#            'csv_choice_location',
#            'csv_column_location',
#            'csv_default_location',
#            'csv_remove_location',
#            'csv_choice_os',
#            'csv_column_os',
#            'csv_default_os',
#            'csv_remove_os',
#            'csv_choice_reason',
#            'csv_column_reason',
#            'csv_default_reason',
#            'csv_remove_reason',
#            'csv_choice_recommendation',
#            'csv_column_recommendation',
#            'csv_default_recommendation',
#            'csv_remove_recommendation',
#            'csv_choice_serviceprovider',
#            'csv_column_serviceprovider',
#            'csv_default_serviceprovider',
#            'csv_remove_serviceprovider',
#            'csv_choice_systemtype',
#            'csv_column_systemtype',
#            'csv_default_systemtype',
#            'csv_remove_systemtype',
#            'csv_choice_case',
#            'csv_column_case',
#            'csv_default_case',
#            'csv_remove_case',
#            'csv_choice_company',
#            'csv_column_company',
#            'csv_default_company',
#            'csv_remove_company',
#            'csv_choice_tag',
#            'csv_column_tag',
#            'csv_default_tag',
            'csv_remove_tag': 'tag_remove_prefix',
#            'csv_tag_prefix',
#            'csv_tag_prefix_delimiter',
            'csv_field_delimiter': 'field_comma',
            'csv_text_quote': 'text_double_quotation_marks',
            'csv_ip_delimiter': 'ip_semicolon',
            'csv_tag_delimiter': 'tag_space',
        })
        # compare
        self.assertTrue(form.is_valid())
