from django.test import TestCase
from dfirtrack_main.models import Serviceprovider

class ServiceproviderModelTestCase(TestCase):
    """ serviceprovider model tests """

    @classmethod
    def setUpTestData(cls):

        # create object
        Serviceprovider.objects.create(serviceprovider_name='serviceprovider_1', serviceprovider_note='lorem ipsum')

    def test_serviceprovider_string(self):

        # get object
        serviceprovider_1 = Serviceprovider.objects.get(serviceprovider_name='serviceprovider_1')
        # compare
        self.assertEqual(str(serviceprovider_1), 'serviceprovider_1')

    def test_serviceprovider_name_label(self):

        # get object
        serviceprovider_1 = Serviceprovider.objects.get(serviceprovider_name='serviceprovider_1')
        # get label
        field_label = serviceprovider_1._meta.get_field('serviceprovider_name').verbose_name
        # compare
        self.assertEquals(field_label, 'serviceprovider name')

    def test_serviceprovider_note_label(self):

        # get object
        serviceprovider_1 = Serviceprovider.objects.get(serviceprovider_name='serviceprovider_1')
        # get label
        field_label = serviceprovider_1._meta.get_field('serviceprovider_note').verbose_name
        # compare
        self.assertEquals(field_label, 'serviceprovider note')

    def test_serviceprovider_name_length(self):

        # get object
        serviceprovider_1 = Serviceprovider.objects.get(serviceprovider_name='serviceprovider_1')
        # get max length
        max_length = serviceprovider_1._meta.get_field('serviceprovider_name').max_length
        # compare
        self.assertEquals(max_length, 50)
