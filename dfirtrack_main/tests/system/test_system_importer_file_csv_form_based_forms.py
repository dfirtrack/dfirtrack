from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from dfirtrack_main.importer.file.csv_importer_forms import SystemImporterFileCsvFormbasedForm
from dfirtrack_main.models import Analysisstatus, Case, Company, Dnsname, Domain, Location, Os, Reason, Serviceprovider, Systemstatus, Systemtype, Tag, Tagcolor

class SystemImporterFileCsvFormbasedFormbasedFormTestCase(TestCase):
    """ system importer file CSV form-based form tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_system_importer_file_csv_config_based', password='kBCV4spAtkHqcmejUBgt')

        # create object
        Systemstatus.objects.create(systemstatus_name='systemstatus_1')

        # create object
        Analysisstatus.objects.create(analysisstatus_name='analysisstatus_1')

        # create object
        Reason.objects.create(reason_name='reason_1')

        # create object
        Systemtype.objects.create(systemtype_name='systemtype_1')

        # create object
        Domain.objects.create(domain_name='domain_1')

        # create object
        Dnsname.objects.create(dnsname_name='dnsname_1')

        # create object
        Os.objects.create(os_name='os_1')

        # create object
        Company.objects.create(company_name='company_1')
        Company.objects.create(company_name='company_2')

        # create object
        Location.objects.create(location_name='location_1')

        # create object
        Serviceprovider.objects.create(serviceprovider_name='serviceprovider_1')

        # create object
        tagcolor_1 = Tagcolor.objects.create(tagcolor_name='tagcolor_1')

        # create object
        Tag.objects.create(
            tag_name = 'tag_1',
            tagcolor = tagcolor_1,
        )
        Tag.objects.create(
            tag_name = 'tag_2',
            tagcolor = tagcolor_1,
        )

        # create object
        Case.objects.create(
            case_name = 'case_1',
            case_is_incident = True,
            case_created_by_user_id = test_user,
        )
        Case.objects.create(
            case_name = 'case_2',
            case_is_incident = True,
            case_created_by_user_id = test_user,
        )


    def test_system_importer_file_csv_form_based_systemcsv_form_label(self):
        """ test form label """

        # get object
        form = SystemImporterFileCsvFormbasedForm()
        # compare
        self.assertEqual(form.fields['systemcsv'].label, 'CSV with systems (*)')

    def test_system_importer_file_csv_form_based_systemstatus_form_label(self):
        """ test form label """

        # get object
        form = SystemImporterFileCsvFormbasedForm()
        # compare
        self.assertEqual(form.fields['systemstatus'].label, 'Systemstatus (*)')

    def test_system_importer_file_csv_form_based_analysisstatus_form_label(self):
        """ test form label """

        # get object
        form = SystemImporterFileCsvFormbasedForm()
        # compare
        self.assertEqual(form.fields['analysisstatus'].label, 'Analysisstatus')

    def test_system_importer_file_csv_form_based_reason_form_label(self):
        """ test form label """

        # get object
        form = SystemImporterFileCsvFormbasedForm()
        # compare
        self.assertEqual(form.fields['reason'].label, 'Reason for investigation')

    def test_system_importer_file_csv_form_based_domain_form_label(self):
        """ test form label """

        # get object
        form = SystemImporterFileCsvFormbasedForm()
        # compare
        self.assertEqual(form.fields['domain'].label, 'Domain')

    def test_system_importer_file_csv_form_based_dnsname_form_label(self):
        """ test form label """

        # get object
        form = SystemImporterFileCsvFormbasedForm()
        # compare
        self.assertEqual(form.fields['dnsname'].label, 'DNS name')

    def test_system_importer_file_csv_form_based_systemtype_form_label(self):
        """ test form label """

        # get object
        form = SystemImporterFileCsvFormbasedForm()
        # compare
        self.assertEqual(form.fields['systemtype'].label, 'Systemtype')

    def test_system_importer_file_csv_form_based_os_form_label(self):
        """ test form label """

        # get object
        form = SystemImporterFileCsvFormbasedForm()
        # compare
        self.assertEqual(form.fields['os'].label, 'Os')

    def test_system_importer_file_csv_form_based_location_form_label(self):
        """ test form label """

        # get object
        form = SystemImporterFileCsvFormbasedForm()
        # compare
        self.assertEqual(form.fields['location'].label, 'Location')

    def test_system_importer_file_csv_form_based_serviceprovider_form_label(self):
        """ test form label """

        # get object
        form = SystemImporterFileCsvFormbasedForm()
        # compare
        self.assertEqual(form.fields['serviceprovider'].label, 'Serviceprovider')

    def test_system_importer_file_csv_form_based_case_form_label(self):
        """ test form label """

        # get object
        form = SystemImporterFileCsvFormbasedForm()
        # compare
        self.assertEqual(form.fields['case'].label, 'Cases')

    def test_system_importer_file_csv_form_based_company_form_label(self):
        """ test form label """

        # get object
        form = SystemImporterFileCsvFormbasedForm()
        # compare
        self.assertEqual(form.fields['company'].label, 'Companies')

    def test_system_importer_file_csv_form_based_tag_form_label(self):
        """ test form label """

        # get object
        form = SystemImporterFileCsvFormbasedForm()
        # compare
        self.assertEqual(form.fields['tag'].label, 'Tags')

    def test_system_importer_file_csv_form_based_form_empty(self):
        """ test minimum form requirements / INVALID """

        # get object
        form = SystemImporterFileCsvFormbasedForm(data = {})
        # compare
        self.assertFalse(form.is_valid())

    def test_system_importer_file_csv_form_based_systemcsv_form_filled(self):
        """ test minimum form requirements / INVALID """

        # get file
        upload_csv = open('example_data/dfirtrack_main_importer_file_csv_system__valid.csv', 'rb')
        # create dictionaries
        data_dict = {}
        file_dict = {
            'systemcsv': SimpleUploadedFile(upload_csv.name, upload_csv.read()),
        }
        # get object
        form = SystemImporterFileCsvFormbasedForm(
            data = data_dict,
            files = file_dict,
        )
        # close file
        upload_csv.close()
        # compare
        self.assertFalse(form.is_valid())

    def test_system_importer_file_csv_form_based_systemstatus_form_filled(self):
        """ test minimum form requirements / VALID """

        # get object
        systemstatus_id = Systemstatus.objects.get(systemstatus_name='systemstatus_1').systemstatus_id
        # get file
        upload_csv = open('example_data/dfirtrack_main_importer_file_csv_system__valid.csv', 'rb')
        # create dictionaries
        data_dict = {
            'systemstatus': systemstatus_id,
        }
        file_dict = {
            'systemcsv': SimpleUploadedFile(upload_csv.name, upload_csv.read()),
        }
        # get object
        form = SystemImporterFileCsvFormbasedForm(
            data = data_dict,
            files = file_dict,
        )
        # close file
        upload_csv.close()
        # compare
        self.assertTrue(form.is_valid())

    def test_system_importer_file_csv_form_based_analysisstatus_form_filled(self):
        """ test additional form content """

        # get object
        systemstatus_id = Systemstatus.objects.get(systemstatus_name='systemstatus_1').systemstatus_id
        # get object
        analysisstatus_id = Analysisstatus.objects.get(analysisstatus_name='analysisstatus_1').analysisstatus_id
        # get file
        upload_csv = open('example_data/dfirtrack_main_importer_file_csv_system__valid.csv', 'rb')
        # create dictionaries
        data_dict = {
            'systemstatus': systemstatus_id,
            'analysisstatus': analysisstatus_id,
        }
        file_dict = {
            'systemcsv': SimpleUploadedFile(upload_csv.name, upload_csv.read()),
        }
        # get object
        form = SystemImporterFileCsvFormbasedForm(
            data = data_dict,
            files = file_dict,
        )
        # close file
        upload_csv.close()
        # compare
        self.assertTrue(form.is_valid())

    def test_system_importer_file_csv_form_based_reason_form_filled(self):
        """ test additional form content """

        # get object
        systemstatus_id = Systemstatus.objects.get(systemstatus_name='systemstatus_1').systemstatus_id
        # get object
        reason_id = Reason.objects.get(reason_name='reason_1').reason_id
        # get file
        upload_csv = open('example_data/dfirtrack_main_importer_file_csv_system__valid.csv', 'rb')
        # create dictionaries
        data_dict = {
            'systemstatus': systemstatus_id,
            'reason': reason_id,
        }
        file_dict = {
            'systemcsv': SimpleUploadedFile(upload_csv.name, upload_csv.read()),
        }
        # get object
        form = SystemImporterFileCsvFormbasedForm(
            data = data_dict,
            files = file_dict,
        )
        # close file
        upload_csv.close()
        # compare
        self.assertTrue(form.is_valid())

    def test_system_importer_file_csv_form_based_domain_form_filled(self):
        """ test additional form content """

        # get object
        systemstatus_id = Systemstatus.objects.get(systemstatus_name='systemstatus_1').systemstatus_id
        # get object
        domain_id = Domain.objects.get(domain_name='domain_1').domain_id
        # get file
        upload_csv = open('example_data/dfirtrack_main_importer_file_csv_system__valid.csv', 'rb')
        # create dictionaries
        data_dict = {
            'systemstatus': systemstatus_id,
            'domain': domain_id,
        }
        file_dict = {
            'systemcsv': SimpleUploadedFile(upload_csv.name, upload_csv.read()),
        }
        # get object
        form = SystemImporterFileCsvFormbasedForm(
            data = data_dict,
            files = file_dict,
        )
        # close file
        upload_csv.close()
        # compare
        self.assertTrue(form.is_valid())

    def test_system_importer_file_csv_form_based_dnsname_form_filled(self):
        """ test additional form content """

        # get object
        systemstatus_id = Systemstatus.objects.get(systemstatus_name='systemstatus_1').systemstatus_id
        # get object
        dnsname_id = Dnsname.objects.get(dnsname_name='dnsname_1').dnsname_id
        # get file
        upload_csv = open('example_data/dfirtrack_main_importer_file_csv_system__valid.csv', 'rb')
        # create dictionaries
        data_dict = {
            'systemstatus': systemstatus_id,
            'dnsname': dnsname_id,
        }
        file_dict = {
            'systemcsv': SimpleUploadedFile(upload_csv.name, upload_csv.read()),
        }
        # get object
        form = SystemImporterFileCsvFormbasedForm(
            data = data_dict,
            files = file_dict,
        )
        # close file
        upload_csv.close()
        # compare
        self.assertTrue(form.is_valid())

    def test_system_importer_file_csv_form_based_systemtype_form_filled(self):
        """ test additional form content """

        # get object
        systemstatus_id = Systemstatus.objects.get(systemstatus_name='systemstatus_1').systemstatus_id
        # get object
        systemtype_id = Systemtype.objects.get(systemtype_name='systemtype_1').systemtype_id
        # get file
        upload_csv = open('example_data/dfirtrack_main_importer_file_csv_system__valid.csv', 'rb')
        # create dictionaries
        data_dict = {
            'systemstatus': systemstatus_id,
            'systemtype': systemtype_id,
        }
        file_dict = {
            'systemcsv': SimpleUploadedFile(upload_csv.name, upload_csv.read()),
        }
        # get object
        form = SystemImporterFileCsvFormbasedForm(
            data = data_dict,
            files = file_dict,
        )
        # close file
        upload_csv.close()
        # compare
        self.assertTrue(form.is_valid())

    def test_system_importer_file_csv_form_based_os_form_filled(self):
        """ test additional form content """

        # get object
        systemstatus_id = Systemstatus.objects.get(systemstatus_name='systemstatus_1').systemstatus_id
        # get object
        os_id = Os.objects.get(os_name='os_1').os_id
        # get file
        upload_csv = open('example_data/dfirtrack_main_importer_file_csv_system__valid.csv', 'rb')
        # create dictionaries
        data_dict = {
            'systemstatus': systemstatus_id,
            'os': os_id,
        }
        file_dict = {
            'systemcsv': SimpleUploadedFile(upload_csv.name, upload_csv.read()),
        }
        # get object
        form = SystemImporterFileCsvFormbasedForm(
            data = data_dict,
            files = file_dict,
        )
        # close file
        upload_csv.close()
        # compare
        self.assertTrue(form.is_valid())

    def test_system_importer_file_csv_form_based_location_form_filled(self):
        """ test additional form content """

        # get object
        systemstatus_id = Systemstatus.objects.get(systemstatus_name='systemstatus_1').systemstatus_id
        # get object
        location_id = Location.objects.get(location_name='location_1').location_id
        # get file
        upload_csv = open('example_data/dfirtrack_main_importer_file_csv_system__valid.csv', 'rb')
        # create dictionaries
        data_dict = {
            'systemstatus': systemstatus_id,
            'location': location_id,
        }
        file_dict = {
            'systemcsv': SimpleUploadedFile(upload_csv.name, upload_csv.read()),
        }
        # get object
        form = SystemImporterFileCsvFormbasedForm(
            data = data_dict,
            files = file_dict,
        )
        # close file
        upload_csv.close()
        # compare
        self.assertTrue(form.is_valid())

    def test_system_importer_file_csv_form_based_serviceprovider_form_filled(self):
        """ test additional form content """

        # get object
        systemstatus_id = Systemstatus.objects.get(systemstatus_name='systemstatus_1').systemstatus_id
        # get object
        serviceprovider_id = Serviceprovider.objects.get(serviceprovider_name='serviceprovider_1').serviceprovider_id
        # get file
        upload_csv = open('example_data/dfirtrack_main_importer_file_csv_system__valid.csv', 'rb')
        # create dictionaries
        data_dict = {
            'systemstatus': systemstatus_id,
            'serviceprovider': serviceprovider_id,
        }
        file_dict = {
            'systemcsv': SimpleUploadedFile(upload_csv.name, upload_csv.read()),
        }
        # get object
        form = SystemImporterFileCsvFormbasedForm(
            data = data_dict,
            files = file_dict,
        )
        # close file
        upload_csv.close()
        # compare
        self.assertTrue(form.is_valid())

    def test_system_importer_file_csv_form_based_company_form_filled(self):
        """ test additional form content """

        # get object
        systemstatus_id = Systemstatus.objects.get(systemstatus_name='systemstatus_1').systemstatus_id
        # get object
        company_1_id = Company.objects.get(company_name='company_1').company_id
        company_2_id = Company.objects.get(company_name='company_2').company_id
        # get file
        upload_csv = open('example_data/dfirtrack_main_importer_file_csv_system__valid.csv', 'rb')
        # create dictionaries
        data_dict = {
            'systemstatus': systemstatus_id,
            'company': [company_1_id, company_2_id],
        }
        file_dict = {
            'systemcsv': SimpleUploadedFile(upload_csv.name, upload_csv.read()),
        }
        # get object
        form = SystemImporterFileCsvFormbasedForm(
            data = data_dict,
            files = file_dict,
        )
        # close file
        upload_csv.close()
        # compare
        self.assertTrue(form.is_valid())

    def test_system_importer_file_csv_form_based_tag_form_filled(self):
        """ test additional form content """

        # get object
        systemstatus_id = Systemstatus.objects.get(systemstatus_name='systemstatus_1').systemstatus_id
        # get object
        tag_1_id = Tag.objects.get(tag_name='tag_1').tag_id
        tag_2_id = Tag.objects.get(tag_name='tag_2').tag_id
        # get file
        upload_csv = open('example_data/dfirtrack_main_importer_file_csv_system__valid.csv', 'rb')
        # create dictionaries
        data_dict = {
            'systemstatus': systemstatus_id,
            'tag': [tag_1_id, tag_2_id],
        }
        file_dict = {
            'systemcsv': SimpleUploadedFile(upload_csv.name, upload_csv.read()),
        }
        # get object
        form = SystemImporterFileCsvFormbasedForm(
            data = data_dict,
            files = file_dict,
        )
        # close file
        upload_csv.close()
        # compare
        self.assertTrue(form.is_valid())

    def test_system_importer_file_csv_form_based_case_form_filled(self):
        """ test additional form content """

        # get object
        systemstatus_id = Systemstatus.objects.get(systemstatus_name='systemstatus_1').systemstatus_id
        # get object
        case_1_id = Case.objects.get(case_name='case_1').case_id
        case_2_id = Case.objects.get(case_name='case_2').case_id
        # get file
        upload_csv = open('example_data/dfirtrack_main_importer_file_csv_system__valid.csv', 'rb')
        # create dictionaries
        data_dict = {
            'systemstatus': systemstatus_id,
            'case': [case_1_id, case_2_id],
        }
        file_dict = {
            'systemcsv': SimpleUploadedFile(upload_csv.name, upload_csv.read()),
        }
        # get object
        form = SystemImporterFileCsvFormbasedForm(
            data = data_dict,
            files = file_dict,
        )
        # close file
        upload_csv.close()
        # compare
        self.assertTrue(form.is_valid())
