from django.test import TestCase
from dfirtrack_main.models import Domain

class DomainModelTestCase(TestCase):
    """ domain model tests """

    @classmethod
    def setUpTestData(cls):

        # create object
        Domain.objects.create(domain_name='domain_1', domain_note='lorem ipsum')

    def test_domain_string(self):

        # get object
        domain_1 = Domain.objects.get(domain_name='domain_1')
        # compare
        self.assertEqual(str(domain_1), 'domain_1')

    def test_domain_name_label(self):

        # get object
        domain_1 = Domain.objects.get(domain_name='domain_1')
        # get label
        field_label = domain_1._meta.get_field('domain_name').verbose_name
        # compare
        self.assertEquals(field_label, 'domain name')

    def test_domain_note_label(self):

        # get object
        domain_1 = Domain.objects.get(domain_name='domain_1')
        # get label
        field_label = domain_1._meta.get_field('domain_note').verbose_name
        # compare
        self.assertEquals(field_label, 'domain note')

    def test_domain_name_length(self):

        # get object
        domain_1 = Domain.objects.get(domain_name='domain_1')
        # get max length
        max_length = domain_1._meta.get_field('domain_name').max_length
        # compare
        self.assertEquals(max_length, 100)
