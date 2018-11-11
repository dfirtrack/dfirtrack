from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from dfirtrack_main.models import System

class SystemView(APIView):

    # define API view (only) for GET request
    def get(self, request, format=None):

        # get all system objects
        system = System.objects.all()
        # create serializer for all systems from serializers.py
        serializer = serializers.SystemSerializer(system, many=True)
        return Response(serializer.data)
