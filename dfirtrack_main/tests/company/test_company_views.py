from django.contrib.auth.models import User
from django.test import TestCase
from dfirtrack_main.models import Company
import urllib.parse

class CompanyViewTestCase(TestCase):
    """ company view tests """

    @classmethod
    def setUpTestData(cls):

        # create object
        Company.objects.create(company_name='company_1')
        # create user
        test_user = User.objects.create_user(username='testuser_company', password='MbJfulGWGKeqceBtN9Mi')

    def test_companys_list_not_logged_in(self):
        """ test list view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/companys/', safe='')
        # get response
        response = self.client.get('/companys/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_companys_list_logged_in(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_company', password='MbJfulGWGKeqceBtN9Mi')
        # get response
        response = self.client.get('/companys/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_companys_list_template(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_company', password='MbJfulGWGKeqceBtN9Mi')
        # get response
        response = self.client.get('/companys/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/company/companys_list.html')

    def test_companys_list_get_user_context(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_company', password='MbJfulGWGKeqceBtN9Mi')
        # get response
        response = self.client.get('/companys/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_company')

    def test_companys_detail_not_logged_in(self):
        """ test detail view """

        # get object
        company_1 = Company.objects.get(company_name='company_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/companys/' + str(company_1.company_id), safe='')
        # get response
        response = self.client.get('/companys/' + str(company_1.company_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_companys_detail_logged_in(self):
        """ test detail view """

        # get object
        company_1 = Company.objects.get(company_name='company_1')
        # login testuser
        login = self.client.login(username='testuser_company', password='MbJfulGWGKeqceBtN9Mi')
        # get response
        response = self.client.get('/companys/' + str(company_1.company_id))
        # compare
        self.assertEqual(response.status_code, 200)

    def test_companys_detail_template(self):
        """ test detail view """

        # get object
        company_1 = Company.objects.get(company_name='company_1')
        # login testuser
        login = self.client.login(username='testuser_company', password='MbJfulGWGKeqceBtN9Mi')
        # get response
        response = self.client.get('/companys/' + str(company_1.company_id))
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/company/companys_detail.html')

    def test_companys_detail_get_user_context(self):
        """ test detail view """

        # get object
        company_1 = Company.objects.get(company_name='company_1')
        # login testuser
        login = self.client.login(username='testuser_company', password='MbJfulGWGKeqceBtN9Mi')
        # get response
        response = self.client.get('/companys/' + str(company_1.company_id))
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_company')

    def test_companys_add_not_logged_in(self):
        """ test add view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/companys/add/', safe='')
        # get response
        response = self.client.get('/companys/add/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_companys_add_logged_in(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_company', password='MbJfulGWGKeqceBtN9Mi')
        # get response
        response = self.client.get('/companys/add/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_companys_add_template(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_company', password='MbJfulGWGKeqceBtN9Mi')
        # get response
        response = self.client.get('/companys/add/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/company/companys_add.html')

    def test_companys_add_get_user_context(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_company', password='MbJfulGWGKeqceBtN9Mi')
        # get response
        response = self.client.get('/companys/add/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_company')

    def test_companys_edit_not_logged_in(self):
        """ test edit view """

        # get object
        company_1 = Company.objects.get(company_name='company_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/companys/' + str(company_1.company_id) + '/edit/', safe='')
        # get response
        response = self.client.get('/companys/' + str(company_1.company_id) + '/edit/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_companys_edit_logged_in(self):
        """ test edit view """

        # get object
        company_1 = Company.objects.get(company_name='company_1')
        # login testuser
        login = self.client.login(username='testuser_company', password='MbJfulGWGKeqceBtN9Mi')
        # get response
        response = self.client.get('/companys/' + str(company_1.company_id) + '/edit/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_companys_edit_template(self):
        """ test edit view """

        # get object
        company_1 = Company.objects.get(company_name='company_1')
        # login testuser
        login = self.client.login(username='testuser_company', password='MbJfulGWGKeqceBtN9Mi')
        # get response
        response = self.client.get('/companys/' + str(company_1.company_id) + '/edit/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/company/companys_edit.html')

    def test_companys_edit_get_user_context(self):
        """ test edit view """

        # get object
        company_1 = Company.objects.get(company_name='company_1')
        # login testuser
        login = self.client.login(username='testuser_company', password='MbJfulGWGKeqceBtN9Mi')
        # get response
        response = self.client.get('/companys/' + str(company_1.company_id) + '/edit/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_company')
