from constance import config as constance_config
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from dfirtrack_main.config_forms import SystemExporterMarkdownConfigForm

@login_required(login_url="/login")
def system_exporter_markdown_config_view(request):

    # form was valid to post
    if request.method == "POST":

        form = SystemExporterMarkdownConfigForm(request.POST)

        if form.is_valid():

            # assign values
            constance_config.MARKDOWN_PATH = form.cleaned_data['markdown_path']
            constance_config.MARKDOWN_SORTING = form.cleaned_data['markdown_sorting']

        # close popup
        return HttpResponse('<script type="text/javascript">window.close();</script>')

    else:

        # submit existing values to form
        form = SystemExporterMarkdownConfigForm(
            initial = {
                'markdown_path': constance_config.MARKDOWN_PATH,
                'markdown_sorting': constance_config.MARKDOWN_SORTING,
            }
        )

    # show form page
    return render(
        request,
        'dfirtrack_main/system/system_exporter_markdown_config_popup.html',
        {
            'form': form,
        }
    )
