from dfirtrack_api.serializers import dfirtrack_main as dfirtrack_main_serializers
from dfirtrack_main import models as dfirtrack_main_models
from rest_framework import generics


class AnalysisstatusListApi(generics.ListAPIView):
    """ all objects, allowed: GET """

    queryset = dfirtrack_main_models.Analysisstatus.objects.all()
    serializer_class = dfirtrack_main_serializers.AnalysisstatusSerializer

class AnalysisstatusDetailApi(generics.RetrieveAPIView):
    """ single object, allowed: GET """

    queryset = dfirtrack_main_models.Analysisstatus.objects.all()
    serializer_class = dfirtrack_main_serializers.AnalysisstatusSerializer

class CaseListApi(generics.ListCreateAPIView):
    """ all objects, allowed: GET + POST """

    queryset = dfirtrack_main_models.Case.objects.all()
    serializer_class = dfirtrack_main_serializers.CaseSerializer

class CaseDetailApi(generics.RetrieveUpdateAPIView):
    """ single object, allowed: GET + PUT """

    queryset = dfirtrack_main_models.Case.objects.all()
    serializer_class = dfirtrack_main_serializers.CaseSerializer

class CasepriorityListApi(generics.ListAPIView):
    """ all objects, allowed: GET """

    queryset = dfirtrack_main_models.Casepriority.objects.all()
    serializer_class = dfirtrack_main_serializers.CaseprioritySerializer

class CasepriorityDetailApi(generics.RetrieveAPIView):
    """ single object, allowed: GET """

    queryset = dfirtrack_main_models.Casepriority.objects.all()
    serializer_class = dfirtrack_main_serializers.CaseprioritySerializer

class CasestatusListApi(generics.ListAPIView):
    """ all objects, allowed: GET """

    queryset = dfirtrack_main_models.Casestatus.objects.all()
    serializer_class = dfirtrack_main_serializers.CasestatusSerializer

class CasestatusDetailApi(generics.RetrieveAPIView):
    """ single object, allowed: GET """

    queryset = dfirtrack_main_models.Casestatus.objects.all()
    serializer_class = dfirtrack_main_serializers.CasestatusSerializer

class CasetypeListApi(generics.ListCreateAPIView):
    """ all objects, allowed: GET + POST """

    queryset = dfirtrack_main_models.Casetype.objects.all()
    serializer_class = dfirtrack_main_serializers.CasetypeSerializer

class CasetypeDetailApi(generics.RetrieveUpdateAPIView):
    """ single object, allowed: GET + PUT """

    queryset = dfirtrack_main_models.Casetype.objects.all()
    serializer_class = dfirtrack_main_serializers.CasetypeSerializer

class CompanyListApi(generics.ListCreateAPIView):
    """ all objects, allowed: GET + POST """

    queryset = dfirtrack_main_models.Company.objects.all()
    serializer_class = dfirtrack_main_serializers.CompanySerializer

class CompanyDetailApi(generics.RetrieveUpdateAPIView):
    """ single object, allowed: GET + PUT """

    queryset = dfirtrack_main_models.Company.objects.all()
    serializer_class = dfirtrack_main_serializers.CompanySerializer

class ContactListApi(generics.ListCreateAPIView):
    """ all objects, allowed: GET + POST """

    queryset = dfirtrack_main_models.Contact.objects.all()
    serializer_class = dfirtrack_main_serializers.ContactSerializer

class ContactDetailApi(generics.RetrieveUpdateAPIView):
    """ single object, allowed: GET + PUT """

    queryset = dfirtrack_main_models.Contact.objects.all()
    serializer_class = dfirtrack_main_serializers.ContactSerializer

class DivisionListApi(generics.ListCreateAPIView):
    """ all objects, allowed: GET + POST """

    queryset = dfirtrack_main_models.Division.objects.all()
    serializer_class = dfirtrack_main_serializers.DivisionSerializer

class DivisionDetailApi(generics.RetrieveUpdateAPIView):
    """ single object, allowed: GET + PUT """

    queryset = dfirtrack_main_models.Division.objects.all()
    serializer_class = dfirtrack_main_serializers.DivisionSerializer

class DnsnameListApi(generics.ListCreateAPIView):
    """ all objects, allowed: GET + POST """

    queryset = dfirtrack_main_models.Dnsname.objects.all()
    serializer_class = dfirtrack_main_serializers.DnsnameSerializer

class DnsnameDetailApi(generics.RetrieveUpdateAPIView):
    """ single object, allowed: GET + PUT """

    queryset = dfirtrack_main_models.Dnsname.objects.all()
    serializer_class = dfirtrack_main_serializers.DnsnameSerializer

class DomainListApi(generics.ListCreateAPIView):
    """ all objects, allowed: GET + POST """

    queryset = dfirtrack_main_models.Domain.objects.all()
    serializer_class = dfirtrack_main_serializers.DomainSerializer

class DomainDetailApi(generics.RetrieveUpdateAPIView):
    """ single object, allowed: GET + PUT """

    queryset = dfirtrack_main_models.Domain.objects.all()
    serializer_class = dfirtrack_main_serializers.DomainSerializer

class DomainuserListApi(generics.ListCreateAPIView):
    """ all objects, allowed: GET + POST """

    queryset = dfirtrack_main_models.Domainuser.objects.all()
    serializer_class = dfirtrack_main_serializers.DomainuserSerializer

class DomainuserDetailApi(generics.RetrieveUpdateAPIView):
    """ single object, allowed: GET + PUT """

    queryset = dfirtrack_main_models.Domainuser.objects.all()
    serializer_class = dfirtrack_main_serializers.DomainuserSerializer

class HeadlineListApi(generics.ListCreateAPIView):
    """ all objects, allowed: GET + POST """

    queryset = dfirtrack_main_models.Headline.objects.all()
    serializer_class = dfirtrack_main_serializers.HeadlineSerializer

class HeadlineDetailApi(generics.RetrieveUpdateAPIView):
    """ single object, allowed: GET + PUT """

    queryset = dfirtrack_main_models.Headline.objects.all()
    serializer_class = dfirtrack_main_serializers.HeadlineSerializer

class IpListApi(generics.ListCreateAPIView):
    """ all objects, allowed: GET + POST """

    queryset = dfirtrack_main_models.Ip.objects.all()
    serializer_class = dfirtrack_main_serializers.IpSerializer

class IpDetailApi(generics.RetrieveUpdateAPIView):
    """ single object, allowed: GET + PUT """

    queryset = dfirtrack_main_models.Ip.objects.all()
    serializer_class = dfirtrack_main_serializers.IpSerializer

class LocationListApi(generics.ListCreateAPIView):
    """ all objects, allowed: GET + POST """

    queryset = dfirtrack_main_models.Location.objects.all()
    serializer_class = dfirtrack_main_serializers.LocationSerializer

class LocationDetailApi(generics.RetrieveUpdateAPIView):
    """ single object, allowed: GET + PUT """

    queryset = dfirtrack_main_models.Location.objects.all()
    serializer_class = dfirtrack_main_serializers.LocationSerializer

class NoteListApi(generics.ListCreateAPIView):
    """ all objects, allowed: GET + POST """

    queryset = dfirtrack_main_models.Note.objects.all()
    serializer_class = dfirtrack_main_serializers.NoteSerializer

class NoteDetailApi(generics.RetrieveUpdateAPIView):
    """ single object, allowed: GET + PUT """

    queryset = dfirtrack_main_models.Note.objects.all()
    serializer_class = dfirtrack_main_serializers.NoteSerializer

class NotestatusListApi(generics.ListAPIView):
    """ all objects, allowed: GET """

    queryset = dfirtrack_main_models.Notestatus.objects.all()
    serializer_class = dfirtrack_main_serializers.NotestatusSerializer

class NotestatusDetailApi(generics.RetrieveAPIView):
    """ single object, allowed: GET """

    queryset = dfirtrack_main_models.Notestatus.objects.all()
    serializer_class = dfirtrack_main_serializers.NotestatusSerializer

class OsListApi(generics.ListCreateAPIView):
    """ all objects, allowed: GET + POST """

    queryset = dfirtrack_main_models.Os.objects.all()
    serializer_class = dfirtrack_main_serializers.OsSerializer

class OsDetailApi(generics.RetrieveUpdateAPIView):
    """ single object, allowed: GET + PUT """

    queryset = dfirtrack_main_models.Os.objects.all()
    serializer_class = dfirtrack_main_serializers.OsSerializer

class OsarchListApi(generics.ListCreateAPIView):
    """ all objects, allowed: GET + POST """

    queryset = dfirtrack_main_models.Osarch.objects.all()
    serializer_class = dfirtrack_main_serializers.OsarchSerializer

class OsarchDetailApi(generics.RetrieveUpdateAPIView):
    """ single object, allowed: GET + PUT """

    queryset = dfirtrack_main_models.Osarch.objects.all()
    serializer_class = dfirtrack_main_serializers.OsarchSerializer

class ReasonListApi(generics.ListCreateAPIView):
    """ all objects, allowed: GET + POST """

    queryset = dfirtrack_main_models.Reason.objects.all()
    serializer_class = dfirtrack_main_serializers.ReasonSerializer

class ReasonDetailApi(generics.RetrieveUpdateAPIView):
    """ single object, allowed: GET + PUT """

    queryset = dfirtrack_main_models.Reason.objects.all()
    serializer_class = dfirtrack_main_serializers.ReasonSerializer

class RecommendationListApi(generics.ListCreateAPIView):
    """ all objects, allowed: GET + POST """

    queryset = dfirtrack_main_models.Recommendation.objects.all()
    serializer_class = dfirtrack_main_serializers.RecommendationSerializer

class RecommendationDetailApi(generics.RetrieveUpdateAPIView):
    """ single object, allowed: GET + PUT """

    queryset = dfirtrack_main_models.Recommendation.objects.all()
    serializer_class = dfirtrack_main_serializers.RecommendationSerializer

class ServiceproviderListApi(generics.ListCreateAPIView):
    """ all objects, allowed: GET + POST """

    queryset = dfirtrack_main_models.Serviceprovider.objects.all()
    serializer_class = dfirtrack_main_serializers.ServiceproviderSerializer

class ServiceproviderDetailApi(generics.RetrieveUpdateAPIView):
    """ single object, allowed: GET + PUT """

    queryset = dfirtrack_main_models.Serviceprovider.objects.all()
    serializer_class = dfirtrack_main_serializers.ServiceproviderSerializer

class SystemListApi(generics.ListCreateAPIView):
    """ all objects, allowed: GET + POST """

    queryset = dfirtrack_main_models.System.objects.all()
    serializer_class = dfirtrack_main_serializers.SystemSerializer

class SystemDetailApi(generics.RetrieveUpdateAPIView):
    """ single object, allowed: GET + PUT """

    queryset = dfirtrack_main_models.System.objects.all()
    serializer_class = dfirtrack_main_serializers.SystemSerializer

class SystemstatusListApi(generics.ListAPIView):
    """ all objects, allowed: GET """

    queryset = dfirtrack_main_models.Systemstatus.objects.all()
    serializer_class = dfirtrack_main_serializers.SystemstatusSerializer

class SystemstatusDetailApi(generics.RetrieveAPIView):
    """ single object, allowed: GET """

    queryset = dfirtrack_main_models.Systemstatus.objects.all()
    serializer_class = dfirtrack_main_serializers.SystemstatusSerializer

class SystemtypeListApi(generics.ListCreateAPIView):
    """ all objects, allowed: GET + POST """

    queryset = dfirtrack_main_models.Systemtype.objects.all()
    serializer_class = dfirtrack_main_serializers.SystemtypeSerializer

class SystemtypeDetailApi(generics.RetrieveUpdateAPIView):
    """ single object, allowed: GET + PUT """

    queryset = dfirtrack_main_models.Systemtype.objects.all()
    serializer_class = dfirtrack_main_serializers.SystemtypeSerializer

class SystemuserListApi(generics.ListCreateAPIView):
    """ all objects, allowed: GET + POST """

    queryset = dfirtrack_main_models.Systemuser.objects.all()
    serializer_class = dfirtrack_main_serializers.SystemuserSerializer

class SystemuserDetailApi(generics.RetrieveUpdateAPIView):
    """ single object, allowed: GET + PUT """

    queryset = dfirtrack_main_models.Systemuser.objects.all()
    serializer_class = dfirtrack_main_serializers.SystemuserSerializer

class TagListApi(generics.ListCreateAPIView):
    """ all objects, allowed: GET + POST """

    queryset = dfirtrack_main_models.Tag.objects.all()
    serializer_class = dfirtrack_main_serializers.TagSerializer

class TagDetailApi(generics.RetrieveUpdateAPIView):
    """ single object, allowed: GET + PUT """

    queryset = dfirtrack_main_models.Tag.objects.all()
    serializer_class = dfirtrack_main_serializers.TagSerializer

class TagcolorListApi(generics.ListAPIView):
    """ all objects, allowed: GET """

    queryset = dfirtrack_main_models.Tagcolor.objects.all()
    serializer_class = dfirtrack_main_serializers.TagcolorSerializer

class TagcolorDetailApi(generics.RetrieveAPIView):
    """ single object, allowed: GET """

    queryset = dfirtrack_main_models.Tagcolor.objects.all()
    serializer_class = dfirtrack_main_serializers.TagcolorSerializer

class TaskListApi(generics.ListCreateAPIView):
    """ all objects, allowed: GET + POST """

    queryset = dfirtrack_main_models.Task.objects.all()
    serializer_class = dfirtrack_main_serializers.TaskSerializer

class TaskDetailApi(generics.RetrieveUpdateAPIView):
    """ single object, allowed: GET + PUT """

    queryset = dfirtrack_main_models.Task.objects.all()
    serializer_class = dfirtrack_main_serializers.TaskSerializer

class TasknameListApi(generics.ListCreateAPIView):
    """ all objects, allowed: GET + POST """

    queryset = dfirtrack_main_models.Taskname.objects.all()
    serializer_class = dfirtrack_main_serializers.TasknameSerializer

class TasknameDetailApi(generics.RetrieveUpdateAPIView):
    """ single object, allowed: GET + PUT """

    queryset = dfirtrack_main_models.Taskname.objects.all()
    serializer_class = dfirtrack_main_serializers.TasknameSerializer

class TaskpriorityListApi(generics.ListAPIView):
    """ all objects, allowed: GET """

    queryset = dfirtrack_main_models.Taskpriority.objects.all()
    serializer_class = dfirtrack_main_serializers.TaskprioritySerializer

class TaskpriorityDetailApi(generics.RetrieveAPIView):
    """ single object, allowed: GET """

    queryset = dfirtrack_main_models.Taskpriority.objects.all()
    serializer_class = dfirtrack_main_serializers.TaskprioritySerializer

class TaskstatusListApi(generics.ListAPIView):
    """ all objects, allowed: GET """

    queryset = dfirtrack_main_models.Taskstatus.objects.all()
    serializer_class = dfirtrack_main_serializers.TaskstatusSerializer

class TaskstatusDetailApi(generics.RetrieveAPIView):
    """ single object, allowed: GET """

    queryset = dfirtrack_main_models.Taskstatus.objects.all()
    serializer_class = dfirtrack_main_serializers.TaskstatusSerializer
