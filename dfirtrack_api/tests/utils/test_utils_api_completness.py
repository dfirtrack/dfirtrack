import yaml
from django.test import TestCase


class DFIRTrackUtilityAPICompletnessTestCase(TestCase):
    """
    Test case for the utlity that helps to determine
    the completness of the API
    """

    @classmethod
    def setUpTestData(cls):
        # load openapi specification
        pass

    def test_load_openapi_specification(self):
        with open('dfirtrack_api/openapi/openapi_dfirtrack.yml') as spec:
            try:
                openapiSpec = yaml.safe_load(spec)
            except yaml.YAMLError as e:
                print(e)

            self.assertIsNotNone(openapiSpec)
