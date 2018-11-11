"""dfirtrack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, handler404, handler500, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from . import views

urlpatterns = [
    url(r'^$', views.login_redirect, name='login_redirect'),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('dfirtrack_main.urls')),
    url(r'^api/', include('dfirtrack_api.urls')),
    url(r'^login/', login, {'template_name': 'dfirtrack_main/login.html'}),
    url(r'^logout/', logout, {'template_name': 'dfirtrack_main/logout.html'})
]

handler400 = views.page_400
handler403 = views.page_403
handler404 = views.page_404
handler500 = views.page_500
