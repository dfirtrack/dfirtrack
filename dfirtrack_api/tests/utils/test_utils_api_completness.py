from django.test import TestCase

from dfirtrack_api.utils.api_completeness import (
    DFIRTrackModels,
    DFIRTrackOpenAPISpecification,
)
from dfirtrack_main.templatetags import dfirtrack_main_tags


class DFIRTrackUtilityAPICompletnessTestCase(TestCase):
    """
    Test case for the utility that helps to determine
    the completeness of the API
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
        """Test that the loading of the openapi specification works"""

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
        Check that the OPENAPI specification is up-to-date
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

    def test_all_models_exist_in_api(self):
        """
        Test that all main DFIRTrack models exist in OpenAPI
        schema definition and are therefore exposed via API.

        We need to verify that each element of the DFIRTrack models
        are defined in the openapi specification file (actuals), if
        so the models will be exposed via API.

        If this test fails it will mean that a model of DFIRTrack
        is currently not exposed within the API and must be added to that

        Please note if you want to disable the check for a specific module,
        because this should be never exposed via API add it to the EXCEPTIONS
        list
        """

        # Setup
        # The following models will not be checked because they make no sense in the API
        MODEL_EXCEPTIONS = [
            'ArtifactExporterSpreadsheetXlsConfigModel',
            'MainConfigModel',
            'SystemExporterMarkdownConfigModel',
            'SystemExporterSpreadsheetCsvConfigModel',
            'SystemExporterSpreadsheetXlsConfigModel',
            'SystemImporterFileCsvConfigModel',
            'Statushistory',
            'StatushistoryEntry',
            'UserConfigModel',
            'Workflow',
            'WorkflowDefaultArtifactAttributes',
            'WorkflowDefaultTasknameAttributes',
            'ContentType',
            'Failure',
            'Group',
            'LogEntry',
            'OrmQ',
            'Permission',
            'Schedule',
            'Session',
            'Success',
            'Token',
            'TokenProxy',
            'User',
        ]

        all_models = DFIRTrackModels().get_models_names()
        models_filtered = sorted(set(all_models).difference(MODEL_EXCEPTIONS))

        # Exercise
        # Remove exceptions
        actual_schemas = DFIRTrackOpenAPISpecification().get_schema_object_names()

        # Verifiy - stepwise
        for desired in models_filtered:
            self.assertIn(desired, actual_schemas)

        # Cleanup - Not needed
