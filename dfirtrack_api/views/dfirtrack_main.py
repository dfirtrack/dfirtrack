from dfirtrack_api.serializers import dfirtrack_main
from dfirtrack_main.models import Ip, Os, System, Tag
from rest_framework import generics

class IpListApi(generics.ListCreateAPIView):
    """ all objects, allowed: GET + POST """

    queryset = Ip.objects.all()
    serializer_class = dfirtrack_main.IpSerializer

class OsListApi(generics.ListCreateAPIView):
    """ all objects, allowed: GET + POST """

    queryset = Os.objects.all()
    serializer_class = dfirtrack_main.OsSerializer

class SystemListApi(generics.ListAPIView):
    """ all objects, allowed: GET """

    queryset = System.objects.all()
    serializer_class = dfirtrack_main.SystemSerializer

class SystemDetailApi(generics.RetrieveAPIView):
    """ single object, allowed: GET """

    queryset = System.objects.all()
    serializer_class = dfirtrack_main.SystemSerializer

class TagListApi(generics.ListAPIView):
    """ all objects, allowed: GET """

    queryset = Tag.objects.all()
    serializer_class = dfirtrack_main.TagSerializer
