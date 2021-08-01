import urllib.parse

from django.contrib.auth.models import User
from django.test import TestCase

from dfirtrack_main.models import Taskname


class TasknameAPIViewTestCase(TestCase):
    """taskname API view tests"""

    @classmethod
    def setUpTestData(cls):

        # create object
        Taskname.objects.create(taskname_name="taskname_api_1")
        # create user
        User.objects.create_user(
            username="testuser_taskname_api", password="JUsV9RlTdQkAjLgB4hD1"
        )

    def test_taskname_list_api_unauthorized(self):
        """unauthorized access is forbidden"""

        # get response
        response = self.client.get("/api/taskname/")
        # compare
        self.assertEqual(response.status_code, 401)

    def test_taskname_list_api_method_get(self):
        """GET is allowed"""

        # login testuser
        self.client.login(
            username="testuser_taskname_api", password="JUsV9RlTdQkAjLgB4hD1"
        )
        # get response
        response = self.client.get("/api/taskname/")
        # compare
        self.assertEqual(response.status_code, 200)

    def test_taskname_list_api_method_post(self):
        """POST is allowed"""

        # login testuser
        self.client.login(
            username="testuser_taskname_api", password="JUsV9RlTdQkAjLgB4hD1"
        )
        # create POST string
        poststring = {"taskname_name": "taskname_api_2"}
        # get response
        response = self.client.post("/api/taskname/", data=poststring)
        # compare
        self.assertEqual(response.status_code, 201)

    def test_taskname_list_api_redirect(self):
        """test redirect with appending slash"""

        # login testuser
        self.client.login(
            username="testuser_taskname_api", password="JUsV9RlTdQkAjLgB4hD1"
        )
        # create url
        destination = urllib.parse.quote("/api/taskname/", safe="/")
        # get response
        response = self.client.get("/api/taskname", follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )

    def test_taskname_detail_api_unauthorized(self):
        """unauthorized access is forbidden"""

        # get object
        taskname_api_1 = Taskname.objects.get(taskname_name="taskname_api_1")
        # get response
        response = self.client.get(
            "/api/taskname/" + str(taskname_api_1.taskname_id) + "/"
        )
        # compare
        self.assertEqual(response.status_code, 401)

    def test_taskname_detail_api_method_get(self):
        """GET is allowed"""

        # get object
        taskname_api_1 = Taskname.objects.get(taskname_name="taskname_api_1")
        # login testuser
        self.client.login(
            username="testuser_taskname_api", password="JUsV9RlTdQkAjLgB4hD1"
        )
        # get response
        response = self.client.get(
            "/api/taskname/" + str(taskname_api_1.taskname_id) + "/"
        )
        # compare
        self.assertEqual(response.status_code, 200)

    def test_taskname_detail_api_method_delete(self):
        """DELETE is forbidden"""

        # get object
        taskname_api_1 = Taskname.objects.get(taskname_name="taskname_api_1")
        # login testuser
        self.client.login(
            username="testuser_taskname_api", password="JUsV9RlTdQkAjLgB4hD1"
        )
        # get response
        response = self.client.delete(
            "/api/taskname/" + str(taskname_api_1.taskname_id) + "/"
        )
        # compare
        self.assertEqual(response.status_code, 405)

    def test_taskname_detail_api_method_put(self):
        """PUT is allowed"""

        # get object
        taskname_api_1 = Taskname.objects.get(taskname_name="taskname_api_1")
        # login testuser
        self.client.login(
            username="testuser_taskname_api", password="JUsV9RlTdQkAjLgB4hD1"
        )
        # create url
        destination = urllib.parse.quote(
            "/api/taskname/" + str(taskname_api_1.taskname_id) + "/", safe="/"
        )
        # create PUT string
        putstring = {"taskname_name": "new_taskname_api_1"}
        # get response
        response = self.client.put(
            destination, data=putstring, content_type="application/json"
        )
        # compare
        self.assertEqual(response.status_code, 200)

    def test_taskname_detail_api_redirect(self):
        """test redirect with appending slash"""

        # get object
        taskname_api_1 = Taskname.objects.get(taskname_name="taskname_api_1")
        # login testuser
        self.client.login(
            username="testuser_taskname_api", password="JUsV9RlTdQkAjLgB4hD1"
        )
        # create url
        destination = urllib.parse.quote(
            "/api/taskname/" + str(taskname_api_1.taskname_id) + "/", safe="/"
        )
        # get response
        response = self.client.get(
            "/api/taskname/" + str(taskname_api_1.taskname_id), follow=True
        )
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )
