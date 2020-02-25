from dfirtrack_api.serializers.dfirtrack_main import AnalysisstatusSerializer, CaseSerializer, CompanySerializer, ContactSerializer, DivisionSerializer, DnsnameSerializer, DomainSerializer, IpSerializer, LocationSerializer, OsSerializer, ReasonSerializer, RecommendationSerializer, ServiceproviderSerializer, SystemSerializer, SystemstatusSerializer, SystemtypeSerializer, TagSerializer
from dfirtrack_main.models import Analysisstatus, Case, Company, Contact, Division, Dnsname, Domain, Ip, Location, Os, Reason, Recommendation, Serviceprovider, System, Systemstatus, Systemtype, Tag
from rest_framework import generics

class AnalysisstatusListApi(generics.ListCreateAPIView):
    """ all objects, allowed: GET + POST """

    queryset = Analysisstatus.objects.all()
    serializer_class = AnalysisstatusSerializer

class AnalysisstatusDetailApi(generics.RetrieveUpdateAPIView):
    """ single object, allowed: GET + PUT"""

    queryset = Analysisstatus.objects.all()
    serializer_class = AnalysisstatusSerializer

class CaseListApi(generics.ListCreateAPIView):
    """ all objects, allowed: GET + POST """

    queryset = Case.objects.all()
    serializer_class = CaseSerializer

class CaseDetailApi(generics.RetrieveUpdateAPIView):
    """ single object, allowed: GET + PUT"""

    queryset = Case.objects.all()
    serializer_class = CaseSerializer

class CompanyListApi(generics.ListCreateAPIView):
    """ all objects, allowed: GET + POST """

    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyDetailApi(generics.RetrieveUpdateAPIView):
    """ single object, allowed: GET + PUT"""

    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class ContactListApi(generics.ListCreateAPIView):
    """ all objects, allowed: GET + POST """

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactDetailApi(generics.RetrieveUpdateAPIView):
    """ single object, allowed: GET + PUT"""

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class DivisionListApi(generics.ListCreateAPIView):
    """ all objects, allowed: GET + POST """

    queryset = Division.objects.all()
    serializer_class = DivisionSerializer

class DivisionDetailApi(generics.RetrieveUpdateAPIView):
    """ single object, allowed: GET + PUT"""

    queryset = Division.objects.all()
    serializer_class = DivisionSerializer

class DnsnameListApi(generics.ListCreateAPIView):
    """ all objects, allowed: GET + POST """

    queryset = Dnsname.objects.all()
    serializer_class = DnsnameSerializer

class DnsnameDetailApi(generics.RetrieveUpdateAPIView):
    """ single object, allowed: GET + PUT"""

    queryset = Dnsname.objects.all()
    serializer_class = DnsnameSerializer

class DomainListApi(generics.ListCreateAPIView):
    """ all objects, allowed: GET + POST """

    queryset = Domain.objects.all()
    serializer_class = DomainSerializer

class DomainDetailApi(generics.RetrieveUpdateAPIView):
    """ single object, allowed: GET + PUT"""

    queryset = Domain.objects.all()
    serializer_class = DomainSerializer

class IpListApi(generics.ListCreateAPIView):
    """ all objects, allowed: GET + POST """

    queryset = Ip.objects.all()
    serializer_class = IpSerializer

class IpDetailApi(generics.RetrieveUpdateAPIView):
    """ single object, allowed: GET + PUT"""

    queryset = Ip.objects.all()
    serializer_class = IpSerializer

class LocationListApi(generics.ListCreateAPIView):
    """ all objects, allowed: GET + POST """

    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class LocationDetailApi(generics.RetrieveUpdateAPIView):
    """ single object, allowed: GET + PUT"""

    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class OsListApi(generics.ListCreateAPIView):
    """ all objects, allowed: GET + POST """

    queryset = Os.objects.all()
    serializer_class = OsSerializer

class ReasonListApi(generics.ListCreateAPIView):
    """ all objects, allowed: GET + POST """

    queryset = Reason.objects.all()
    serializer_class = ReasonSerializer

class ReasonDetailApi(generics.RetrieveUpdateAPIView):
    """ single object, allowed: GET + PUT"""

    queryset = Reason.objects.all()
    serializer_class = ReasonSerializer

class RecommendationListApi(generics.ListCreateAPIView):
    """ all objects, allowed: GET + POST """

    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer

class RecommendationDetailApi(generics.RetrieveUpdateAPIView):
    """ single object, allowed: GET + PUT"""

    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer

class ServiceproviderListApi(generics.ListCreateAPIView):
    """ all objects, allowed: GET + POST """

    queryset = Serviceprovider.objects.all()
    serializer_class = ServiceproviderSerializer

class ServiceproviderDetailApi(generics.RetrieveUpdateAPIView):
    """ single object, allowed: GET + PUT"""

    queryset = Serviceprovider.objects.all()
    serializer_class = ServiceproviderSerializer

class SystemListApi(generics.ListAPIView):
    """ all objects, allowed: GET """

    queryset = System.objects.all()
    serializer_class = SystemSerializer

class SystemDetailApi(generics.RetrieveAPIView):
    """ single object, allowed: GET """

    queryset = System.objects.all()
    serializer_class = SystemSerializer

class SystemstatusListApi(generics.ListCreateAPIView):
    """ all objects, allowed: GET + POST """

    queryset = Systemstatus.objects.all()
    serializer_class = SystemstatusSerializer

class SystemstatusDetailApi(generics.RetrieveUpdateAPIView):
    """ single object, allowed: GET + PUT"""

    queryset = Systemstatus.objects.all()
    serializer_class = SystemstatusSerializer

class SystemtypeListApi(generics.ListCreateAPIView):
    """ all objects, allowed: GET + POST """

    queryset = Systemtype.objects.all()
    serializer_class = SystemtypeSerializer

class SystemtypeDetailApi(generics.RetrieveUpdateAPIView):
    """ single object, allowed: GET + PUT"""

    queryset = Systemtype.objects.all()
    serializer_class = SystemtypeSerializer

class TagListApi(generics.ListAPIView):
    """ all objects, allowed: GET """

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
