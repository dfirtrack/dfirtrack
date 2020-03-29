from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from dfirtrack_api.views import dfirtrack_artifacts, dfirtrack_main

urlpatterns = [

    # dfirtrack_artifacts
    url(r'^artifact/$', dfirtrack_artifacts.ArtifactListApi.as_view()),
    url(r'^artifact/(?P<pk>\d+)/$', dfirtrack_artifacts.ArtifactDetailApi.as_view()),
    url(r'^artifactstatus/$', dfirtrack_artifacts.ArtifactstatusListApi.as_view()),
    url(r'^artifactstatus/(?P<pk>\d+)/$', dfirtrack_artifacts.ArtifactstatusDetailApi.as_view()),
    url(r'^artifacttype/$', dfirtrack_artifacts.ArtifacttypeListApi.as_view()),
    url(r'^artifacttype/(?P<pk>\d+)/$', dfirtrack_artifacts.ArtifacttypeDetailApi.as_view()),

    # dfirtrack_main
    url(r'^analysisstatus/$', dfirtrack_main.AnalysisstatusListApi.as_view()),
    url(r'^analysisstatus/(?P<pk>\d+)/$', dfirtrack_main.AnalysisstatusDetailApi.as_view()),
    url(r'^case/$', dfirtrack_main.CaseListApi.as_view()),
    url(r'^case/(?P<pk>\d+)/$', dfirtrack_main.CaseDetailApi.as_view()),
    url(r'^company/$', dfirtrack_main.CompanyListApi.as_view()),
    url(r'^company/(?P<pk>\d+)/$', dfirtrack_main.CompanyDetailApi.as_view()),
    url(r'^contact/$', dfirtrack_main.ContactListApi.as_view()),
    url(r'^contact/(?P<pk>\d+)/$', dfirtrack_main.ContactDetailApi.as_view()),
    url(r'^division/$', dfirtrack_main.DivisionListApi.as_view()),
    url(r'^division/(?P<pk>\d+)/$', dfirtrack_main.DivisionDetailApi.as_view()),
    url(r'^dnsname/$', dfirtrack_main.DnsnameListApi.as_view()),
    url(r'^dnsname/(?P<pk>\d+)/$', dfirtrack_main.DnsnameDetailApi.as_view()),
    url(r'^domain/$', dfirtrack_main.DomainListApi.as_view()),
    url(r'^domain/(?P<pk>\d+)/$', dfirtrack_main.DomainDetailApi.as_view()),
    url(r'^domainuser/$', dfirtrack_main.DomainuserListApi.as_view()),
    url(r'^domainuser/(?P<pk>\d+)/$', dfirtrack_main.DomainuserDetailApi.as_view()),
    url(r'^ip/$', dfirtrack_main.IpListApi.as_view()),
    url(r'^ip/(?P<pk>\d+)/$', dfirtrack_main.IpDetailApi.as_view()),
    url(r'^location/$', dfirtrack_main.LocationListApi.as_view()),
    url(r'^location/(?P<pk>\d+)/$', dfirtrack_main.LocationDetailApi.as_view()),
    url(r'^os/$', dfirtrack_main.OsListApi.as_view()),
    url(r'^os/(?P<pk>\d+)/$', dfirtrack_main.OsDetailApi.as_view()),
    url(r'^osarch/$', dfirtrack_main.OsarchListApi.as_view()),
    url(r'^osarch/(?P<pk>\d+)/$', dfirtrack_main.OsarchDetailApi.as_view()),
    url(r'^reason/$', dfirtrack_main.ReasonListApi.as_view()),
    url(r'^reason/(?P<pk>\d+)/$', dfirtrack_main.ReasonDetailApi.as_view()),
    url(r'^recommendation/$', dfirtrack_main.RecommendationListApi.as_view()),
    url(r'^recommendation/(?P<pk>\d+)/$', dfirtrack_main.RecommendationDetailApi.as_view()),
    url(r'^serviceprovider/$', dfirtrack_main.ServiceproviderListApi.as_view()),
    url(r'^serviceprovider/(?P<pk>\d+)/$', dfirtrack_main.ServiceproviderDetailApi.as_view()),
    url(r'^system/$', dfirtrack_main.SystemListApi.as_view()),
    url(r'^system/(?P<pk>\d+)/$', dfirtrack_main.SystemDetailApi.as_view()),
    url(r'^systemstatus/$', dfirtrack_main.SystemstatusListApi.as_view()),
    url(r'^systemstatus/(?P<pk>\d+)/$', dfirtrack_main.SystemstatusDetailApi.as_view()),
    url(r'^systemtype/$', dfirtrack_main.SystemtypeListApi.as_view()),
    url(r'^systemtype/(?P<pk>\d+)/$', dfirtrack_main.SystemtypeDetailApi.as_view()),
    url(r'^systemuser/$', dfirtrack_main.SystemuserListApi.as_view()),
    url(r'^systemuser/(?P<pk>\d+)/$', dfirtrack_main.SystemuserDetailApi.as_view()),
    url(r'^tag/$', dfirtrack_main.TagListApi.as_view()),
    url(r'^tag/(?P<pk>\d+)/$', dfirtrack_main.TagDetailApi.as_view()),
    url(r'^tagcolor/$', dfirtrack_main.TagcolorListApi.as_view()),
    url(r'^tagcolor/(?P<pk>\d+)/$', dfirtrack_main.TagcolorDetailApi.as_view()),
    url(r'^task/$', dfirtrack_main.TaskListApi.as_view()),
    url(r'^task/(?P<pk>\d+)/$', dfirtrack_main.TaskDetailApi.as_view()),
    url(r'^taskname/$', dfirtrack_main.TasknameListApi.as_view()),
    url(r'^taskname/(?P<pk>\d+)/$', dfirtrack_main.TasknameDetailApi.as_view()),
    url(r'^taskpriority/$', dfirtrack_main.TaskpriorityListApi.as_view()),
    url(r'^taskpriority/(?P<pk>\d+)/$', dfirtrack_main.TaskpriorityDetailApi.as_view()),
    url(r'^taskstatus/$', dfirtrack_main.TaskstatusListApi.as_view()),
    url(r'^taskstatus/(?P<pk>\d+)/$', dfirtrack_main.TaskstatusDetailApi.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
