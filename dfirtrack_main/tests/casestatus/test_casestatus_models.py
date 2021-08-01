from django.test import TestCase

from dfirtrack_main.models import Casestatus


class CasestatusModelTestCase(TestCase):
    """casestatus model tests"""

    @classmethod
    def setUpTestData(cls):

        # create object
        Casestatus.objects.create(casestatus_name="casestatus_1")

    def test_casestatus_string(self):
        """test string representation"""

        # get object
        casestatus_1 = Casestatus.objects.get(casestatus_name="casestatus_1")
        # compare
        self.assertEqual(str(casestatus_1), "casestatus_1")

    def test_casestatus_verbose_name_plural(self):
        """test string representation"""

        # get object
        casestatus_1 = Casestatus.objects.get(casestatus_name="casestatus_1")
        # compare
        self.assertEqual(casestatus_1._meta.verbose_name_plural, "casestatus")

    def test_casestatus_id_attribute_label(self):
        """test attribute label"""

        # get object
        casestatus_1 = Casestatus.objects.get(casestatus_name="casestatus_1")
        # get label
        field_label = casestatus_1._meta.get_field("casestatus_id").verbose_name
        # compare
        self.assertEqual(field_label, "casestatus id")

    def test_casestatus_name_attribute_label(self):
        """test attribute label"""

        # get object
        casestatus_1 = Casestatus.objects.get(casestatus_name="casestatus_1")
        # get label
        field_label = casestatus_1._meta.get_field("casestatus_name").verbose_name
        # compare
        self.assertEqual(field_label, "casestatus name")

    def test_casestatus_note_attribute_label(self):
        """test attribute label"""

        # get object
        casestatus_1 = Casestatus.objects.get(casestatus_name="casestatus_1")
        # get label
        field_label = casestatus_1._meta.get_field("casestatus_note").verbose_name
        # compare
        self.assertEqual(field_label, "casestatus note")

    def test_casestatus_slug_attribute_label(self):
        """test attribute label"""

        # get object
        casestatus_1 = Casestatus.objects.get(casestatus_name="casestatus_1")
        # get label
        field_label = casestatus_1._meta.get_field("casestatus_slug").verbose_name
        # compare
        self.assertEqual(field_label, "casestatus slug")

    def test_casestatus_name_length(self):
        """test for max length"""

        # get object
        casestatus_1 = Casestatus.objects.get(casestatus_name="casestatus_1")
        # get max length
        max_length = casestatus_1._meta.get_field("casestatus_name").max_length
        # compare
        self.assertEqual(max_length, 255)

    def test_casestatus_slug_length(self):
        """test for max length"""

        # get object
        casestatus_1 = Casestatus.objects.get(casestatus_name="casestatus_1")
        # get max length
        max_length = casestatus_1._meta.get_field("casestatus_slug").max_length
        # compare
        self.assertEqual(max_length, 255)
