from django.contrib.auth.models import User
from django.test import TestCase
from dfirtrack_main.models import Systemtype
from dfirtrack_main.views import systemtypes_views
import urllib.parse

class SystemtypeViewTestCase(TestCase):
    """ systemtype view tests """

    @classmethod
    def setUpTestData(cls):

        # create object
        Systemtype.objects.create(systemtype_name='systemtype_1')
        # create user
        test_user = User.objects.create_user(username='testuser_systemtype', password='A8VfAc8hrJp3Dg7EtMpu')
        test_user.save()

    def test_systemtypes_list_not_logged_in(self):

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/systemtypes/', safe='')
        # get response
        response = self.client.get('/systemtypes/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_systemtypes_list_logged_in(self):

        # login testuser
        login = self.client.login(username='testuser_systemtype', password='A8VfAc8hrJp3Dg7EtMpu')
        # get response
        response = self.client.get('/systemtypes/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_systemtypes_list_template(self):

        # login testuser
        login = self.client.login(username='testuser_systemtype', password='A8VfAc8hrJp3Dg7EtMpu')
        # get response
        response = self.client.get('/systemtypes/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/systemtype/systemtypes_list.html')

    def test_systemtypes_list_get_user_context(self):

        # login testuser
        login = self.client.login(username='testuser_systemtype', password='A8VfAc8hrJp3Dg7EtMpu')
        # get response
        response = self.client.get('/systemtypes/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_systemtype')

    def test_systemtypes_detail_not_logged_in(self):

        # get object
        systemtype_1 = Systemtype.objects.get(systemtype_name='systemtype_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/systemtypes/' + str(systemtype_1.systemtype_id), safe='')
        # get response
        response = self.client.get('/systemtypes/' + str(systemtype_1.systemtype_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_systemtypes_detail_logged_in(self):

        # get object
        systemtype_1 = Systemtype.objects.get(systemtype_name='systemtype_1')
        # login testuser
        login = self.client.login(username='testuser_systemtype', password='A8VfAc8hrJp3Dg7EtMpu')
        # get response
        response = self.client.get('/systemtypes/' + str(systemtype_1.systemtype_id))
        # compare
        self.assertEqual(response.status_code, 200)

    def test_systemtypes_detail_template(self):

        # get object
        systemtype_1 = Systemtype.objects.get(systemtype_name='systemtype_1')
        # login testuser
        login = self.client.login(username='testuser_systemtype', password='A8VfAc8hrJp3Dg7EtMpu')
        # get response
        response = self.client.get('/systemtypes/' + str(systemtype_1.systemtype_id))
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/systemtype/systemtypes_detail.html')

    def test_systemtypes_detail_get_user_context(self):

        # get object
        systemtype_1 = Systemtype.objects.get(systemtype_name='systemtype_1')
        # login testuser
        login = self.client.login(username='testuser_systemtype', password='A8VfAc8hrJp3Dg7EtMpu')
        # get response
        response = self.client.get('/systemtypes/' + str(systemtype_1.systemtype_id))
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_systemtype')

    def test_systemtypes_add_not_logged_in(self):

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/systemtypes/add/', safe='')
        # get response
        response = self.client.get('/systemtypes/add/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_systemtypes_add_logged_in(self):

        # login testuser
        login = self.client.login(username='testuser_systemtype', password='A8VfAc8hrJp3Dg7EtMpu')
        # get response
        response = self.client.get('/systemtypes/add/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_systemtypes_add_template(self):

        # login testuser
        login = self.client.login(username='testuser_systemtype', password='A8VfAc8hrJp3Dg7EtMpu')
        # get response
        response = self.client.get('/systemtypes/add/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/systemtype/systemtypes_add.html')

    def test_systemtypes_add_get_user_context(self):

        # login testuser
        login = self.client.login(username='testuser_systemtype', password='A8VfAc8hrJp3Dg7EtMpu')
        # get response
        response = self.client.get('/systemtypes/add/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_systemtype')

    def test_systemtypes_edit_not_logged_in(self):

        # get object
        systemtype_1 = Systemtype.objects.get(systemtype_name='systemtype_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/systemtypes/' + str(systemtype_1.systemtype_id) + '/edit/', safe='')
        # get response
        response = self.client.get('/systemtypes/' + str(systemtype_1.systemtype_id) + '/edit/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_systemtypes_edit_logged_in(self):

        # get object
        systemtype_1 = Systemtype.objects.get(systemtype_name='systemtype_1')
        # login testuser
        login = self.client.login(username='testuser_systemtype', password='A8VfAc8hrJp3Dg7EtMpu')
        # get response
        response = self.client.get('/systemtypes/' + str(systemtype_1.systemtype_id) + '/edit/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_systemtypes_edit_template(self):

        # get object
        systemtype_1 = Systemtype.objects.get(systemtype_name='systemtype_1')
        # login testuser
        login = self.client.login(username='testuser_systemtype', password='A8VfAc8hrJp3Dg7EtMpu')
        # get response
        response = self.client.get('/systemtypes/' + str(systemtype_1.systemtype_id) + '/edit/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/systemtype/systemtypes_edit.html')

    def test_systemtypes_edit_get_user_context(self):

        # get object
        systemtype_1 = Systemtype.objects.get(systemtype_name='systemtype_1')
        # login testuser
        login = self.client.login(username='testuser_systemtype', password='A8VfAc8hrJp3Dg7EtMpu')
        # get response
        response = self.client.get('/systemtypes/' + str(systemtype_1.systemtype_id) + '/edit/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_systemtype')

#    def test_systemtypes_detail_logged_in_not_existing(self):
#
#        # login testuser
#        login = self.client.login(username='testuser_systemtype', password='A8VfAc8hrJp3Dg7EtMpu')
#        # get response
#        response = self.client.get('/systemtypes/x')
#        # compare
#        self.assertEqual(response.status_code, 404)
