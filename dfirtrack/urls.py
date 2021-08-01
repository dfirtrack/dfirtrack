from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path, re_path

from dfirtrack import views

urlpatterns = [
    re_path(r'^$', views.login_redirect, name='login_redirect'),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^', include('dfirtrack_main.urls')),
    re_path(r'^artifacts/', include('dfirtrack_artifacts.urls')),
    re_path(r'^config/', include('dfirtrack_config.urls')),
    re_path(r'^login/', LoginView.as_view(template_name='dfirtrack_main/login.html')),
    re_path(r'^logout/', LogoutView.as_view(template_name='dfirtrack_main/logout.html')),
    re_path(r'^martor/', include('martor.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if 'dfirtrack_api' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^api/', include('dfirtrack_api.urls')),
    ]

urlpatterns += [
    path('main_overview/', views.main_overview_redirect, name='main_overview'),
]
