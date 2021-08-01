import urllib.parse

from django.contrib.auth.models import User
from django.test import TestCase

from dfirtrack_main.models import Casestatus


class CasestatusAPIViewTestCase(TestCase):
    """casestatus API view tests"""

    @classmethod
    def setUpTestData(cls):

        # create object
        Casestatus.objects.create(casestatus_name="casestatus_api_1")
        # create user
        User.objects.create_user(
            username="testuser_casestatus_api", password="KeJUkN86YJVhEVERfLKs"
        )

    def test_casestatus_list_api_unauthorized(self):
        """unauthorized access is forbidden"""

        # get response
        response = self.client.get("/api/casestatus/")
        # compare
        self.assertEqual(response.status_code, 401)

    def test_casestatus_list_api_method_get(self):
        """GET is allowed"""

        # login testuser
        self.client.login(
            username="testuser_casestatus_api", password="KeJUkN86YJVhEVERfLKs"
        )
        # get response
        response = self.client.get("/api/casestatus/")
        # compare
        self.assertEqual(response.status_code, 200)

    def test_casestatus_list_api_method_post(self):
        """POST is forbidden"""

        # login testuser
        self.client.login(
            username="testuser_casestatus_api", password="KeJUkN86YJVhEVERfLKs"
        )
        # create POST string
        poststring = {"casestatus_name": "casestatus_api_2"}
        # get response
        response = self.client.post("/api/casestatus/", data=poststring)
        # compare
        self.assertEqual(response.status_code, 405)

    def test_casestatus_list_api_redirect(self):
        """test redirect with appending slash"""

        # login testuser
        self.client.login(
            username="testuser_casestatus_api", password="KeJUkN86YJVhEVERfLKs"
        )
        # create url
        destination = urllib.parse.quote("/api/casestatus/", safe="/")
        # get response
        response = self.client.get("/api/casestatus", follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )

    def test_casestatus_detail_api_unauthorized(self):
        """unauthorized access is forbidden"""

        # get object
        casestatus_api_1 = Casestatus.objects.get(casestatus_name="casestatus_api_1")
        # get response
        response = self.client.get(
            "/api/casestatus/" + str(casestatus_api_1.casestatus_id) + "/"
        )
        # compare
        self.assertEqual(response.status_code, 401)

    def test_casestatus_detail_api_method_get(self):
        """GET is allowed"""

        # get object
        casestatus_api_1 = Casestatus.objects.get(casestatus_name="casestatus_api_1")
        # login testuser
        self.client.login(
            username="testuser_casestatus_api", password="KeJUkN86YJVhEVERfLKs"
        )
        # get response
        response = self.client.get(
            "/api/casestatus/" + str(casestatus_api_1.casestatus_id) + "/"
        )
        # compare
        self.assertEqual(response.status_code, 200)

    def test_casestatus_detail_api_method_delete(self):
        """DELETE is forbidden"""

        # get object
        casestatus_api_1 = Casestatus.objects.get(casestatus_name="casestatus_api_1")
        # login testuser
        self.client.login(
            username="testuser_casestatus_api", password="KeJUkN86YJVhEVERfLKs"
        )
        # get response
        response = self.client.delete(
            "/api/casestatus/" + str(casestatus_api_1.casestatus_id) + "/"
        )
        # compare
        self.assertEqual(response.status_code, 405)

    def test_casestatus_detail_api_method_put(self):
        """PUT is forbidden"""

        # get object
        casestatus_api_1 = Casestatus.objects.get(casestatus_name="casestatus_api_1")
        # login testuser
        self.client.login(
            username="testuser_casestatus_api", password="KeJUkN86YJVhEVERfLKs"
        )
        # create url
        destination = urllib.parse.quote(
            "/api/casestatus/" + str(casestatus_api_1.casestatus_id) + "/", safe="/"
        )
        # create PUT string
        putstring = {"casestatus_name": "new_casestatus_api_1"}
        # get response
        response = self.client.put(
            destination, data=putstring, content_type="application/json"
        )
        # compare
        self.assertEqual(response.status_code, 405)

    def test_casestatus_detail_api_redirect(self):
        """test redirect with appending slash"""

        # get object
        casestatus_api_1 = Casestatus.objects.get(casestatus_name="casestatus_api_1")
        # login testuser
        self.client.login(
            username="testuser_casestatus_api", password="KeJUkN86YJVhEVERfLKs"
        )
        # create url
        destination = urllib.parse.quote(
            "/api/casestatus/" + str(casestatus_api_1.casestatus_id) + "/", safe="/"
        )
        # get response
        response = self.client.get(
            "/api/casestatus/" + str(casestatus_api_1.casestatus_id), follow=True
        )
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )
