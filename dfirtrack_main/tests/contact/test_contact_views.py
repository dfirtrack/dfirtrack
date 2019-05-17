from django.contrib.auth.models import User
from django.test import TestCase
from dfirtrack_main.models import Contact
from dfirtrack_main.views import contacts_views
import urllib.parse

class ContactViewTestCase(TestCase):
    """ contact view tests """

    @classmethod
    def setUpTestData(cls):

        # create object
        Contact.objects.create(contact_name='contact_1', contact_email='contact_1@example.org')
        # create user
        test_user = User.objects.create_user(username='testuser_contact', password='BeQNeJYsIpvJzFi0t5YW')

    def test_contacts_list_not_logged_in(self):

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/contacts/', safe='')
        # get response
        response = self.client.get('/contacts/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_contacts_list_logged_in(self):

        # login testuser
        login = self.client.login(username='testuser_contact', password='BeQNeJYsIpvJzFi0t5YW')
        # get response
        response = self.client.get('/contacts/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_contacts_list_template(self):

        # login testuser
        login = self.client.login(username='testuser_contact', password='BeQNeJYsIpvJzFi0t5YW')
        # get response
        response = self.client.get('/contacts/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/contact/contacts_list.html')

    def test_contacts_list_get_user_context(self):

        # login testuser
        login = self.client.login(username='testuser_contact', password='BeQNeJYsIpvJzFi0t5YW')
        # get response
        response = self.client.get('/contacts/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_contact')

    def test_contacts_detail_not_logged_in(self):

        # get object
        contact_1 = Contact.objects.get(contact_name='contact_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/contacts/' + str(contact_1.contact_id), safe='')
        # get response
        response = self.client.get('/contacts/' + str(contact_1.contact_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_contacts_detail_logged_in(self):

        # get object
        contact_1 = Contact.objects.get(contact_name='contact_1')
        # login testuser
        login = self.client.login(username='testuser_contact', password='BeQNeJYsIpvJzFi0t5YW')
        # get response
        response = self.client.get('/contacts/' + str(contact_1.contact_id))
        # compare
        self.assertEqual(response.status_code, 200)

    def test_contacts_detail_template(self):

        # get object
        contact_1 = Contact.objects.get(contact_name='contact_1')
        # login testuser
        login = self.client.login(username='testuser_contact', password='BeQNeJYsIpvJzFi0t5YW')
        # get response
        response = self.client.get('/contacts/' + str(contact_1.contact_id))
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/contact/contacts_detail.html')

    def test_contacts_detail_get_user_context(self):

        # get object
        contact_1 = Contact.objects.get(contact_name='contact_1')
        # login testuser
        login = self.client.login(username='testuser_contact', password='BeQNeJYsIpvJzFi0t5YW')
        # get response
        response = self.client.get('/contacts/' + str(contact_1.contact_id))
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_contact')

    def test_contacts_add_not_logged_in(self):

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/contacts/add/', safe='')
        # get response
        response = self.client.get('/contacts/add/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_contacts_add_logged_in(self):

        # login testuser
        login = self.client.login(username='testuser_contact', password='BeQNeJYsIpvJzFi0t5YW')
        # get response
        response = self.client.get('/contacts/add/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_contacts_add_template(self):

        # login testuser
        login = self.client.login(username='testuser_contact', password='BeQNeJYsIpvJzFi0t5YW')
        # get response
        response = self.client.get('/contacts/add/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/contact/contacts_add.html')

    def test_contacts_add_get_user_context(self):

        # login testuser
        login = self.client.login(username='testuser_contact', password='BeQNeJYsIpvJzFi0t5YW')
        # get response
        response = self.client.get('/contacts/add/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_contact')

    def test_contacts_edit_not_logged_in(self):

        # get object
        contact_1 = Contact.objects.get(contact_name='contact_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/contacts/' + str(contact_1.contact_id) + '/edit/', safe='')
        # get response
        response = self.client.get('/contacts/' + str(contact_1.contact_id) + '/edit/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_contacts_edit_logged_in(self):

        # get object
        contact_1 = Contact.objects.get(contact_name='contact_1')
        # login testuser
        login = self.client.login(username='testuser_contact', password='BeQNeJYsIpvJzFi0t5YW')
        # get response
        response = self.client.get('/contacts/' + str(contact_1.contact_id) + '/edit/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_contacts_edit_template(self):

        # get object
        contact_1 = Contact.objects.get(contact_name='contact_1')
        # login testuser
        login = self.client.login(username='testuser_contact', password='BeQNeJYsIpvJzFi0t5YW')
        # get response
        response = self.client.get('/contacts/' + str(contact_1.contact_id) + '/edit/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/contact/contacts_edit.html')

    def test_contacts_edit_get_user_context(self):

        # get object
        contact_1 = Contact.objects.get(contact_name='contact_1')
        # login testuser
        login = self.client.login(username='testuser_contact', password='BeQNeJYsIpvJzFi0t5YW')
        # get response
        response = self.client.get('/contacts/' + str(contact_1.contact_id) + '/edit/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_contact')

#    def test_contacts_detail_logged_in_not_existing(self):
#
#        # login testuser
#        login = self.client.login(username='testuser_contact', password='BeQNeJYsIpvJzFi0t5YW')
#        # get response
#        response = self.client.get('/contacts/x')
#        # compare
#        self.assertEqual(response.status_code, 404)
