from django.contrib.auth.models import User
from django.test import TestCase
from dfirtrack_main.models import Division
import urllib.parse

class DivisionAPIViewTestCase(TestCase):
    """ division API view tests """

    @classmethod
    def setUpTestData(cls):

        # create object
        Division.objects.create(division_name='division_api_1')
        # create user
        test_user = User.objects.create_user(username='testuser_division_api', password='tvjnIPBlhP9P3ixDHVE7')

    def test_division_list_api_unauthorized(self):
        """ unauthorized access is forbidden"""

        # get response
        response = self.client.get('/api/divisions/')
        # compare
        self.assertEqual(response.status_code, 401)

    def test_division_list_api_method_get(self):
        """ GET is allowed """

        # login testuser
        login = self.client.login(username='testuser_division_api', password='tvjnIPBlhP9P3ixDHVE7')
        # get response
        response = self.client.get('/api/divisions/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_division_list_api_method_post(self):
        """ POST is allowed """

        # login testuser
        login = self.client.login(username='testuser_division_api', password='tvjnIPBlhP9P3ixDHVE7')
        # create POST string
        poststring = {"division_name": "division_api_2"}
        # get response
        response = self.client.post('/api/divisions/', data=poststring)
        # compare
        self.assertEqual(response.status_code, 201)

    def test_division_list_api_redirect(self):
        """ test redirect with appending slash """

        # login testuser
        login = self.client.login(username='testuser_division_api', password='tvjnIPBlhP9P3ixDHVE7')
        # create url
        destination = urllib.parse.quote('/api/divisions/', safe='/')
        # get response
        response = self.client.get('/api/divisions', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

#    def test_division_list_api_get_user_context(self):
#        """ test user context """
#
#        # login testuser
#        login = self.client.login(username='testuser_division_api', password='tvjnIPBlhP9P3ixDHVE7')
#        # get response
#        response = self.client.get('/api/divisions/')
#        # compare
#        self.assertEqual(str(response.context['user']), 'testuser_division_api')

    def test_division_detail_api_unauthorized (self):
        """ unauthorized access is forbidden"""

        # get object
        division_api_1 = Division.objects.get(division_name='division_api_1')
        # get response
        response = self.client.get('/api/divisions/' + str(division_api_1.division_id) + '/')
        # compare
        self.assertEqual(response.status_code, 401)

    def test_division_detail_api_method_get(self):
        """ GET is allowed """

        # get object
        division_api_1 = Division.objects.get(division_name='division_api_1')
        # login testuser
        login = self.client.login(username='testuser_division_api', password='tvjnIPBlhP9P3ixDHVE7')
        # get response
        response = self.client.get('/api/divisions/' + str(division_api_1.division_id) + '/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_division_detail_api_method_delete(self):
        """ DELETE is forbidden """

        # get object
        division_api_1 = Division.objects.get(division_name='division_api_1')
        # login testuser
        login = self.client.login(username='testuser_division_api', password='tvjnIPBlhP9P3ixDHVE7')
        # get response
        response = self.client.delete('/api/divisions/' + str(division_api_1.division_id) + '/')
        # compare
        self.assertEqual(response.status_code, 405)

    def test_division_detail_api_method_put(self):
        """ PUT is allowed """

        # get object
        division_api_1 = Division.objects.get(division_name='division_api_1')
        # login testuser
        login = self.client.login(username='testuser_division_api', password='tvjnIPBlhP9P3ixDHVE7')
        # create url
        destination = urllib.parse.quote('/api/divisions/' + str(division_api_1.division_id) + '/', safe='/')
        # create PUT string
        putstring = {"division_name": "new_division_api_1"}
        # get response
        response = self.client.put(destination, data=putstring, content_type='application/json')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_division_detail_api_redirect(self):
        """ test redirect with appending slash """

        # get object
        division_api_1 = Division.objects.get(division_name='division_api_1')
        # login testuser
        login = self.client.login(username='testuser_division_api', password='tvjnIPBlhP9P3ixDHVE7')
        # create url
        destination = urllib.parse.quote('/api/divisions/' + str(division_api_1.division_id) + '/', safe='/')
        # get response
        response = self.client.get('/api/divisions/' + str(division_api_1.division_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

#    def test_division_detail_api_get_user_context(self):
#        """ test user context """
#
#        # get object
#        division_api_1 = Division.objects.get(division_name='division_api_1')
#        # login testuser
#        login = self.client.login(username='testuser_division_api', password='tvjnIPBlhP9P3ixDHVE7')
#        # get response
#        response = self.client.get('/api/divisions/' + str(division_api_1.division_id) + '/')
#        # compare
#        self.assertEqual(str(response.context['user']), 'testuser_division_api')
