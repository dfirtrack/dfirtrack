from django.test import TestCase
from dfirtrack_main.models import Ip

class IpModelTestCase(TestCase):
    """ ip model tests """

    @classmethod
    def setUpTestData(cls):

        # create object
        Ip.objects.create(ip_ip='127.0.0.1')

    def test_ip_string(self):

        # get object
        ip_1 = Ip.objects.get(ip_ip='127.0.0.1')
        # compare
        self.assertEqual(str(ip_1), '127.0.0.1')

    def test_ip_ip_label(self):

        # get object
        ip_1 = Ip.objects.get(ip_ip='127.0.0.1')
        # get label
        field_label = ip_1._meta.get_field('ip_ip').verbose_name
        # compare
        self.assertEquals(field_label, 'ip ip')
