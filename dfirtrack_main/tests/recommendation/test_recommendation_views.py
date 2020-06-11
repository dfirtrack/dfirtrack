from django.contrib.auth.models import User
from django.test import TestCase
from dfirtrack_main.models import Recommendation
import urllib.parse

class RecommendationViewTestCase(TestCase):
    """ recommendation view tests """

    @classmethod
    def setUpTestData(cls):

        # create object
        Recommendation.objects.create(recommendation_name='recommendation_1')
        # create user
        test_user = User.objects.create_user(username='testuser_recommendation', password='f5n2U59eN7BVi7sM3209')

    def test_recommendation_list_not_logged_in(self):
        """ test list view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/recommendation/', safe='')
        # get response
        response = self.client.get('/recommendation/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_recommendation_list_logged_in(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_recommendation', password='f5n2U59eN7BVi7sM3209')
        # get response
        response = self.client.get('/recommendation/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_recommendation_list_template(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_recommendation', password='f5n2U59eN7BVi7sM3209')
        # get response
        response = self.client.get('/recommendation/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/recommendation/recommendation_list.html')

    def test_recommendation_list_get_user_context(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_recommendation', password='f5n2U59eN7BVi7sM3209')
        # get response
        response = self.client.get('/recommendation/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_recommendation')

    def test_recommendation_list_redirect(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_recommendation', password='f5n2U59eN7BVi7sM3209')
        # create url
        destination = urllib.parse.quote('/recommendation/', safe='/')
        # get response
        response = self.client.get('/recommendation', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_recommendation_detail_not_logged_in(self):
        """ test detail view """

        # get object
        recommendation_1 = Recommendation.objects.get(recommendation_name='recommendation_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/recommendation/' + str(recommendation_1.recommendation_id) + '/', safe='')
        # get response
        response = self.client.get('/recommendation/' + str(recommendation_1.recommendation_id) + '/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_recommendation_detail_logged_in(self):
        """ test detail view """

        # get object
        recommendation_1 = Recommendation.objects.get(recommendation_name='recommendation_1')
        # login testuser
        login = self.client.login(username='testuser_recommendation', password='f5n2U59eN7BVi7sM3209')
        # get response
        response = self.client.get('/recommendation/' + str(recommendation_1.recommendation_id) + '/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_recommendation_detail_template(self):
        """ test detail view """

        # get object
        recommendation_1 = Recommendation.objects.get(recommendation_name='recommendation_1')
        # login testuser
        login = self.client.login(username='testuser_recommendation', password='f5n2U59eN7BVi7sM3209')
        # get response
        response = self.client.get('/recommendation/' + str(recommendation_1.recommendation_id) + '/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/recommendation/recommendation_detail.html')

    def test_recommendation_detail_get_user_context(self):
        """ test detail view """

        # get object
        recommendation_1 = Recommendation.objects.get(recommendation_name='recommendation_1')
        # login testuser
        login = self.client.login(username='testuser_recommendation', password='f5n2U59eN7BVi7sM3209')
        # get response
        response = self.client.get('/recommendation/' + str(recommendation_1.recommendation_id) + '/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_recommendation')

    def test_recommendation_detail_redirect(self):
        """ test detail view """

        # get object
        recommendation_1 = Recommendation.objects.get(recommendation_name='recommendation_1')
        # login testuser
        login = self.client.login(username='testuser_recommendation', password='f5n2U59eN7BVi7sM3209')
        # create url
        destination = urllib.parse.quote('/recommendation/' + str(recommendation_1.recommendation_id) + '/', safe='/')
        # get response
        response = self.client.get('/recommendation/' + str(recommendation_1.recommendation_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_recommendation_add_not_logged_in(self):
        """ test add view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/recommendation/add/', safe='')
        # get response
        response = self.client.get('/recommendation/add/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_recommendation_add_logged_in(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_recommendation', password='f5n2U59eN7BVi7sM3209')
        # get response
        response = self.client.get('/recommendation/add/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_recommendation_add_template(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_recommendation', password='f5n2U59eN7BVi7sM3209')
        # get response
        response = self.client.get('/recommendation/add/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/recommendation/recommendation_add.html')

    def test_recommendation_add_get_user_context(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_recommendation', password='f5n2U59eN7BVi7sM3209')
        # get response
        response = self.client.get('/recommendation/add/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_recommendation')

    def test_recommendation_add_redirect(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_recommendation', password='f5n2U59eN7BVi7sM3209')
        # create url
        destination = urllib.parse.quote('/recommendation/add/', safe='/')
        # get response
        response = self.client.get('/recommendation/add', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_recommendation_edit_not_logged_in(self):
        """ test edit view """

        # get object
        recommendation_1 = Recommendation.objects.get(recommendation_name='recommendation_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/recommendation/' + str(recommendation_1.recommendation_id) + '/edit/', safe='')
        # get response
        response = self.client.get('/recommendation/' + str(recommendation_1.recommendation_id) + '/edit/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_recommendation_edit_logged_in(self):
        """ test edit view """

        # get object
        recommendation_1 = Recommendation.objects.get(recommendation_name='recommendation_1')
        # login testuser
        login = self.client.login(username='testuser_recommendation', password='f5n2U59eN7BVi7sM3209')
        # get response
        response = self.client.get('/recommendation/' + str(recommendation_1.recommendation_id) + '/edit/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_recommendation_edit_template(self):
        """ test edit view """

        # get object
        recommendation_1 = Recommendation.objects.get(recommendation_name='recommendation_1')
        # login testuser
        login = self.client.login(username='testuser_recommendation', password='f5n2U59eN7BVi7sM3209')
        # get response
        response = self.client.get('/recommendation/' + str(recommendation_1.recommendation_id) + '/edit/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/recommendation/recommendation_edit.html')

    def test_recommendation_edit_get_user_context(self):
        """ test edit view """

        # get object
        recommendation_1 = Recommendation.objects.get(recommendation_name='recommendation_1')
        # login testuser
        login = self.client.login(username='testuser_recommendation', password='f5n2U59eN7BVi7sM3209')
        # get response
        response = self.client.get('/recommendation/' + str(recommendation_1.recommendation_id) + '/edit/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_recommendation')

    def test_recommendation_edit_redirect(self):
        """ test edit view """

        # get object
        recommendation_1 = Recommendation.objects.get(recommendation_name='recommendation_1')
        # login testuser
        login = self.client.login(username='testuser_recommendation', password='f5n2U59eN7BVi7sM3209')
        # create url
        destination = urllib.parse.quote('/recommendation/' + str(recommendation_1.recommendation_id) + '/edit/', safe='/')
        # get response
        response = self.client.get('/recommendation/' + str(recommendation_1.recommendation_id) + '/edit', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)
