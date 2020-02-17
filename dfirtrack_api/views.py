from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from dfirtrack_main.models import System

class SystemListApi(APIView):

    # define API view (only) for GET request
    def get(self, request, format=None):

        # get all system objects
        system = System.objects.all()
        # create serializer for all systems from serializers.py
        serializer = serializers.SystemSerializer(system, many=True)
        return Response(serializer.data)

class SystemDetailApi(APIView):

    # define API view (only) for GET request
    def get(self, request, pk, format=None):

        # get system objects
        system = System.objects.get(system_id = pk)
        # create serializer for single system
        serializer = serializers.SystemSerializer(system)
        return Response(serializer.data)
