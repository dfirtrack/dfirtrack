from rest_framework.schemas.openapi import SchemaGenerator as JSONAPISchemaGenerator
from dfirtrack_main.templatetags.dfirtrack_main_tags import dfirtrack_version

class SchemaGenerator(JSONAPISchemaGenerator):
    """
    Extend the schema to include some documentation and override not-yet-implemented security, this has been
    copied from https://columbia-it-django-jsonapi-training.readthedocs.io/en/latest/documenting-api/.

    """
    def get_schema(self, request, public):
        schema = super().get_schema(request, public)
        schema['info'] = {
            'version': dfirtrack_version(),
            'title': 'DFIRTrack',
            'description': 'OpenAPI 3 - Documentation of DFIRTrack API',
        }
        # temporarily add securitySchemes until implemented upstream
        if 'securitySchemes' not in schema['components']:
            schema['components']['securitySchemes'] = {
                'basicAuth': {
                    'type': 'http',
                    'scheme': 'basic',
                    'description': 'basic authentication',
                },
                'bearerAuth': {
                    'type': 'http',
                    'name': 'Token',
                    'description': 'API Token authentication'
                },
            }

        # temporarily add default security object at top-level
        if 'security' not in schema:
            schema['security'] = [
                {'basicAuth': []},
                {'bearerAuth': []},
            ]

        return schema