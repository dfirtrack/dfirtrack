from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from dfirtrack_config.forms import SystemExporterMarkdownConfigForm
from dfirtrack_config.models import SystemExporterMarkdownConfigModel

@login_required(login_url="/login")
def system_exporter_markdown_config_view(request):

    # form was valid to post
    if request.method == "POST":

        form = SystemExporterMarkdownConfigForm(request.POST)
        model = SystemExporterMarkdownConfigModel.objects.get(system_exporter_markdown_config_name = 'SystemExporterMarkdownConfig')

        if form.is_valid():

            # assign values
            model.markdown_path = form.cleaned_data['markdown_path']
            model.markdown_sorting = form.cleaned_data['markdown_sorting']
            model.save()

        # close popup
        return HttpResponse('<script type="text/javascript">window.close();</script>')

    else:

        # get config model
        model = SystemExporterMarkdownConfigModel.objects.get(system_exporter_markdown_config_name = 'SystemExporterMarkdownConfig')
        # submit existing values to form
        form = SystemExporterMarkdownConfigForm(
            initial = {
                'markdown_path': model.markdown_path,
                'markdown_sorting': model.markdown_sorting,
            }
        )

    # show form page
    return render(
        request,
        'dfirtrack_config/system/system_exporter_markdown_config_popup.html',
        {
            'form': form,
        }
    )
