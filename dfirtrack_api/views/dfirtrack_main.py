from dfirtrack_api.serializers.dfirtrack_main import IpSerializer, OsSerializer, SystemSerializer, TagSerializer
from dfirtrack_main.models import Ip, Os, System, Tag
from rest_framework import generics

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
