import urllib.parse

from django.contrib.auth.models import User
from django.test import TestCase


class DFIRTrackDocsViewTestCase(TestCase):
    """DFIRTrack Docs 3 view tests"""

    @classmethod
    def setUpTestData(cls):

        # create user
        User.objects.create_user(
            username="testuser_docs_api_1", password="HjN6UbLPpdhIrMXXknd9"
        )

    # TODO: unauthorized access for some reason returns 200 followed by 401
    # TODO: test with 'assertRedirects' did not work as well
    #    def test_docs_api_view_unauthorized(self):
    #        """ unauthorized access is forbidden """
    #
    #        # get response
    #        response = self.client.get('/api/docs/')
    #        # compare
    #        self.assertEqual(response.status_code, 401)

    def test_docs_api_view_authorized_method_get(self):
        """GET is allowed"""

        # login test user
        response = self.client.login(
            username="testuser_docs_api_1", password="HjN6UbLPpdhIrMXXknd9"
        )
        # get response
        response = self.client.get("/api/docs/")
        # compare
        self.assertEqual(response.status_code, 200)

    def test_docs_api_view_authorized_method_post(self):
        """POST is forbidden"""

        # login testuser
        self.client.login(
            username="testuser_docs_api_1", password="HjN6UbLPpdhIrMXXknd9"
        )
        # create POST string
        poststring = {"docs_var": "docs_value"}
        # get response
        response = self.client.post("/api/docs/", data=poststring)
        # compare
        self.assertEqual(response.status_code, 405)

    def test_docs_api_view_authorized_redirect(self):
        """test redirect with appending slash"""

        # login testuser
        self.client.login(
            username="testuser_docs_api_1", password="HjN6UbLPpdhIrMXXknd9"
        )
        # create url
        destination = urllib.parse.quote("/api/docs/", safe="/")
        # get response
        response = self.client.get("/api/docs", follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )
