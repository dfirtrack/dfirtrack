import urllib.parse

from django.contrib.auth.models import User
from django.test import TestCase

from dfirtrack_main.models import Casetype


class CasetypeViewTestCase(TestCase):
    """casetype view tests"""

    @classmethod
    def setUpTestData(cls):

        # create object
        Casetype.objects.create(casetype_name="casetype_1")
        # create user
        User.objects.create_user(
            username="testuser_casetype", password="zI9vhT7Z0HlzJeOPlO3F"
        )

    def test_casetype_list_not_logged_in(self):
        """test list view"""

        # create url
        destination = "/login/?next=" + urllib.parse.quote("/casetype/", safe="")
        # get response
        response = self.client.get("/casetype/", follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_casetype_list_logged_in(self):
        """test list view"""

        # login testuser
        self.client.login(username="testuser_casetype", password="zI9vhT7Z0HlzJeOPlO3F")
        # get response
        response = self.client.get("/casetype/")
        # compare
        self.assertEqual(response.status_code, 200)

    def test_casetype_list_template(self):
        """test list view"""

        # login testuser
        self.client.login(username="testuser_casetype", password="zI9vhT7Z0HlzJeOPlO3F")
        # get response
        response = self.client.get("/casetype/")
        # compare
        self.assertTemplateUsed(response, "dfirtrack_main/casetype/casetype_list.html")

    def test_casetype_list_get_user_context(self):
        """test list view"""

        # login testuser
        self.client.login(username="testuser_casetype", password="zI9vhT7Z0HlzJeOPlO3F")
        # get response
        response = self.client.get("/casetype/")
        # compare
        self.assertEqual(str(response.context["user"]), "testuser_casetype")

    def test_casetype_list_redirect(self):
        """test list view"""

        # login testuser
        self.client.login(username="testuser_casetype", password="zI9vhT7Z0HlzJeOPlO3F")
        # create url
        destination = urllib.parse.quote("/casetype/", safe="/")
        # get response
        response = self.client.get("/casetype", follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )

    def test_casetype_detail_not_logged_in(self):
        """test detail view"""

        # get object
        casetype_1 = Casetype.objects.get(casetype_name="casetype_1")
        # create url
        destination = "/login/?next=" + urllib.parse.quote(
            "/casetype/detail/" + str(casetype_1.casetype_id) + "/", safe=""
        )
        # get response
        response = self.client.get(
            "/casetype/detail/" + str(casetype_1.casetype_id) + "/", follow=True
        )
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_casetype_detail_logged_in(self):
        """test detail view"""

        # get object
        casetype_1 = Casetype.objects.get(casetype_name="casetype_1")
        # login testuser
        self.client.login(username="testuser_casetype", password="zI9vhT7Z0HlzJeOPlO3F")
        # get response
        response = self.client.get(
            "/casetype/detail/" + str(casetype_1.casetype_id) + "/"
        )
        # compare
        self.assertEqual(response.status_code, 200)

    def test_casetype_detail_template(self):
        """test detail view"""

        # get object
        casetype_1 = Casetype.objects.get(casetype_name="casetype_1")
        # login testuser
        self.client.login(username="testuser_casetype", password="zI9vhT7Z0HlzJeOPlO3F")
        # get response
        response = self.client.get(
            "/casetype/detail/" + str(casetype_1.casetype_id) + "/"
        )
        # compare
        self.assertTemplateUsed(
            response, "dfirtrack_main/casetype/casetype_detail.html"
        )

    def test_casetype_detail_get_user_context(self):
        """test detail view"""

        # get object
        casetype_1 = Casetype.objects.get(casetype_name="casetype_1")
        # login testuser
        self.client.login(username="testuser_casetype", password="zI9vhT7Z0HlzJeOPlO3F")
        # get response
        response = self.client.get(
            "/casetype/detail/" + str(casetype_1.casetype_id) + "/"
        )
        # compare
        self.assertEqual(str(response.context["user"]), "testuser_casetype")

    def test_casetype_detail_redirect(self):
        """test detail view"""

        # get object
        casetype_1 = Casetype.objects.get(casetype_name="casetype_1")
        # login testuser
        self.client.login(username="testuser_casetype", password="zI9vhT7Z0HlzJeOPlO3F")
        # create url
        destination = urllib.parse.quote(
            "/casetype/detail/" + str(casetype_1.casetype_id) + "/", safe="/"
        )
        # get response
        response = self.client.get(
            "/casetype/detail/" + str(casetype_1.casetype_id), follow=True
        )
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )

    def test_casetype_create_not_logged_in(self):
        """test create view"""

        # create url
        destination = "/login/?next=" + urllib.parse.quote("/casetype/create/", safe="")
        # get response
        response = self.client.get("/casetype/create/", follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_casetype_create_logged_in(self):
        """test create view"""

        # login testuser
        self.client.login(username="testuser_casetype", password="zI9vhT7Z0HlzJeOPlO3F")
        # get response
        response = self.client.get("/casetype/create/")
        # compare
        self.assertEqual(response.status_code, 200)

    def test_casetype_create_template(self):
        """test create view"""

        # login testuser
        self.client.login(username="testuser_casetype", password="zI9vhT7Z0HlzJeOPlO3F")
        # get response
        response = self.client.get("/casetype/create/")
        # compare
        self.assertTemplateUsed(response, "dfirtrack_main/generic_form.html")

    def test_casetype_create_get_user_context(self):
        """test create view"""

        # login testuser
        self.client.login(username="testuser_casetype", password="zI9vhT7Z0HlzJeOPlO3F")
        # get response
        response = self.client.get("/casetype/create/")
        # compare
        self.assertEqual(str(response.context["user"]), "testuser_casetype")

    def test_casetype_create_redirect(self):
        """test create view"""

        # login testuser
        self.client.login(username="testuser_casetype", password="zI9vhT7Z0HlzJeOPlO3F")
        # create url
        destination = urllib.parse.quote("/casetype/create/", safe="/")
        # get response
        response = self.client.get("/casetype/create", follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )

    def test_casetype_create_post_redirect(self):
        """test create view"""

        # login testuser
        self.client.login(username="testuser_casetype", password="zI9vhT7Z0HlzJeOPlO3F")
        # create post data
        data_dict = {
            "casetype_name": "casetype_create_post_test",
        }
        # get response
        response = self.client.post("/casetype/create/", data_dict)
        # get casetype
        casetype_id = Casetype.objects.get(
            casetype_name="casetype_create_post_test"
        ).casetype_id
        # create url
        destination = urllib.parse.quote(
            "/casetype/detail/" + str(casetype_id) + "/", safe="/"
        )
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_casetype_create_post_invalid_reload(self):
        """test create view"""

        # login testuser
        self.client.login(username="testuser_casetype", password="zI9vhT7Z0HlzJeOPlO3F")
        # create post data
        data_dict = {}
        # get response
        response = self.client.post("/casetype/create/", data_dict)
        # compare
        self.assertEqual(response.status_code, 200)

    def test_casetype_create_post_invalid_template(self):
        """test create view"""

        # login testuser
        self.client.login(username="testuser_casetype", password="zI9vhT7Z0HlzJeOPlO3F")
        # create post data
        data_dict = {}
        # get response
        response = self.client.post("/casetype/create/", data_dict)
        # compare
        self.assertTemplateUsed(response, "dfirtrack_main/generic_form.html")

    def test_casetype_add_popup_not_logged_in(self):
        """test add view"""

        # create url
        destination = "/login/?next=" + urllib.parse.quote(
            "/casetype/add_popup/", safe=""
        )
        # get response
        response = self.client.get("/casetype/add_popup/", follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_casetype_add_popup_logged_in(self):
        """test add view"""

        # login testuser
        self.client.login(username="testuser_casetype", password="zI9vhT7Z0HlzJeOPlO3F")
        # get response
        response = self.client.get("/casetype/add_popup/")
        # compare
        self.assertEqual(response.status_code, 200)

    def test_casetype_add_popup_template(self):
        """test add view"""

        # login testuser
        self.client.login(username="testuser_casetype", password="zI9vhT7Z0HlzJeOPlO3F")
        # get response
        response = self.client.get("/casetype/add_popup/")
        # compare
        self.assertTemplateUsed(response, "dfirtrack_main/generic_form_popup.html")

    def test_casetype_add_popup_get_user_context(self):
        """test add view"""

        # login testuser
        self.client.login(username="testuser_casetype", password="zI9vhT7Z0HlzJeOPlO3F")
        # get response
        response = self.client.get("/casetype/add_popup/")
        # compare
        self.assertEqual(str(response.context["user"]), "testuser_casetype")

    def test_casetype_add_popup_redirect(self):
        """test add view"""

        # login testuser
        self.client.login(username="testuser_casetype", password="zI9vhT7Z0HlzJeOPlO3F")
        # create url
        destination = urllib.parse.quote("/casetype/add_popup/", safe="/")
        # get response
        response = self.client.get("/casetype/add_popup", follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )

    def test_casetype_add_popup_post_redirect(self):
        """test add view"""

        # login testuser
        self.client.login(username="testuser_casetype", password="zI9vhT7Z0HlzJeOPlO3F")
        # create post data
        data_dict = {
            "casetype_name": "casetype_add_popup_post_test",
        }
        # get response
        response = self.client.post("/casetype/add_popup/", data_dict)
        # compare
        self.assertEqual(response.status_code, 200)

    def test_casetype_add_popup_post_invalid_reload(self):
        """test add view"""

        # login testuser
        self.client.login(username="testuser_casetype", password="zI9vhT7Z0HlzJeOPlO3F")
        # create post data
        data_dict = {}
        # get response
        response = self.client.post("/casetype/add_popup/", data_dict)
        # compare
        self.assertEqual(response.status_code, 200)

    def test_casetype_add_popup_post_invalid_template(self):
        """test add view"""

        # login testuser
        self.client.login(username="testuser_casetype", password="zI9vhT7Z0HlzJeOPlO3F")
        # create post data
        data_dict = {}
        # get response
        response = self.client.post("/casetype/add_popup/", data_dict)
        # compare
        self.assertTemplateUsed(response, "dfirtrack_main/generic_form_popup.html")

    def test_casetype_update_not_logged_in(self):
        """test update view"""

        # get object
        casetype_1 = Casetype.objects.get(casetype_name="casetype_1")
        # create url
        destination = "/login/?next=" + urllib.parse.quote(
            "/casetype/update/" + str(casetype_1.casetype_id) + "/", safe=""
        )
        # get response
        response = self.client.get(
            "/casetype/update/" + str(casetype_1.casetype_id) + "/", follow=True
        )
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_casetype_update_logged_in(self):
        """test update view"""

        # get object
        casetype_1 = Casetype.objects.get(casetype_name="casetype_1")
        # login testuser
        self.client.login(username="testuser_casetype", password="zI9vhT7Z0HlzJeOPlO3F")
        # get response
        response = self.client.get(
            "/casetype/update/" + str(casetype_1.casetype_id) + "/"
        )
        # compare
        self.assertEqual(response.status_code, 200)

    def test_casetype_update_template(self):
        """test update view"""

        # get object
        casetype_1 = Casetype.objects.get(casetype_name="casetype_1")
        # login testuser
        self.client.login(username="testuser_casetype", password="zI9vhT7Z0HlzJeOPlO3F")
        # get response
        response = self.client.get(
            "/casetype/update/" + str(casetype_1.casetype_id) + "/"
        )
        # compare
        self.assertTemplateUsed(response, "dfirtrack_main/generic_form.html")

    def test_casetype_update_get_user_context(self):
        """test update view"""

        # get object
        casetype_1 = Casetype.objects.get(casetype_name="casetype_1")
        # login testuser
        self.client.login(username="testuser_casetype", password="zI9vhT7Z0HlzJeOPlO3F")
        # get response
        response = self.client.get(
            "/casetype/update/" + str(casetype_1.casetype_id) + "/"
        )
        # compare
        self.assertEqual(str(response.context["user"]), "testuser_casetype")

    def test_casetype_update_redirect(self):
        """test update view"""

        # get object
        casetype_1 = Casetype.objects.get(casetype_name="casetype_1")
        # login testuser
        self.client.login(username="testuser_casetype", password="zI9vhT7Z0HlzJeOPlO3F")
        # create url
        destination = urllib.parse.quote(
            "/casetype/update/" + str(casetype_1.casetype_id) + "/", safe="/"
        )
        # get response
        response = self.client.get(
            "/casetype/update/" + str(casetype_1.casetype_id), follow=True
        )
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )

    def test_casetype_update_post_redirect(self):
        """test update view"""

        # login testuser
        self.client.login(username="testuser_casetype", password="zI9vhT7Z0HlzJeOPlO3F")
        # create object
        casetype_id = Casetype.objects.create(
            casetype_name="casetype_update_post_test_1"
        ).casetype_id
        # create post data
        data_dict = {
            "casetype_name": "casetype_update_post_test_2",
        }
        # get response
        response = self.client.post(
            "/casetype/update/" + str(casetype_id) + "/", data_dict
        )
        # create url
        destination = urllib.parse.quote(
            "/casetype/detail/" + str(casetype_id) + "/", safe="/"
        )
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_casetype_update_post_invalid_reload(self):
        """test update view"""

        # login testuser
        self.client.login(username="testuser_casetype", password="zI9vhT7Z0HlzJeOPlO3F")
        # get object
        casetype_id = Casetype.objects.get(casetype_name="casetype_1").casetype_id
        # create post data
        data_dict = {}
        # get response
        response = self.client.post(
            "/casetype/update/" + str(casetype_id) + "/", data_dict
        )
        # compare
        self.assertEqual(response.status_code, 200)

    def test_casetype_update_post_invalid_template(self):
        """test update view"""

        # login testuser
        self.client.login(username="testuser_casetype", password="zI9vhT7Z0HlzJeOPlO3F")
        # get object
        casetype_id = Casetype.objects.get(casetype_name="casetype_1").casetype_id
        # create post data
        data_dict = {}
        # get response
        response = self.client.post(
            "/casetype/update/" + str(casetype_id) + "/", data_dict
        )
        # compare
        self.assertTemplateUsed(response, "dfirtrack_main/generic_form.html")
