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

        try:

            # get object
            artifact = Artifact.objects.get(artifact_id = pk)

            # create serializer for single object
            serializer = dfirtrack_artifacts.ArtifactSerializer(artifact)
            return Response(serializer.data)

        except Artifact.DoesNotExist:

            # error message if object does not exist
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

    def post(self, request, format=None):
        """ define API view for POST request """

        # create serializer from request data
        serializer = dfirtrack_artifacts.ArtifactstatusSerializer(data=request.data)

        # save object
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # error message for invalid data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArtifactstatusDetailApi(APIView):
    """ single object """

    def get(self, request, pk, format=None):
        """ define API view for GET request """

        try:

            # get object
            artifactstatus = Artifactstatus.objects.get(artifactstatus_id = pk)

            # create serializer for single object
            serializer = dfirtrack_artifacts.ArtifactstatusSerializer(artifactstatus)
            return Response(serializer.data)

        except Artifactstatus.DoesNotExist:

            # error message if object does not exist
            raise Http404

    def put(self, request, pk, format=None):
        """ define API view for PUT request """

        try:

            # get object
            artifactstatus = Artifactstatus.objects.get(artifactstatus_id = pk)

            # create serializer for single object
            serializer = dfirtrack_artifacts.ArtifactstatusSerializer(artifactstatus, data=request.data)

            if serializer.is_valid():
                # save object
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # object does not exist
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

    def post(self, request, format=None):
        """ define API view for POST request """

        # create serializer from request data
        serializer = dfirtrack_artifacts.ArtifacttypeSerializer(data=request.data)

        # save object
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # error message for invalid data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArtifacttypeDetailApi(APIView):
    """ single object """

    def get(self, request, pk, format=None):
        """ define API view for GET request """

        try:

            # get object
            artifacttype = Artifacttype.objects.get(artifacttype_id = pk)

            # create serializer for single object
            serializer = dfirtrack_artifacts.ArtifacttypeSerializer(artifacttype)
            return Response(serializer.data)

        except Artifacttype.DoesNotExist:

            # error message if object does not exist
            raise Http404

    def put(self, request, pk, format=None):
        """ define API view for PUT request """

        try:

            # get object
            artifacttype = Artifacttype.objects.get(artifacttype_id = pk)

            # create serializer for single object
            serializer = dfirtrack_artifacts.ArtifacttypeSerializer(artifacttype, data=request.data)

            if serializer.is_valid():
                # save object
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # object does not exist
        except Artifacttype.DoesNotExist:
            raise Http404
