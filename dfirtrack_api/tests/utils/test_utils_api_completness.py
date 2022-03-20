from django.test import TestCase
from dfirtrack_api.utils.api_completeness import DFIRTrackOpenAPISpecification


class DFIRTrackUtilityAPICompletnessTestCase(TestCase):
    """
    Test case for the utlity that helps to determine
    the completness of the API
    """

    @classmethod
    def setUpTestData(cls):
        pass

    def test_check_openapi_specification_path(self):
        # setup
        spec = DFIRTrackOpenAPISpecification()

        # assert
        self.assertEqual(spec.OPENAPI_DEFINITION_FILE, "dfirtrack_api/openapi/openapi_dfirtrack.yml")

        # Cleanup - not needed

    def test_load_openapi_specification(self):
        # setup
        spec = DFIRTrackOpenAPISpecification()
        # work
        spec.load()

        # assert
        self.assertIsNotNone = spec.OPENAPI_SPECIFICATION

        # Setup
