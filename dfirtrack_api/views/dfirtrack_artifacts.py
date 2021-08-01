from rest_framework import generics

from dfirtrack_api.serializers.dfirtrack_artifacts import (
    ArtifactprioritySerializer,
    ArtifactSerializer,
    ArtifactstatusSerializer,
    ArtifacttypeSerializer,
)
from dfirtrack_artifacts.models import (
    Artifact,
    Artifactpriority,
    Artifactstatus,
    Artifacttype,
)


class ArtifactListApi(generics.ListCreateAPIView):
    """ all objects, allowed: GET + POST """

    queryset = Artifact.objects.all()
    serializer_class = ArtifactSerializer

class ArtifactDetailApi(generics.RetrieveUpdateAPIView):
    """ single object, allowed: GET + PUT """

    queryset = Artifact.objects.all()
    serializer_class = ArtifactSerializer

class ArtifactpriorityListApi(generics.ListAPIView):
    """ all objects, allowed: GET """

    queryset = Artifactpriority.objects.all()
    serializer_class = ArtifactprioritySerializer

class ArtifactpriorityDetailApi(generics.RetrieveAPIView):
    """ single object, allowed: GET """

    queryset = Artifactpriority.objects.all()
    serializer_class = ArtifactprioritySerializer

class ArtifactstatusListApi(generics.ListAPIView):
    """ all objects, allowed: GET """

    queryset = Artifactstatus.objects.all()
    serializer_class = ArtifactstatusSerializer

class ArtifactstatusDetailApi(generics.RetrieveAPIView):
    """ single object, allowed: GET """

    queryset = Artifactstatus.objects.all()
    serializer_class = ArtifactstatusSerializer

class ArtifacttypeListApi(generics.ListCreateAPIView):
    """ all objects, allowed: GET + POST """

    queryset = Artifacttype.objects.all()
    serializer_class = ArtifacttypeSerializer

class ArtifacttypeDetailApi(generics.RetrieveUpdateAPIView):
    """ single object, allowed: GET + PUT """

    queryset = Artifacttype.objects.all()
    serializer_class = ArtifacttypeSerializer
