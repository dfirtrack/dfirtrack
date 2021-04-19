from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.db.utils import ProgrammingError
from django.urls import include, path, re_path
from dfirtrack import views
from dfirtrack_config.models import MainConfigModel
from dfirtrack_artifacts.views import artifact_view
from dfirtrack_main.views import system_views, case_views, tag_views, task_views

urlpatterns = [
    re_path(r'^$', views.login_redirect, name='login_redirect'),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^', include('dfirtrack_main.urls')),
    re_path(r'^artifacts/', include('dfirtrack_artifacts.urls')),
    re_path(r'^config/', include('dfirtrack_config.urls')),
    re_path(r'^login/', LoginView.as_view(template_name='dfirtrack_main/login.html')),
    re_path(r'^logout/', LogoutView.as_view(template_name='dfirtrack_main/logout.html')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if 'dfirtrack_api' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^api/', include('dfirtrack_api.urls')),
    ]

# TODO: change this design to something more sustainable

# Django setup builds URLs before populating database
# so this is needed for initial migration
try:
    # get config
    model = MainConfigModel.objects.get(main_config_name='MainConfig')

    # TODO: change to something like 'reverse()' to prevent redundant code

    # system
    if model.main_overview == 'main_overview_system':
        urlpatterns += [
            path('system/', system_views.SystemList.as_view(), name='main_overview'),
        ]
    # artifact
    elif model.main_overview == 'main_overview_artifact' and 'dfirtrack_artifacts' in settings.INSTALLED_APPS:
        urlpatterns += [
            re_path(r'artifacts/artfiact/', artifact_view.ArtifactListView.as_view(), name='main_overview'),
        ]
    # case
    elif model.main_overview == 'main_overview_case':
        urlpatterns += [
            re_path(r'case/', case_views.CaseList.as_view(), name='main_overview'),
        ]
    # tag
    elif model.main_overview == 'main_overview_tag':
        urlpatterns += [
            re_path(r'tag/', tag_views.TagList.as_view(), name='main_overview'),
        ]
    # task
    elif model.main_overview == 'main_overview_task':
        urlpatterns += [
            re_path(r'task/', task_views.TaskStart.as_view(), name='main_overview'),
        ]
    # catch-up pattern
    else:
        urlpatterns += [
            re_path(r'system/', system_views.SystemList.as_view(), name='main_overview'),
        ]

# database not available before first migrations
except ProgrammingError:

    # catch-up pattern
    urlpatterns += [
        re_path(r'system/', system_views.SystemList.as_view(), name='main_overview'),
    ]
