from django.test import TestCase
from dfirtrack_main.models import Os, Osimportname

class OsimportnameModelTestCase(TestCase):
    """ osimportname model tests """

    @classmethod
    def setUpTestData(cls):

        # create object
        os_1 = Os.objects.create(os_name='os_1')
        # create object
        Osimportname.objects.create(osimportname_name='osimportname_1', osimportname_importer='osimportname_importer_1', os = os_1)

    def test_osimportname_string(self):

        # get object
        os_1 = Os.objects.get(os_name='os_1')
        # get object
        osimportname_1 = Osimportname.objects.get(osimportname_name='osimportname_1')
        # compare
        self.assertEqual(str(osimportname_1), 'osimportname_1 (' + str(osimportname_1.os) + ')')

    def test_osimportname_name_label(self):

        # get object
        osimportname_1 = Osimportname.objects.get(osimportname_name='osimportname_1')
        # get label
        field_label = osimportname_1._meta.get_field('osimportname_name').verbose_name
        # compare
        self.assertEquals(field_label, 'osimportname name')

    def test_osimportname_importer_label(self):

        # get object
        osimportname_1 = Osimportname.objects.get(osimportname_name='osimportname_1')
        # get label
        field_label = osimportname_1._meta.get_field('osimportname_importer').verbose_name
        # compare
        self.assertEquals(field_label, 'osimportname importer')

    def test_osimportname_os_label(self):

        # get object
        osimportname_1 = Osimportname.objects.get(osimportname_name='osimportname_1')
        # get label
        field_label = osimportname_1._meta.get_field('os').verbose_name
        # compare
        self.assertEquals(field_label, 'os')

    def test_osimportname_name_length(self):

        # get object
        osimportname_1 = Osimportname.objects.get(osimportname_name='osimportname_1')
        # get max length
        max_length = osimportname_1._meta.get_field('osimportname_name').max_length
        # compare
        self.assertEquals(max_length, 30)

    def test_osimportname_importer_length(self):

        # get object
        osimportname_1 = Osimportname.objects.get(osimportname_importer='osimportname_importer_1')
        # get max length
        max_length = osimportname_1._meta.get_field('osimportname_importer').max_length
        # compare
        self.assertEquals(max_length, 30)
