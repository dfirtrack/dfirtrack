from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [

    url(r'^ips/$', views.IpListApi.as_view()),
    url(r'^oss/$', views.OsListApi.as_view()),
    url(r'^systems/$', views.SystemListApi.as_view()),
    url(r'^systems/(?P<pk>\d+)/$', views.SystemDetailApi.as_view()),
    url(r'^tags/$', views.TagListApi.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
