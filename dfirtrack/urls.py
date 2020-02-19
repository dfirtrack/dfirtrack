from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    url(r'^$', views.login_redirect, name='login_redirect'),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('dfirtrack_main.urls')),
    url(r'^artifacts/', include('dfirtrack_artifacts.urls')),
    url(r'^login/', LoginView.as_view(template_name='dfirtrack_main/login.html')),
    url(r'^logout/', LogoutView.as_view(template_name='dfirtrack_main/logout.html')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if 'dfirtrack_api' in settings.INSTALLED_APPS:
    urlpatterns += [
        url(r'^api/', include('dfirtrack_api.urls')),
    ]
