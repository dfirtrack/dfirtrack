from django.test import TestCase
from dfirtrack_main.models import Systemstatus

class SystemstatusModelTestCase(TestCase):
    """ systemstatus model tests """

    @classmethod
    def setUpTestData(cls):

        # create object
        Systemstatus.objects.create(systemstatus_name='systemstatus_1')

    def test_systemstatus_string(self):

        # get object
        systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')
        # compare
        self.assertEqual(str(systemstatus_1), 'systemstatus_1')

    def test_systemstatus_name_label(self):

        # get object
        systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')
        # get label
        field_label = systemstatus_1._meta.get_field('systemstatus_name').verbose_name
        # compare
        self.assertEquals(field_label, 'systemstatus name')

    def test_systemstatus_note_label(self):

        # get object
        systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')
        # get label
        field_label = systemstatus_1._meta.get_field('systemstatus_note').verbose_name
        # compare
        self.assertEquals(field_label, 'systemstatus note')

    def test_systemstatus_name_length(self):

        # get object
        systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')
        # get max length
        max_length = systemstatus_1._meta.get_field('systemstatus_name').max_length
        # compare
        self.assertEquals(max_length, 30)
