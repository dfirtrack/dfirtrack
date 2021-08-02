import urllib.parse

from django.contrib.auth.models import User
from django.test import TestCase

from dfirtrack_main.models import Casepriority


class CasepriorityAPIViewTestCase(TestCase):
    """casepriority API view tests"""

    @classmethod
    def setUpTestData(cls):

        # create object
        Casepriority.objects.create(casepriority_name="casepriority_api_1")
        # create user
        User.objects.create_user(
            username="testuser_casepriority_api", password="IkVd4MCMYIlTf5MbCiF8"
        )

    def test_casepriority_list_api_unauthorized(self):
        """unauthorized access is forbidden"""

        # get response
        response = self.client.get("/api/casepriority/")
        # compare
        self.assertEqual(response.status_code, 401)

    def test_casepriority_list_api_method_get(self):
        """GET is allowed"""

        # login testuser
        self.client.login(
            username="testuser_casepriority_api", password="IkVd4MCMYIlTf5MbCiF8"
        )
        # get response
        response = self.client.get("/api/casepriority/")
        # compare
        self.assertEqual(response.status_code, 200)

    def test_casepriority_list_api_method_post(self):
        """POST is forbidden"""

        # login testuser
        self.client.login(
            username="testuser_casepriority_api", password="IkVd4MCMYIlTf5MbCiF8"
        )
        # create POST string
        poststring = {"casepriority_name": "casepriority_api_2"}
        # get response
        response = self.client.post("/api/casepriority/", data=poststring)
        # compare
        self.assertEqual(response.status_code, 405)

    def test_casepriority_list_api_redirect(self):
        """test redirect with appending slash"""

        # login testuser
        self.client.login(
            username="testuser_casepriority_api", password="IkVd4MCMYIlTf5MbCiF8"
        )
        # create url
        destination = urllib.parse.quote("/api/casepriority/", safe="/")
        # get response
        response = self.client.get("/api/casepriority", follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )

    def test_casepriority_detail_api_unauthorized(self):
        """unauthorized access is forbidden"""

        # get object
        casepriority_api_1 = Casepriority.objects.get(
            casepriority_name="casepriority_api_1"
        )
        # get response
        response = self.client.get(
            "/api/casepriority/" + str(casepriority_api_1.casepriority_id) + "/"
        )
        # compare
        self.assertEqual(response.status_code, 401)

    def test_casepriority_detail_api_method_get(self):
        """GET is allowed"""

        # get object
        casepriority_api_1 = Casepriority.objects.get(
            casepriority_name="casepriority_api_1"
        )
        # login testuser
        self.client.login(
            username="testuser_casepriority_api", password="IkVd4MCMYIlTf5MbCiF8"
        )
        # get response
        response = self.client.get(
            "/api/casepriority/" + str(casepriority_api_1.casepriority_id) + "/"
        )
        # compare
        self.assertEqual(response.status_code, 200)

    def test_casepriority_detail_api_method_delete(self):
        """DELETE is forbidden"""

        # get object
        casepriority_api_1 = Casepriority.objects.get(
            casepriority_name="casepriority_api_1"
        )
        # login testuser
        self.client.login(
            username="testuser_casepriority_api", password="IkVd4MCMYIlTf5MbCiF8"
        )
        # get response
        response = self.client.delete(
            "/api/casepriority/" + str(casepriority_api_1.casepriority_id) + "/"
        )
        # compare
        self.assertEqual(response.status_code, 405)

    def test_casepriority_detail_api_method_put(self):
        """PUT is forbidden"""

        # get object
        casepriority_api_1 = Casepriority.objects.get(
            casepriority_name="casepriority_api_1"
        )
        # login testuser
        self.client.login(
            username="testuser_casepriority_api", password="IkVd4MCMYIlTf5MbCiF8"
        )
        # create url
        destination = urllib.parse.quote(
            "/api/casepriority/" + str(casepriority_api_1.casepriority_id) + "/",
            safe="/",
        )
        # create PUT string
        putstring = {"casepriority_name": "new_casepriority_api_1"}
        # get response
        response = self.client.put(
            destination, data=putstring, content_type="application/json"
        )
        # compare
        self.assertEqual(response.status_code, 405)

    def test_casepriority_detail_api_redirect(self):
        """test redirect with appending slash"""

        # get object
        casepriority_api_1 = Casepriority.objects.get(
            casepriority_name="casepriority_api_1"
        )
        # login testuser
        self.client.login(
            username="testuser_casepriority_api", password="IkVd4MCMYIlTf5MbCiF8"
        )
        # create url
        destination = urllib.parse.quote(
            "/api/casepriority/" + str(casepriority_api_1.casepriority_id) + "/",
            safe="/",
        )
        # get response
        response = self.client.get(
            "/api/casepriority/" + str(casepriority_api_1.casepriority_id), follow=True
        )
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )
