from dfirtrack_api.serializers.dfirtrack_main import AnalysisstatusSerializer, CaseSerializer, CompanySerializer, ContactSerializer, DivisionSerializer, DnsnameSerializer, DomainSerializer, IpSerializer, OsSerializer, SystemSerializer, SystemstatusSerializer, TagSerializer
from dfirtrack_main.models import Analysisstatus, Case, Company, Contact, Division, Dnsname, Domain, Ip, Os, System, Systemstatus, Tag
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

class SystemstatusListApi(generics.ListCreateAPIView):
    """ all objects, allowed: GET + POST """

    queryset = Systemstatus.objects.all()
    serializer_class = SystemstatusSerializer

class SystemstatusDetailApi(generics.RetrieveUpdateAPIView):
    """ single object, allowed: GET + PUT"""

    queryset = Systemstatus.objects.all()
    serializer_class = SystemstatusSerializer

class TagListApi(generics.ListAPIView):
    """ all objects, allowed: GET """

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
