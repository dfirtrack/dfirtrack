from django.contrib.auth.models import User
from django.test import TestCase
import urllib.parse

class TaskCreatorViewTestCase(TestCase):
    """ task creator view tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_task_creator', password='E5BGU4meULjw7kdtvnzn')

    def test_task_creator_not_logged_in(self):
        """ test creator view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/task/creator/', safe='')
        # get response
        response = self.client.get('/task/creator/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_task_creator_logged_in(self):
        """ test creator view """

        # login testuser
        login = self.client.login(username='testuser_task_creator', password='E5BGU4meULjw7kdtvnzn')
        # get response
        response = self.client.get('/task/creator/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_task_creator_template(self):
        """ test creator view """

        # login testuser
        login = self.client.login(username='testuser_task_creator', password='E5BGU4meULjw7kdtvnzn')
        # get response
        response = self.client.get('/task/creator/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/task/task_creator.html')

    def test_task_creator_get_user_context(self):
        """ test creator view """

        # login testuser
        login = self.client.login(username='testuser_task_creator', password='E5BGU4meULjw7kdtvnzn')
        # get response
        response = self.client.get('/task/creator/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_task_creator')

    def test_task_creator_redirect(self):
        """ test creator view """

        # login testuser
        login = self.client.login(username='testuser_task_creator', password='E5BGU4meULjw7kdtvnzn')
        # create url
        destination = urllib.parse.quote('/task/creator/', safe='/')
        # get response
        response = self.client.get('/task/creator', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)
