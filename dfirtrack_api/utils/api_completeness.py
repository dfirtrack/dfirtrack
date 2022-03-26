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

    def get_schema_object_names(self):
        """
        Return a list of all names of the schema objects
        that are defined in openapi specification
        """
        schemas = []
        for s in self.schema_objects:
            schemas.append(s)
        return sorted(schemas)


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
        Return the number of models that are loaded
        """
        return self.count

    def get_models(self):
        """
        Return the models
        """
        return self.models

    def get_models_names(self):
        """
        Returns a sorted list of all
        model names
        """
        names = []
        for m in self.models:
            names.append(m.__name__)
        return sorted(names)
