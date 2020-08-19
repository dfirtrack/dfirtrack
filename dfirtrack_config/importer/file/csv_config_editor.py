from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from dfirtrack_config.forms import SystemImporterFileCsvConfigbasedConfigForm, SystemImporterFileCsvFormbasedConfigForm
from dfirtrack_config.models import SystemImporterFileCsvConfigbasedConfigModel, SystemImporterFileCsvFormbasedConfigModel

@login_required(login_url="/login")
def system_importer_file_csv_config_based_config_view(request):

    # form was valid to post
    if request.method == "POST":

        form = SystemImporterFileCsvConfigbasedConfigForm(request.POST)
        model = SystemImporterFileCsvConfigbasedConfigModel.objects.get(system_importer_file_csv_configbased_config_name = 'SystemImporterFileCsvConfigbasedConfig')

        if form.is_valid():

            """ assign values """

            # general settings
            model.csv_skip_existing_system = form.cleaned_data['csv_skip_existing_system']
            model.csv_column_system = form.cleaned_data['csv_column_system']
            model.csv_headline = form.cleaned_data['csv_headline']
            # IP related settings
            model.csv_choice_ip = form.cleaned_data['csv_choice_ip']
            model.csv_remove_ip = form.cleaned_data['csv_remove_ip']
            model.csv_column_ip = form.cleaned_data['csv_column_ip']
            # overriding settings
            model.csv_remove_case = form.cleaned_data['csv_remove_case']
            model.csv_remove_company = form.cleaned_data['csv_remove_company']
            model.csv_remove_tag = form.cleaned_data['csv_remove_tag']
            # TODO: find an alternative for the selection
            ## config based settings
            #model.csv_default_systemstatus = form.cleaned_data['csv_default_systemstatus']
            #model.csv_default_analysisstatus = form.cleaned_data['csv_default_analysisstatus']
            #model.csv_default_reason = form.cleaned_data['csv_default_reason']
            #model.csv_default_domain = form.cleaned_data['csv_default_domain']
            #model.csv_default_dnsname = form.cleaned_data['csv_default_dnsname']
            #model.csv_default_systemtype = form.cleaned_data['csv_default_systemtype']
            #model.csv_default_os = form.cleaned_data['csv_default_os']
            #model.csv_default_location = form.cleaned_data['csv_default_location']
            #model.csv_default_serviceprovider = form.cleaned_data['csv_default_serviceprovider']
            #model.csv_default_case = form.cleaned_data['csv_default_case']
            #model.csv_default_company = form.cleaned_data['csv_default_company']
            #model.csv_default_tag = form.cleaned_data['csv_default_tag']
            model.save()

            # close popup
            return HttpResponse('<script type="text/javascript">window.close();</script>')

        else:
            # show form page again
            return render(
                request,
                'dfirtrack_main/system/system_importer_file_csv_config_based_config_popup.html',
                {
                    'form': form,
                }
            )

    else:

        # get config model
        model = SystemImporterFileCsvConfigbasedConfigModel.objects.get(system_importer_file_csv_configbased_config_name = 'SystemImporterFileCsvConfigbasedConfig')
        # submit existing values to form
        form = SystemImporterFileCsvConfigbasedConfigForm(
            initial = {
                # general settings
                'csv_skip_existing_system': model.csv_skip_existing_system,
                'csv_column_system': model.csv_column_system,
                'csv_headline': model.csv_headline,
                # IP related settings
                'csv_choice_ip': model.csv_choice_ip,
                'csv_remove_ip': model.csv_remove_ip,
                'csv_column_ip': model.csv_column_ip,
                # overriding settings
                'csv_remove_case': model.csv_remove_case,
                'csv_remove_company': model.csv_remove_company,
                'csv_remove_tag': model.csv_remove_tag,
                # TODO: find an alternative for the selection
                ## config based settings
                #'csv_default_systemstatus': model.csv_default_systemstatus,
                #'csv_default_analysisstatus': model.csv_default_analysisstatus,
                #'csv_default_reason': model.csv_default_reason,
                #'csv_default_domain': model.csv_default_domain,
                #'csv_default_dnsname': model.csv_default_dnsname,
                #'csv_default_systemtype': model.csv_default_systemtype,
                #'csv_default_os': model.csv_default_os,
                #'csv_default_location': model.csv_default_location,
                #'csv_default_serviceprovider': model.csv_default_serviceprovider,
                #'csv_default_case': model.csv_default_case,
                #'csv_default_company': model.csv_default_company,
                #'csv_default_tag': model.csv_default_tag,
            }
        )

    # show form page
    return render(
        request,
        'dfirtrack_main/system/system_importer_file_csv_config_based_config_popup.html',
        {
            'form': form,
        }
    )

@login_required(login_url="/login")
def system_importer_file_csv_form_based_config_view(request):

    # form was valid to post
    if request.method == "POST":

        form = SystemImporterFileCsvFormbasedConfigForm(request.POST)
        model = SystemImporterFileCsvFormbasedConfigModel.objects.get(system_importer_file_csv_formbased_config_name = 'SystemImporterFileCsvFormbasedConfig')

        if form.is_valid():

            """ assign values """

            # general settings
            model.csv_skip_existing_system = form.cleaned_data['csv_skip_existing_system']
            model.csv_column_system = form.cleaned_data['csv_column_system']
            model.csv_headline = form.cleaned_data['csv_headline']
            # IP related settings
            model.csv_choice_ip = form.cleaned_data['csv_choice_ip']
            model.csv_remove_ip = form.cleaned_data['csv_remove_ip']
            model.csv_column_ip = form.cleaned_data['csv_column_ip']
            # overriding settings
            model.csv_remove_case = form.cleaned_data['csv_remove_case']
            model.csv_remove_company = form.cleaned_data['csv_remove_company']
            model.csv_remove_tag = form.cleaned_data['csv_remove_tag']
            model.save()

            # close popup
            return HttpResponse('<script type="text/javascript">window.close();</script>')

        else:
            # show form page again
            return render(
                request,
                'dfirtrack_main/system/system_importer_file_csv_form_based_config_popup.html',
                {
                    'form': form,
                }
            )

    else:

        # get config model
        model = SystemImporterFileCsvFormbasedConfigModel.objects.get(system_importer_file_csv_formbased_config_name = 'SystemImporterFileCsvFormbasedConfig')
        # submit existing values to form
        form = SystemImporterFileCsvFormbasedConfigForm(
            initial = {
                # general settings
                'csv_skip_existing_system': model.csv_skip_existing_system,
                'csv_column_system': model.csv_column_system,
                'csv_headline': model.csv_headline,
                # IP related settings
                'csv_choice_ip': model.csv_choice_ip,
                'csv_remove_ip': model.csv_remove_ip,
                'csv_column_ip': model.csv_column_ip,
                # overriding settings
                'csv_remove_case': model.csv_remove_case,
                'csv_remove_company': model.csv_remove_company,
                'csv_remove_tag': model.csv_remove_tag,
            }
        )

    # show form page
    return render(
        request,
        'dfirtrack_main/system/system_importer_file_csv_form_based_config_popup.html',
        {
            'form': form,
        }
    )
