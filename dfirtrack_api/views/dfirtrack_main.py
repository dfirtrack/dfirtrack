from dfirtrack_api.serializers import dfirtrack_main
from dfirtrack_main.models import Ip, Os, System, Tag
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class IpListApi(APIView):

    def get(self, request, format=None):
        """ define API view for GET request """

        # get all objects
        ip = Ip.objects.all()
        # create serializer for all objects
        serializer = dfirtrack_main.IpSerializer(ip, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        """ define API view for POST request """

        serializer = dfirtrack_main.IpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OsListApi(APIView):

    def get(self, request, format=None):
        """ define API view for GET request """

        # get all objects
        os = Os.objects.all()
        # create serializer for all objects
        serializer = dfirtrack_main.OsSerializer(os, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        """ define API view for POST request """

        serializer = dfirtrack_main.OsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SystemListApi(APIView):
    """ all objects """

    def get(self, request, format=None):
        """ define API view for GET request """

        # get all objects
        system = System.objects.all()
        # create serializer for all objects
        serializer = dfirtrack_main.SystemSerializer(system, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class SystemDetailApi(APIView):

    def get(self, request, pk, format=None):
        """ define API view for GET request """

        # get object
        try:
            system = System.objects.get(system_id = pk)
            # create serializer for single object
            serializer = dfirtrack_main.SystemSerializer(system)
            return Response(serializer.data)
        except System.DoesNotExist:
            raise Http404

class TagListApi(APIView):

    def get(self, request, format=None):
        """ define API view for GET request """

        # get all objects
        tag = Tag.objects.all()
        # create serializer for all objects
        serializer = dfirtrack_main.TagSerializer(tag, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
