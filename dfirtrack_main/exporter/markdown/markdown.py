from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
from dfirtrack_config.models import SystemExporterMarkdownConfigModel
from dfirtrack_main.exporter.markdown.domainsorted import domainsorted
from dfirtrack_main.exporter.markdown.systemsorted import systemsorted


@login_required(login_url="/login")
def system_create_cron(request):
    """ helper function to check config before creating scheduled task """

    # TODO: add logic like in 'dfirtrack_main.exporter.file.xls.system_create_cron'
    pass

@login_required(login_url="/login")
def system(request):
    """ instant markdown export via button to server file system """

    # get config model
    model = SystemExporterMarkdownConfigModel.objects.get(system_exporter_markdown_config_name = 'SystemExporterMarkdownConfig')

    # decide between sorted by system or sorted by domain
    if model.markdown_sorting == 'sys':
        systemsorted(request)
    if model.markdown_sorting == 'dom':
        domainsorted(request)

    # return to 'system_list'
    return redirect(reverse('system_list'))

def system_cron():
    """ markdown export via scheduled task to server file system """

    # get config model
    model = SystemExporterMarkdownConfigModel.objects.get(system_exporter_markdown_config_name = 'SystemExporterMarkdownConfig')

    # decide between sorted by system or sorted by domain
    if model.markdown_sorting == 'sys':
        systemsorted()
    if model.markdown_sorting == 'dom':
        domainsorted()

    # return to 'system_list'
    return redirect(reverse('system_list'))
