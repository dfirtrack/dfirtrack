from dfirtrack_api.serializers import dfirtrack_artifacts
from dfirtrack_artifacts.models import Artifact, Artifactstatus, Artifacttype
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class ArtifactListApi(APIView):
    """ all objects """

    def get(self, request, format=None):
        """ define API view for GET request """

        # get all objects
        artifact = Artifact.objects.all()
        # create serializer for all objects
        serializer = dfirtrack_artifacts.ArtifactSerializer(artifact, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ArtifactDetailApi(APIView):
    """ single object """

    def get(self, request, pk, format=None):
        """ define API view for GET request """

        # get object
        try:
            artifact = Artifact.objects.get(artifact_id = pk)
            # create serializer for single object
            serializer = dfirtrack_artifacts.ArtifactSerializer(artifact)
            return Response(serializer.data)
        except Artifact.DoesNotExist:
            raise Http404

class ArtifactstatusListApi(APIView):
    """ all objects """

    def get(self, request, format=None):
        """ define API view for GET request """

        # get all objects
        artifactstatus = Artifactstatus.objects.all()
        # create serializer for all objects
        serializer = dfirtrack_artifacts.ArtifactstatusSerializer(artifactstatus, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ArtifactstatusDetailApi(APIView):
    """ single object """

    def get(self, request, pk, format=None):
        """ define API view for GET request """

        # get object
        try:
            artifactstatus = Artifactstatus.objects.get(artifactstatus_id = pk)
            # create serializer for single object
            serializer = dfirtrack_artifacts.ArtifactstatusSerializer(artifactstatus)
            return Response(serializer.data)
        except Artifactstatus.DoesNotExist:
            raise Http404

class ArtifacttypeListApi(APIView):
    """ all objects """

    def get(self, request, format=None):
        """ define API view for GET request """

        # get all objects
        artifacttype = Artifacttype.objects.all()
        # create serializer for all objects
        serializer = dfirtrack_artifacts.ArtifacttypeSerializer(artifacttype, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ArtifacttypeDetailApi(APIView):
    """ single object """

    def get(self, request, pk, format=None):
        """ define API view for GET request """

        # get object
        try:
            artifacttype = Artifacttype.objects.get(artifacttype_id = pk)
            # create serializer for single object
            serializer = dfirtrack_artifacts.ArtifacttypeSerializer(artifacttype)
            return Response(serializer.data)
        except Artifacttype.DoesNotExist:
            raise Http404
