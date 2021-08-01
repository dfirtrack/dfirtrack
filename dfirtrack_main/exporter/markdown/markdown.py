from urllib.parse import urlencode, urlunparse

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse

from dfirtrack_config.models import SystemExporterMarkdownConfigModel
from dfirtrack_main.exporter.markdown.checks import check_content_file_system
from dfirtrack_main.exporter.markdown.domainsorted import domainsorted
from dfirtrack_main.exporter.markdown.systemsorted import systemsorted


@login_required(login_url="/login")
def system_create_cron(request):
    """helper function to check config before creating scheduled task"""

    # check file system
    stop_exporter_markdown = check_content_file_system(request)

    # check stop condition
    if stop_exporter_markdown:
        # return to 'system_list'
        return redirect(reverse("system_list"))
    else:

        # create parameter dict
        params = {}

        # prepare parameter dict
        params["name"] = "system_markdown_exporter"
        params["func"] = "dfirtrack_main.exporter.markdown.markdown.system_cron"

        # build url
        urlpath = "/admin/django_q/schedule/add/"
        urlquery = urlencode(params)
        admin_url_create_cron = urlunparse(("", "", urlpath, "", urlquery, ""))

        # open django admin with pre-filled form for scheduled task
        return redirect(admin_url_create_cron)


@login_required(login_url="/login")
def system(request):
    """instant markdown export via button to server file system"""

    # check file system
    stop_exporter_markdown = check_content_file_system(request)

    # leave if config caused errors
    if stop_exporter_markdown:
        # return to 'system_list'
        return redirect(reverse("system_list"))

    # get config model
    model = SystemExporterMarkdownConfigModel.objects.get(
        system_exporter_markdown_config_name="SystemExporterMarkdownConfig"
    )

    # decide between sorted by system or sorted by domain
    if model.markdown_sorting == "sys":
        systemsorted(request)
    if model.markdown_sorting == "dom":
        domainsorted(request)

    # return to 'system_list'
    return redirect(reverse("system_list"))


def system_cron():
    """markdown export via scheduled task to server file system"""

    # check file system
    stop_exporter_markdown = check_content_file_system()

    # leave if config caused errors
    if stop_exporter_markdown:
        # return to scheduled task
        return

    # get config model
    model = SystemExporterMarkdownConfigModel.objects.get(
        system_exporter_markdown_config_name="SystemExporterMarkdownConfig"
    )

    # decide between sorted by system or sorted by domain
    if model.markdown_sorting == "sys":
        systemsorted()
    if model.markdown_sorting == "dom":
        domainsorted()
