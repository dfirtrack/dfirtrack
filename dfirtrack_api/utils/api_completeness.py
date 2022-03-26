import yaml
from django.apps import apps


class DFIRTrackOpenAPISpecification(object):
    """
    Class to work with the DFIRTrack OpenAPI
    specification file
    """

    def __init__(self):
        # set path to openapi specification file
        self.OPENAPI_DEFINITION_FILE = 'dfirtrack_api/openapi/openapi_dfirtrack.yml'
        self.OPENAPI_SPECIFICATION = None
        self.dfirtrack_version = None
        self.schema_objects = None
        self.load()

    def load(self):
        """
        Load the DFIRTrack OpenAPI specification
        """

        with open(self.OPENAPI_DEFINITION_FILE) as spec:
            try:
                self.OPENAPI_SPECIFICATION = yaml.safe_load(spec)
            except yaml.YAMLError as e:
                print(e)

        # load specific important values from specification
        self.dfirtrack_version = self.OPENAPI_SPECIFICATION['info']['version']
        self.schema_objects = self.OPENAPI_SPECIFICATION['components']['schemas']

        return None

    def get_version(self):
        """
        Retrieves the DFIRTrack version from the OpenAPI specification
        """
        return self.dfirtrack_version

    def get_schema_objects(self):
        """
        Method that retrieves the openapi schema_objects
        """
        return self.schema_objects


class DFIRTrackModels(object):
    """
    Class that holds all the DFIRTrack models in use
    """

    def __init__(self):
        """
        Load the models from all DFIRTrack apps
        """
        self.models = apps.get_models()
        self.count = len(self.models)

    def count(self):
        """
        Return the numer of models that are loaded
        """
        return self.count
