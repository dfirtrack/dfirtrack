from django.contrib.auth.models import User
from django.test import TestCase
from dfirtrack_main.models import Serviceprovider
from dfirtrack_main.views import serviceproviders_views
import urllib.parse

class ServiceproviderViewTestCase(TestCase):
    """ serviceprovider view tests """

    @classmethod
    def setUpTestData(cls):

        # create object
        Serviceprovider.objects.create(serviceprovider_name='serviceprovider_1')
        # create user
        test_user = User.objects.create_user(username='testuser_serviceprovider', password='KxVbBhKZcvh6IcQUGjr0')

    def test_serviceproviders_list_not_logged_in(self):

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/serviceproviders/', safe='')
        # get response
        response = self.client.get('/serviceproviders/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_serviceproviders_list_logged_in(self):

        # login testuser
        login = self.client.login(username='testuser_serviceprovider', password='KxVbBhKZcvh6IcQUGjr0')
        # get response
        response = self.client.get('/serviceproviders/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_serviceproviders_list_template(self):

        # login testuser
        login = self.client.login(username='testuser_serviceprovider', password='KxVbBhKZcvh6IcQUGjr0')
        # get response
        response = self.client.get('/serviceproviders/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/serviceprovider/serviceproviders_list.html')

    def test_serviceproviders_list_get_user_context(self):

        # login testuser
        login = self.client.login(username='testuser_serviceprovider', password='KxVbBhKZcvh6IcQUGjr0')
        # get response
        response = self.client.get('/serviceproviders/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_serviceprovider')

    def test_serviceproviders_detail_not_logged_in(self):

        # get object
        serviceprovider_1 = Serviceprovider.objects.get(serviceprovider_name='serviceprovider_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/serviceproviders/' + str(serviceprovider_1.serviceprovider_id), safe='')
        # get response
        response = self.client.get('/serviceproviders/' + str(serviceprovider_1.serviceprovider_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_serviceproviders_detail_logged_in(self):

        # get object
        serviceprovider_1 = Serviceprovider.objects.get(serviceprovider_name='serviceprovider_1')
        # login testuser
        login = self.client.login(username='testuser_serviceprovider', password='KxVbBhKZcvh6IcQUGjr0')
        # get response
        response = self.client.get('/serviceproviders/' + str(serviceprovider_1.serviceprovider_id))
        # compare
        self.assertEqual(response.status_code, 200)

    def test_serviceproviders_detail_template(self):

        # get object
        serviceprovider_1 = Serviceprovider.objects.get(serviceprovider_name='serviceprovider_1')
        # login testuser
        login = self.client.login(username='testuser_serviceprovider', password='KxVbBhKZcvh6IcQUGjr0')
        # get response
        response = self.client.get('/serviceproviders/' + str(serviceprovider_1.serviceprovider_id))
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/serviceprovider/serviceproviders_detail.html')

    def test_serviceproviders_detail_get_user_context(self):

        # get object
        serviceprovider_1 = Serviceprovider.objects.get(serviceprovider_name='serviceprovider_1')
        # login testuser
        login = self.client.login(username='testuser_serviceprovider', password='KxVbBhKZcvh6IcQUGjr0')
        # get response
        response = self.client.get('/serviceproviders/' + str(serviceprovider_1.serviceprovider_id))
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_serviceprovider')

    def test_serviceproviders_add_not_logged_in(self):

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/serviceproviders/add/', safe='')
        # get response
        response = self.client.get('/serviceproviders/add/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_serviceproviders_add_logged_in(self):

        # login testuser
        login = self.client.login(username='testuser_serviceprovider', password='KxVbBhKZcvh6IcQUGjr0')
        # get response
        response = self.client.get('/serviceproviders/add/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_serviceproviders_add_template(self):

        # login testuser
        login = self.client.login(username='testuser_serviceprovider', password='KxVbBhKZcvh6IcQUGjr0')
        # get response
        response = self.client.get('/serviceproviders/add/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/serviceprovider/serviceproviders_add.html')

    def test_serviceproviders_add_get_user_context(self):

        # login testuser
        login = self.client.login(username='testuser_serviceprovider', password='KxVbBhKZcvh6IcQUGjr0')
        # get response
        response = self.client.get('/serviceproviders/add/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_serviceprovider')

    def test_serviceproviders_edit_not_logged_in(self):

        # get object
        serviceprovider_1 = Serviceprovider.objects.get(serviceprovider_name='serviceprovider_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/serviceproviders/' + str(serviceprovider_1.serviceprovider_id) + '/edit/', safe='')
        # get response
        response = self.client.get('/serviceproviders/' + str(serviceprovider_1.serviceprovider_id) + '/edit/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_serviceproviders_edit_logged_in(self):

        # get object
        serviceprovider_1 = Serviceprovider.objects.get(serviceprovider_name='serviceprovider_1')
        # login testuser
        login = self.client.login(username='testuser_serviceprovider', password='KxVbBhKZcvh6IcQUGjr0')
        # get response
        response = self.client.get('/serviceproviders/' + str(serviceprovider_1.serviceprovider_id) + '/edit/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_serviceproviders_edit_template(self):

        # get object
        serviceprovider_1 = Serviceprovider.objects.get(serviceprovider_name='serviceprovider_1')
        # login testuser
        login = self.client.login(username='testuser_serviceprovider', password='KxVbBhKZcvh6IcQUGjr0')
        # get response
        response = self.client.get('/serviceproviders/' + str(serviceprovider_1.serviceprovider_id) + '/edit/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/serviceprovider/serviceproviders_edit.html')

    def test_serviceproviders_edit_get_user_context(self):

        # get object
        serviceprovider_1 = Serviceprovider.objects.get(serviceprovider_name='serviceprovider_1')
        # login testuser
        login = self.client.login(username='testuser_serviceprovider', password='KxVbBhKZcvh6IcQUGjr0')
        # get response
        response = self.client.get('/serviceproviders/' + str(serviceprovider_1.serviceprovider_id) + '/edit/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_serviceprovider')

#    def test_serviceproviders_detail_logged_in_not_existing(self):
#
#        # login testuser
#        login = self.client.login(username='testuser_serviceprovider', password='KxVbBhKZcvh6IcQUGjr0')
#        # get response
#        response = self.client.get('/serviceproviders/x')
#        # compare
#        self.assertEqual(response.status_code, 404)
