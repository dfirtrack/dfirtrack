from constance import config as constance_config
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
from .domainsorted import domainsorted
from .systemsorted import systemsorted

@login_required(login_url="/login")
def system(request):
    """ function to decide between sorted by system or sorted by domain """

    if constance_config.MARKDOWN_SORTING == 'systemsorted':
        systemsorted(request)
    if constance_config.MARKDOWN_SORTING == 'domainsorted':
        domainsorted(request)

    return redirect(reverse('system_list'))
