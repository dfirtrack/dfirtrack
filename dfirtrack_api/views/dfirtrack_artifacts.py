from dfirtrack_api.serializers import dfirtrack_artifacts
from dfirtrack_artifacts.models import Artifact, Artifactstatus, Artifacttype
from rest_framework import generics

class ArtifactListApi(generics.ListAPIView):
    """ all objects, allowed: GET """

    queryset = Artifact.objects.all()
    serializer_class = dfirtrack_artifacts.ArtifactSerializer

class ArtifactDetailApi(generics.RetrieveAPIView):
    """ single object, allowed: GET """

    queryset = Artifact.objects.all()
    serializer_class = dfirtrack_artifacts.ArtifactSerializer

class ArtifactstatusListApi(generics.ListCreateAPIView):
    """ all objects, allowed: GET + POST """

    queryset = Artifactstatus.objects.all()
    serializer_class = dfirtrack_artifacts.ArtifactstatusSerializer

class ArtifactstatusDetailApi(generics.RetrieveUpdateAPIView):
    """ single object, allowed: GET + PUT """

    queryset = Artifactstatus.objects.all()
    serializer_class = dfirtrack_artifacts.ArtifactstatusSerializer

class ArtifacttypeListApi(generics.ListCreateAPIView):
    """ all objects, allowed: GET + POST """

    queryset = Artifacttype.objects.all()
    serializer_class = dfirtrack_artifacts.ArtifacttypeSerializer

class ArtifacttypeDetailApi(generics.RetrieveUpdateAPIView):
    """ single object, allowed: GET + PUT """

    queryset = Artifacttype.objects.all()
    serializer_class = dfirtrack_artifacts.ArtifacttypeSerializer
