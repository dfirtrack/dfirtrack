from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from dfirtrack_api.views import dfirtrack_artifacts, dfirtrack_main

urlpatterns = [

    # dfirtrack_artifacts
    url(r'^artifacts/$', dfirtrack_artifacts.ArtifactListApi.as_view()),
    url(r'^artifacts/(?P<pk>\d+)/$', dfirtrack_artifacts.ArtifactDetailApi.as_view()),
    url(r'^artifactstatuss/$', dfirtrack_artifacts.ArtifactstatusListApi.as_view()),
    url(r'^artifactstatuss/(?P<pk>\d+)/$', dfirtrack_artifacts.ArtifactstatusDetailApi.as_view()),
    url(r'^artifacttypes/$', dfirtrack_artifacts.ArtifacttypeListApi.as_view()),
    url(r'^artifacttypes/(?P<pk>\d+)/$', dfirtrack_artifacts.ArtifacttypeDetailApi.as_view()),

    # dfirtrack_main
    url(r'^analysisstatuss/$', dfirtrack_main.AnalysisstatusListApi.as_view()),
    url(r'^analysisstatuss/(?P<pk>\d+)/$', dfirtrack_main.AnalysisstatusDetailApi.as_view()),
    url(r'^ips/$', dfirtrack_main.IpListApi.as_view()),
    url(r'^oss/$', dfirtrack_main.OsListApi.as_view()),
    url(r'^systems/$', dfirtrack_main.SystemListApi.as_view()),
    url(r'^systems/(?P<pk>\d+)/$', dfirtrack_main.SystemDetailApi.as_view()),
    url(r'^tags/$', dfirtrack_main.TagListApi.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
