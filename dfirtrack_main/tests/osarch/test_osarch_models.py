from django.test import TestCase
from dfirtrack_main.models import Osarch

class OsarchModelTestCase(TestCase):
    """ osarch model tests """

    @classmethod
    def setUpTestData(cls):

        # create object
        Osarch.objects.create(osarch_name='osarch_1')

    def test_osarch_string(self):

        # get object
        osarch_1 = Osarch.objects.get(osarch_name='osarch_1')
        # compare
        self.assertEqual(str(osarch_1), 'osarch_1')

    def test_osarch_name_label(self):

        # get object
        osarch_1 = Osarch.objects.get(osarch_name='osarch_1')
        # get label
        field_label = osarch_1._meta.get_field('osarch_name').verbose_name
        # compare
        self.assertEquals(field_label, 'osarch name')

    def test_osarch_name_length(self):

        # get object
        osarch_1 = Osarch.objects.get(osarch_name='osarch_1')
        # get max length
        max_length = osarch_1._meta.get_field('osarch_name').max_length
        # compare
        self.assertEquals(max_length, 10)
