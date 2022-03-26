from tkinter import W
from django.test import TestCase
from dfirtrack_api.utils.api_completeness import DFIRTrackOpenAPISpecification, DFIRTrackModels
from dfirtrack_main.templatetags import dfirtrack_main_tags


class DFIRTrackUtilityAPICompletnessTestCase(TestCase):
    """
    Test case for the utlity that helps to determine
    the completness of the API
    """

    @classmethod
    def setUpTestData(cls):
        pass

    def test_check_openapi_specification_path(self):
        """
        Test that the default openapi specification path is correct
        """

        # Setup
        spec = DFIRTrackOpenAPISpecification()
        desired = 'dfirtrack_api/openapi/openapi_dfirtrack.yml'

        # Exercise
        actual = spec.OPENAPI_DEFINITION_FILE

        # Verify
        self.assertEqual(actual, desired)

        # Cleanup - not needed

    def test_load_openapi_specification(self):
        """ Test that the loading of the openapi specification works """

        # Setup
        spec = DFIRTrackOpenAPISpecification()

        # Exercise
        spec.load()
        actual = spec.OPENAPI_SPECIFICATION

        # Verify
        self.assertIsNotNone(actual)

        # Cleanup - not needed

    def test_compare_openapi_spec_uptodate_version(self):
        """
        Check that the OPENAPI specification is uptodate
        and is the same as the dfirtrack version used
        """

        # Setup
        spec = DFIRTrackOpenAPISpecification()
        desired = dfirtrack_main_tags.dfirtrack_version()

        # Exercise
        spec.load()
        actual = spec.get_version()

        # Verify
        self.assertEqual(desired, actual)

        # Cleanup - None needed

    def test_retrieve_dfirtrack_django_models(self):
        """
        Test that all models that are available in DFIRTrack
        from all available django apps can be loaded
        """
        # Setup
        dfir_models = DFIRTrackModels()

        # Exercise
        actual = dfir_models.count

        # Verifiy
        self.assertGreater(actual, 0)

        # Cleanup - Not needed

    def test_load_openapi_schemaobjects(self):
        """
        Load the schema objects that have been defined in the OpenAPI specifiaction
        """

        # Setup
        spec = DFIRTrackOpenAPISpecification()
        spec.load()
        desired = 'Artifact'

        # Exercise
        actual = spec.get_schema_objects()

        # Verifiy
        self.assertIn(desired, actual)

        # Cleanup - Not needed
