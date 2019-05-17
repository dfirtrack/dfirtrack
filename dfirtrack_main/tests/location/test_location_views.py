from django.contrib.auth.models import User
from django.test import TestCase
from dfirtrack_main.models import Location
import urllib.parse

class LocationViewTestCase(TestCase):
    """ location view tests """

    @classmethod
    def setUpTestData(cls):

        # create object
        Location.objects.create(location_name='location_1')
        # create user
        test_user = User.objects.create_user(username='testuser_location', password='jjSeshxL17aDEdqkt8tP')

    def test_locations_list_not_logged_in(self):

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/locations/', safe='')
        # get response
        response = self.client.get('/locations/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_locations_list_logged_in(self):

        # login testuser
        login = self.client.login(username='testuser_location', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/locations/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_locations_list_template(self):

        # login testuser
        login = self.client.login(username='testuser_location', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/locations/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/location/locations_list.html')

    def test_locations_list_get_user_context(self):

        # login testuser
        login = self.client.login(username='testuser_location', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/locations/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_location')

    def test_locations_detail_not_logged_in(self):

        # get object
        location_1 = Location.objects.get(location_name='location_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/locations/' + str(location_1.location_id), safe='')
        # get response
        response = self.client.get('/locations/' + str(location_1.location_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_locations_detail_logged_in(self):

        # get object
        location_1 = Location.objects.get(location_name='location_1')
        # login testuser
        login = self.client.login(username='testuser_location', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/locations/' + str(location_1.location_id))
        # compare
        self.assertEqual(response.status_code, 200)

    def test_locations_detail_template(self):

        # get object
        location_1 = Location.objects.get(location_name='location_1')
        # login testuser
        login = self.client.login(username='testuser_location', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/locations/' + str(location_1.location_id))
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/location/locations_detail.html')

    def test_locations_detail_get_user_context(self):

        # get object
        location_1 = Location.objects.get(location_name='location_1')
        # login testuser
        login = self.client.login(username='testuser_location', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/locations/' + str(location_1.location_id))
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_location')

    def test_locations_add_not_logged_in(self):

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/locations/add/', safe='')
        # get response
        response = self.client.get('/locations/add/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_locations_add_logged_in(self):

        # login testuser
        login = self.client.login(username='testuser_location', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/locations/add/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_locations_add_template(self):

        # login testuser
        login = self.client.login(username='testuser_location', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/locations/add/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/location/locations_add.html')

    def test_locations_add_get_user_context(self):

        # login testuser
        login = self.client.login(username='testuser_location', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/locations/add/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_location')

    def test_locations_edit_not_logged_in(self):

        # get object
        location_1 = Location.objects.get(location_name='location_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/locations/' + str(location_1.location_id) + '/edit/', safe='')
        # get response
        response = self.client.get('/locations/' + str(location_1.location_id) + '/edit/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_locations_edit_logged_in(self):

        # get object
        location_1 = Location.objects.get(location_name='location_1')
        # login testuser
        login = self.client.login(username='testuser_location', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/locations/' + str(location_1.location_id) + '/edit/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_locations_edit_template(self):

        # get object
        location_1 = Location.objects.get(location_name='location_1')
        # login testuser
        login = self.client.login(username='testuser_location', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/locations/' + str(location_1.location_id) + '/edit/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/location/locations_edit.html')

    def test_locations_edit_get_user_context(self):

        # get object
        location_1 = Location.objects.get(location_name='location_1')
        # login testuser
        login = self.client.login(username='testuser_location', password='jjSeshxL17aDEdqkt8tP')
        # get response
        response = self.client.get('/locations/' + str(location_1.location_id) + '/edit/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_location')

#    def test_locations_detail_logged_in_not_existing(self):
#
#        # login testuser
#        login = self.client.login(username='testuser_location', password='jjSeshxL17aDEdqkt8tP')
#        # get response
#        response = self.client.get('/locations/x')
#        # compare
#        self.assertEqual(response.status_code, 404)
