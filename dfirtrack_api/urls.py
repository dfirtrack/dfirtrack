from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from dfirtrack_api.views import dfirtrack_artifacts, dfirtrack_main

urlpatterns = [

    # dfirtrack_artifacts
    url(r'^artifacts/$', dfirtrack_artifacts.ArtifactListApi.as_view()),

    # dfirtrack_main
    url(r'^ips/$', dfirtrack_main.IpListApi.as_view()),
    url(r'^oss/$', dfirtrack_main.OsListApi.as_view()),
    url(r'^systems/$', dfirtrack_main.SystemListApi.as_view()),
    url(r'^systems/(?P<pk>\d+)/$', dfirtrack_main.SystemDetailApi.as_view()),
    url(r'^tags/$', dfirtrack_main.TagListApi.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
