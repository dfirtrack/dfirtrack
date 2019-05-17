from django.contrib.auth.models import User
from django.test import TestCase
from dfirtrack_main.models import Division
from dfirtrack_main.views import divisions_views
import urllib.parse

class DivisionViewTestCase(TestCase):
    """ division view tests """

    @classmethod
    def setUpTestData(cls):

        # create object
        Division.objects.create(division_name='division_1')
        # create user
        test_user = User.objects.create_user(username='testuser_division', password='tcrayKsMKw7T6SGBKYgA')

    def test_divisions_list_not_logged_in(self):

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/divisions/', safe='')
        # get response
        response = self.client.get('/divisions/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_divisions_list_logged_in(self):

        # login testuser
        login = self.client.login(username='testuser_division', password='tcrayKsMKw7T6SGBKYgA')
        # get response
        response = self.client.get('/divisions/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_divisions_list_template(self):

        # login testuser
        login = self.client.login(username='testuser_division', password='tcrayKsMKw7T6SGBKYgA')
        # get response
        response = self.client.get('/divisions/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/division/divisions_list.html')

    def test_divisions_list_get_user_context(self):

        # login testuser
        login = self.client.login(username='testuser_division', password='tcrayKsMKw7T6SGBKYgA')
        # get response
        response = self.client.get('/divisions/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_division')

    def test_divisions_detail_not_logged_in(self):

        # get object
        division_1 = Division.objects.get(division_name='division_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/divisions/' + str(division_1.division_id), safe='')
        # get response
        response = self.client.get('/divisions/' + str(division_1.division_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_divisions_detail_logged_in(self):

        # get object
        division_1 = Division.objects.get(division_name='division_1')
        # login testuser
        login = self.client.login(username='testuser_division', password='tcrayKsMKw7T6SGBKYgA')
        # get response
        response = self.client.get('/divisions/' + str(division_1.division_id))
        # compare
        self.assertEqual(response.status_code, 200)

    def test_divisions_detail_template(self):

        # get object
        division_1 = Division.objects.get(division_name='division_1')
        # login testuser
        login = self.client.login(username='testuser_division', password='tcrayKsMKw7T6SGBKYgA')
        # get response
        response = self.client.get('/divisions/' + str(division_1.division_id))
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/division/divisions_detail.html')

    def test_divisions_detail_get_user_context(self):

        # get object
        division_1 = Division.objects.get(division_name='division_1')
        # login testuser
        login = self.client.login(username='testuser_division', password='tcrayKsMKw7T6SGBKYgA')
        # get response
        response = self.client.get('/divisions/' + str(division_1.division_id))
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_division')

    def test_divisions_add_not_logged_in(self):

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/divisions/add/', safe='')
        # get response
        response = self.client.get('/divisions/add/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_divisions_add_logged_in(self):

        # login testuser
        login = self.client.login(username='testuser_division', password='tcrayKsMKw7T6SGBKYgA')
        # get response
        response = self.client.get('/divisions/add/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_divisions_add_template(self):

        # login testuser
        login = self.client.login(username='testuser_division', password='tcrayKsMKw7T6SGBKYgA')
        # get response
        response = self.client.get('/divisions/add/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/division/divisions_add.html')

    def test_divisions_add_get_user_context(self):

        # login testuser
        login = self.client.login(username='testuser_division', password='tcrayKsMKw7T6SGBKYgA')
        # get response
        response = self.client.get('/divisions/add/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_division')

    def test_divisions_edit_not_logged_in(self):

        # get object
        division_1 = Division.objects.get(division_name='division_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/divisions/' + str(division_1.division_id) + '/edit/', safe='')
        # get response
        response = self.client.get('/divisions/' + str(division_1.division_id) + '/edit/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_divisions_edit_logged_in(self):

        # get object
        division_1 = Division.objects.get(division_name='division_1')
        # login testuser
        login = self.client.login(username='testuser_division', password='tcrayKsMKw7T6SGBKYgA')
        # get response
        response = self.client.get('/divisions/' + str(division_1.division_id) + '/edit/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_divisions_edit_template(self):

        # get object
        division_1 = Division.objects.get(division_name='division_1')
        # login testuser
        login = self.client.login(username='testuser_division', password='tcrayKsMKw7T6SGBKYgA')
        # get response
        response = self.client.get('/divisions/' + str(division_1.division_id) + '/edit/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/division/divisions_edit.html')

    def test_divisions_edit_get_user_context(self):

        # get object
        division_1 = Division.objects.get(division_name='division_1')
        # login testuser
        login = self.client.login(username='testuser_division', password='tcrayKsMKw7T6SGBKYgA')
        # get response
        response = self.client.get('/divisions/' + str(division_1.division_id) + '/edit/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_division')

#    def test_divisions_detail_logged_in_not_existing(self):
#
#        # login testuser
#        login = self.client.login(username='testuser_division', password='tcrayKsMKw7T6SGBKYgA')
#        # get response
#        response = self.client.get('/divisions/x')
#        # compare
#        self.assertEqual(response.status_code, 404)
