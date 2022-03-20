import yaml


class DFIRTrackOpenAPISpecification(object):

    def __init__(self):
        # set path to openapi specification file
        self.OPENAPI_DEFINITION_FILE = 'dfirtrack_api/openapi/openapi_dfirtrack.yml'
        self.OPENAPI_SPECIFICATION = None

    def load(self):
        """
        Load the DFIRTrack OpenAPI specification
        """

        with open(self.OPENAPI_DEFINITION_FILE) as spec:
            try:
                self.OPENAPI_SPECIFICATION = yaml.safe_load(spec)
            except yaml.YAMLError as e:
                print(e)

        return None
