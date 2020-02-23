from dfirtrack_api.serializers.dfirtrack_main import AnalysisstatusSerializer, IpSerializer, OsSerializer, SystemSerializer, TagSerializer
from dfirtrack_main.models import Analysisstatus, Ip, Os, System, Tag
from rest_framework import generics

class AnalysisstatusListApi(generics.ListCreateAPIView):
    """ all objects, allowed: GET + POST """

    queryset = Analysisstatus.objects.all()
    serializer_class = AnalysisstatusSerializer

class AnalysisstatusDetailApi(generics.RetrieveUpdateAPIView):
    """ single object, allowed: GET + PUT"""

    queryset = Analysisstatus.objects.all()
    serializer_class = AnalysisstatusSerializer

class IpListApi(generics.ListCreateAPIView):
    """ all objects, allowed: GET + POST """

    queryset = Ip.objects.all()
    serializer_class = IpSerializer

class OsListApi(generics.ListCreateAPIView):
    """ all objects, allowed: GET + POST """

    queryset = Os.objects.all()
    serializer_class = OsSerializer

class SystemListApi(generics.ListAPIView):
    """ all objects, allowed: GET """

    queryset = System.objects.all()
    serializer_class = SystemSerializer

class SystemDetailApi(generics.RetrieveAPIView):
    """ single object, allowed: GET """

    queryset = System.objects.all()
    serializer_class = SystemSerializer

class TagListApi(generics.ListAPIView):
    """ all objects, allowed: GET """

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
