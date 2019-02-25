from django.test import TestCase
from dfirtrack_main.forms import IpForm

class IpFormTestCase(TestCase):
    """ ip form tests """

    def test_ip_ip_label(self):

        # get object
        form = IpForm()
        # compare
        self.assertEquals(form.fields['ip_ip'].label, 'IP (*)')

    def test_ip_ip_empty(self):

        # get object
        form = IpForm(data = {'ip_ip': ''})
        # compare
        self.assertFalse(form.is_valid())

    def test_ip_ip_filled(self):

        # get object
        form = IpForm(data = {'ip_ip': '127.0.0.1'})
        # compare
        self.assertTrue(form.is_valid())
