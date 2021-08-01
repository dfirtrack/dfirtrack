import urllib.parse

from django.contrib.auth.models import User
from django.test import TestCase

from dfirtrack_main.models import Notestatus


class NotestatusViewTestCase(TestCase):
    """notestatus view tests"""

    @classmethod
    def setUpTestData(cls):

        # create object
        Notestatus.objects.create(notestatus_name="notestatus_1")
        # create user
        User.objects.create_user(
            username="testuser_notestatus", password="HABbKEVhT9iNeMYv4q9l"
        )

    def test_notestatus_list_not_logged_in(self):
        """test list view"""

        # create url
        destination = "/login/?next=" + urllib.parse.quote("/notestatus/", safe="")
        # get response
        response = self.client.get("/notestatus/", follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_notestatus_list_logged_in(self):
        """test list view"""

        # login testuser
        self.client.login(
            username="testuser_notestatus", password="HABbKEVhT9iNeMYv4q9l"
        )
        # get response
        response = self.client.get("/notestatus/")
        # compare
        self.assertEqual(response.status_code, 200)

    def test_notestatus_list_template(self):
        """test list view"""

        # login testuser
        self.client.login(
            username="testuser_notestatus", password="HABbKEVhT9iNeMYv4q9l"
        )
        # get response
        response = self.client.get("/notestatus/")
        # compare
        self.assertTemplateUsed(
            response, "dfirtrack_main/notestatus/notestatus_list.html"
        )

    def test_notestatus_list_get_user_context(self):
        """test list view"""

        # login testuser
        self.client.login(
            username="testuser_notestatus", password="HABbKEVhT9iNeMYv4q9l"
        )
        # get response
        response = self.client.get("/notestatus/")
        # compare
        self.assertEqual(str(response.context["user"]), "testuser_notestatus")

    def test_notestatus_list_redirect(self):
        """test list view"""

        # login testuser
        self.client.login(
            username="testuser_notestatus", password="HABbKEVhT9iNeMYv4q9l"
        )
        # create url
        destination = urllib.parse.quote("/notestatus/", safe="/")
        # get response
        response = self.client.get("/notestatus", follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )

    def test_notestatus_detail_not_logged_in(self):
        """test detail view"""

        # get object
        notestatus_1 = Notestatus.objects.get(notestatus_name="notestatus_1")
        # create url
        destination = "/login/?next=" + urllib.parse.quote(
            "/notestatus/" + str(notestatus_1.notestatus_id) + "/", safe=""
        )
        # get response
        response = self.client.get(
            "/notestatus/" + str(notestatus_1.notestatus_id) + "/", follow=True
        )
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_notestatus_detail_logged_in(self):
        """test detail view"""

        # get object
        notestatus_1 = Notestatus.objects.get(notestatus_name="notestatus_1")
        # login testuser
        self.client.login(
            username="testuser_notestatus", password="HABbKEVhT9iNeMYv4q9l"
        )
        # get response
        response = self.client.get(
            "/notestatus/" + str(notestatus_1.notestatus_id) + "/"
        )
        # compare
        self.assertEqual(response.status_code, 200)

    def test_notestatus_detail_template(self):
        """test detail view"""

        # get object
        notestatus_1 = Notestatus.objects.get(notestatus_name="notestatus_1")
        # login testuser
        self.client.login(
            username="testuser_notestatus", password="HABbKEVhT9iNeMYv4q9l"
        )
        # get response
        response = self.client.get(
            "/notestatus/" + str(notestatus_1.notestatus_id) + "/"
        )
        # compare
        self.assertTemplateUsed(
            response, "dfirtrack_main/notestatus/notestatus_detail.html"
        )

    def test_notestatus_detail_get_user_context(self):
        """test detail view"""

        # get object
        notestatus_1 = Notestatus.objects.get(notestatus_name="notestatus_1")
        # login testuser
        self.client.login(
            username="testuser_notestatus", password="HABbKEVhT9iNeMYv4q9l"
        )
        # get response
        response = self.client.get(
            "/notestatus/" + str(notestatus_1.notestatus_id) + "/"
        )
        # compare
        self.assertEqual(str(response.context["user"]), "testuser_notestatus")

    def test_notestatus_detail_redirect(self):
        """test detail view"""

        # get object
        notestatus_1 = Notestatus.objects.get(notestatus_name="notestatus_1")
        # login testuser
        self.client.login(
            username="testuser_notestatus", password="HABbKEVhT9iNeMYv4q9l"
        )
        # create url
        destination = urllib.parse.quote(
            "/notestatus/" + str(notestatus_1.notestatus_id) + "/", safe="/"
        )
        # get response
        response = self.client.get(
            "/notestatus/" + str(notestatus_1.notestatus_id), follow=True
        )
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )
