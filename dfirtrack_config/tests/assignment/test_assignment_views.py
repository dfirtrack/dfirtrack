import urllib.parse

from django.contrib.auth.models import User
from django.test import TestCase


class AssignmentViewTestCase(TestCase):
    """assignment view tests"""

    @classmethod
    def setUpTestData(cls):
        # create user
        User.objects.create_user(
            username='testuser_assignment', password='8t5Uw5eAYDtd5X6TVAXK'
        )

    def test_assignment_view_not_logged_in(self):
        """test assignment view"""

        # create url
        destination = '/login/?next=' + urllib.parse.quote(
            '/config/assignment/', safe=''
        )
        # get response
        response = self.client.get('/config/assignment/', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_assignment_view_logged_in(self):
        """test assignment view"""

        # login testuser
        self.client.login(
            username='testuser_assignment', password='8t5Uw5eAYDtd5X6TVAXK'
        )
        # get response
        response = self.client.get('/config/assignment/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_assignment_view_template(self):
        """test assignment view"""

        # login testuser
        self.client.login(
            username='testuser_assignment', password='8t5Uw5eAYDtd5X6TVAXK'
        )
        # get response
        response = self.client.get('/config/assignment/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_config/assignment/assignment.html')

    def test_assignment_view_get_user_context(self):
        """test assignment view"""

        # login testuser
        self.client.login(
            username='testuser_assignment', password='8t5Uw5eAYDtd5X6TVAXK'
        )
        # get response
        response = self.client.get('/config/assignment/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_assignment')

    def test_assignment_view_redirect(self):
        """test assignment view"""

        # login testuser
        self.client.login(
            username='testuser_assignment', password='8t5Uw5eAYDtd5X6TVAXK'
        )
        # create url
        destination = urllib.parse.quote('/config/assignment/', safe='/')
        # get response
        response = self.client.get('/config/assignment', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )

    def test_assignment_view_clear_filter_not_logged_in(self):
        """test assignment view"""

        # create url
        destination = '/login/?next=' + urllib.parse.quote(
            '/config/assignment/clear_filter/', safe=''
        )
        # get response
        response = self.client.get('/config/assignment/clear_filter/', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_assignment_view_clear_filter_logged_in(self):
        """test assignment view"""

        # login testuser
        self.client.login(
            username='testuser_assignment', password='8t5Uw5eAYDtd5X6TVAXK'
        )
        # create url
        destination = urllib.parse.quote('/config/assignment/', safe='/')
        # get response
        response = self.client.get('/config/assignment/clear_filter/')
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_assignment_view_clear_filter_redirect(self):
        """test assignment view"""

        # login testuser
        self.client.login(
            username='testuser_assignment', password='8t5Uw5eAYDtd5X6TVAXK'
        )
        # create url
        destination = urllib.parse.quote('/config/assignment/', safe='/')
        # get response
        response = self.client.get('/config/assignment/clear_filter', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )
