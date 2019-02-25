from django.test import TestCase
from dfirtrack_main.models import Company

class CompanyModelTestCase(TestCase):
    """ company model tests """

    @classmethod
    def setUpTestData(cls):

        # create object
        Company.objects.create(company_name='company_1')

    def test_company_string(self):

        # get object
        company_1 = Company.objects.get(company_name='company_1')
        # compare
        self.assertEqual(str(company_1), 'company_1')

    def test_company_name_label(self):

        # get object
        company_1 = Company.objects.get(company_name='company_1')
        # get label
        field_label = company_1._meta.get_field('company_name').verbose_name
        # compare
        self.assertEquals(field_label, 'company name')

    def test_company_note_label(self):

        # get object
        company_1 = Company.objects.get(company_name='company_1')
        # get label
        field_label = company_1._meta.get_field('company_note').verbose_name
        # compare
        self.assertEquals(field_label, 'company note')

    def test_company_division_label(self):

        # get object
        company_1 = Company.objects.get(company_name='company_1')
        # get label
        field_label = company_1._meta.get_field('division').verbose_name
        # compare
        self.assertEquals(field_label, 'division')

    def test_company_name_length(self):

        # get object
        company_1 = Company.objects.get(company_name='company_1')
        # get max length
        max_length = company_1._meta.get_field('company_name').max_length
        # compare
        self.assertEquals(max_length, 50)
