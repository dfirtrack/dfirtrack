from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
from dfirtrack import settings
from dfirtrack_config.models import MainConfigModel

def login_redirect(request):
    """ redirect to login """

    return redirect('/login')

@login_required
def main_overview_redirect(request):
    """ redirect main overview according to config """

    # get config
    model = MainConfigModel.objects.get(main_config_name='MainConfig')

    # system
    if model.main_overview == 'main_overview_system':
        return redirect(reverse('system_list'))
    # artifact
    elif model.main_overview == 'main_overview_artifact' and 'dfirtrack_artifacts' in settings.INSTALLED_APPS:
        return redirect(reverse('artifact_list'))
    # case
    elif model.main_overview == 'main_overview_case':
        return redirect(reverse('case_list'))
    # tag
    elif model.main_overview == 'main_overview_tag':
        return redirect(reverse('tag_list'))
    # task
    elif model.main_overview == 'main_overview_task':
        return redirect(reverse('task_list'))
    # catch-up pattern
    else:
        return redirect(reverse('system_list'))
