from django.test import TestCase
from dfirtrack_main.forms import CompanyForm
from dfirtrack_main.models import Division

class CompanyFormTestCase(TestCase):
    """ company form tests """

    def test_company_name_label(self):

        # get object
        form = CompanyForm()
        # compare
        self.assertEquals(form.fields['company_name'].label, 'Company name (*)')

    def test_company_note_label(self):

        # get object
        form = CompanyForm()
        # compare
        self.assertEquals(form.fields['company_note'].label, 'Company note')

    def test_company_name_empty(self):

        # get object
        form = CompanyForm(data = {'company_name': ''})
        # compare
        self.assertFalse(form.is_valid())

    def test_company_name_filled(self):

        # get object
        form = CompanyForm(data = {'company_name': 'company_1'})
        # compare
        self.assertTrue(form.is_valid())

    def test_company_name_filled_with_division(self):

        # create foreign key object
        Division.objects.create(division_name='division_1')
        # get foreign key object id
        division_id = Division.objects.get(division_name='division_1').division_id
        # get object
        form = CompanyForm(data = {'company_name': 'company_1', 'division': division_id})
        # compare
        self.assertTrue(form.is_valid())
