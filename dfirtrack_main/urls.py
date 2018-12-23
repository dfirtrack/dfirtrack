from django.conf.urls import url
from dfirtrack_main.views import generic_views
from dfirtrack_main.views import analysisstatuss_views, analystmemos_views, cases_views, companys_views, contacts_views, divisions_views, domains_views, entrys_views, headlines_views, ips_views, locations_views, oss_views, osimportnames_views, reasons_views, recommendations_views, reportitems_views, serviceproviders_views, systems_views, systemstatuss_views, systemtypes_views, systemusers_views, tags_views, tasks_views, tasknames_views, taskprioritys_views, taskstatuss_views
from dfirtrack_main.creator import systems_creator, tasks_creator
from dfirtrack_main.exporter.spreadsheet import csv as spreadsheet_csv
from dfirtrack_main.exporter.spreadsheet import xls
from dfirtrack_main.exporter.markdown import domainsorted, systemsorted
from dfirtrack_main.importer.api import giraf
from dfirtrack_main.importer.file import csv as file_csv
from dfirtrack_main.importer.file import filesystem, markdown
from dfirtrack_main.models import Analysisstatus, Analystmemo, Case, Company, Contact, Division, Domain, Entry, Headline, Ip, Location, Os, Osimportname, Reason, Recommendation, Reportitem, Serviceprovider, System, Systemstatus, Systemtype, Systemuser, Tag, Task, Taskname, Taskpriority, Taskstatus

urlpatterns = [

    url(r'^about/$', generic_views.about, name='about'),
    url(r'^faq/$', generic_views.faq, name='faq'),

    url(r'^analysisstatuss/$', analysisstatuss_views.Analysisstatuss.as_view(), name='analysisstatuss'),
    url(r'^analysisstatuss/(?P<pk>\d+)$', analysisstatuss_views.AnalysisstatussDetail.as_view(), name='analysisstatussdetail'),

    url(r'^analystmemos/$', analystmemos_views.Analystmemos.as_view(), name='analystmemos'),
    url(r'^analystmemos/(?P<pk>\d+)$', analystmemos_views.AnalystmemosDetail.as_view(), name='analystmemosdetail'),
    url(r'^analystmemos/add$', analystmemos_views.analystmemos_add, name='analystmemos_add'),
    url(r'^analystmemos/(?P<pk>\d+)/edit/$', analystmemos_views.analystmemos_edit, name='analystmemos_edit'),

    url(r'^cases/$', cases_views.Cases.as_view(), name='cases'),
    url(r'^cases/(?P<pk>\d+)$', cases_views.CasesDetail.as_view(), name='casesdetail'),
    url(r'^cases/add$', cases_views.cases_add, name='cases_add'),
    url(r'^cases/(?P<pk>\d+)/edit/$', cases_views.cases_edit, name='cases_edit'),

    url(r'^companys/$', companys_views.Companys.as_view(), name='companys'),
    url(r'^companys/(?P<pk>\d+)$', companys_views.CompanysDetail.as_view(), name='companysdetail'),
    url(r'^companys/add$', companys_views.companys_add, name='companys_add'),
    url(r'^companys/add_popup$', companys_views.companys_add_popup, name='companys_add_popup'),
    url(r'^companys/(?P<pk>\d+)/edit/$', companys_views.companys_edit, name='companys_edit'),

    url(r'^contacts/$', contacts_views.Contacts.as_view(), name='contacts'),
    url(r'^contacts/(?P<pk>\d+)$', contacts_views.ContactsDetail.as_view(), name='contactsdetail'),
    url(r'^contacts/add$', contacts_views.contacts_add, name='contacts_add'),
    url(r'^contacts/add_popup$', contacts_views.contacts_add_popup, name='contacts_add_popup'),
    url(r'^contacts/(?P<pk>\d+)/edit/$', contacts_views.contacts_edit, name='contacts_edit'),

    url(r'^divisions/$', divisions_views.Divisions.as_view(), name='divisions'),
    url(r'^divisions/(?P<pk>\d+)$', divisions_views.DivisionsDetail.as_view(), name='divisionsdetail'),
    url(r'^divisions/add$', divisions_views.divisions_add, name='divisions_add'),
    url(r'^divisions/(?P<pk>\d+)/edit/$', divisions_views.divisions_edit, name='divisions_edit'),

    url(r'^domains/$', domains_views.Domains.as_view(), name='domains'),
    url(r'^domains/(?P<pk>\d+)$', domains_views.DomainsDetail.as_view(), name='domainsdetail'),
    url(r'^domains/add$', domains_views.domains_add, name='domains_add'),
    url(r'^domains/add_popup$', domains_views.domains_add_popup, name='domains_add_popup'),
    url(r'^domains/(?P<pk>\d+)/edit/$', domains_views.domains_edit, name='domains_edit'),

    url(r'^entrys/$', entrys_views.Entrys.as_view(), name='entrys'),
    url(r'^entrys/(?P<pk>\d+)$', entrys_views.EntrysDetail.as_view(), name='entrysdetail'),
    url(r'^entrys/add$', entrys_views.entrys_add, name='entrys_add'),
    url(r'^entrys/(?P<pk>\d+)/edit/$', entrys_views.entrys_edit, name='entrys_edit'),
    url(r'^entrys/importer/api/giraf/entrys/$', giraf.entrys, name='entrys_importer_api_giraf'),
    url(r'^entrys/importer/file/markdown/entrys/$', markdown.entrys, name='entrys_importer_file_markdown'),

    url(r'^headlines/$', headlines_views.Headlines.as_view(), name='headlines'),
    url(r'^headlines/(?P<pk>\d+)$', headlines_views.HeadlinesDetail.as_view(), name='headlinesdetail'),
    url(r'^headlines/add$', headlines_views.headlines_add, name='headlines_add'),
    url(r'^headlines/(?P<pk>\d+)/edit/$', headlines_views.headlines_edit, name='headlines_edit'),

    url(r'^ips/$', ips_views.Ips.as_view(), name='ips'),
    url(r'^ips/(?P<pk>\d+)$', ips_views.IpsDetail.as_view(), name='ipsdetail'),
    url(r'^ips/add/$', ips_views.ips_add, name='ips_add'),
    url(r'^ips/(?P<pk>\d+)/edit/$', ips_views.ips_edit, name='ips_edit'),

    url(r'^locations/$', locations_views.Locations.as_view(), name='locations'),
    url(r'^locations/(?P<pk>\d+)$', locations_views.LocationsDetail.as_view(), name='locationsdetail'),
    url(r'^locations/add$', locations_views.locations_add, name='locations_add'),
    url(r'^locations/add_popup$', locations_views.locations_add_popup, name='locations_add_popup'),
    url(r'^locations/(?P<pk>\d+)/edit/$', locations_views.locations_edit, name='locations_edit'),

    url(r'^oss/$', oss_views.Oss.as_view(), name='oss'),
    url(r'^oss/(?P<pk>\d+)$', oss_views.OssDetail.as_view(), name='ossdetail'),
    url(r'^oss/add/$', oss_views.oss_add, name='oss_add'),
    url(r'^oss/add_popup$', oss_views.oss_add_popup, name='oss_add_popup'),
    url(r'^oss/(?P<pk>\d+)/edit/$', oss_views.oss_edit, name='oss_edit'),

    url(r'^osimportnames/$', osimportnames_views.Osimportnames.as_view(), name='osimportnames'),
    url(r'^osimportnames/add/$', osimportnames_views.osimportnames_add, name='osimportnames_add'),
    url(r'^osimportnames/(?P<pk>\d+)/edit/$', osimportnames_views.osimportnames_edit, name='osimportnames_edit'),

    url(r'^reasons/$', reasons_views.Reasons.as_view(), name='reasons'),
    url(r'^reasons/(?P<pk>\d+)$', reasons_views.ReasonsDetail.as_view(), name='reasonsdetail'),
    url(r'^reasons/add$', reasons_views.reasons_add, name='reasons_add'),
    url(r'^reasons/add_popup$', reasons_views.reasons_add_popup, name='reasons_add_popup'),
    url(r'^reasons/(?P<pk>\d+)/edit/$', reasons_views.reasons_edit, name='reasons_edit'),

    url(r'^recommendations/$', recommendations_views.Recommendations.as_view(), name='recommendations'),
    url(r'^recommendations/(?P<pk>\d+)$', recommendations_views.RecommendationsDetail.as_view(), name='recommendationsdetail'),
    url(r'^recommendations/add$', recommendations_views.recommendations_add, name='recommendations_add'),
    url(r'^recommendations/add_popup$', recommendations_views.recommendations_add_popup, name='recommendations_add_popup'),
    url(r'^recommendations/(?P<pk>\d+)/edit/$', recommendations_views.recommendations_edit, name='recommendations_edit'),

    url(r'^reportitems/$', reportitems_views.Reportitems.as_view(), name='reportitems'),
    url(r'^reportitems/(?P<pk>\d+)$', reportitems_views.ReportitemsDetail.as_view(), name='reportitemsdetail'),
    url(r'^reportitems/add$', reportitems_views.reportitems_add, name='reportitems_add'),
    url(r'^reportitems/(?P<pk>\d+)/edit/$', reportitems_views.reportitems_edit, name='reportitems_edit'),
    url(r'^reportitems/importer/file/filesystem/reportitems/$', filesystem.reportitems, name='reportitems_importer_file_filesystem'),

    url(r'^serviceproviders/$', serviceproviders_views.Serviceproviders.as_view(), name='serviceproviders'),
    url(r'^serviceproviders/(?P<pk>\d+)$', serviceproviders_views.ServiceprovidersDetail.as_view(), name='serviceprovidersdetail'),
    url(r'^serviceproviders/add$', serviceproviders_views.serviceproviders_add, name='serviceproviders_add'),
    url(r'^serviceproviders/add_popup$', serviceproviders_views.serviceproviders_add_popup, name='serviceproviders_add_popup'),
    url(r'^serviceproviders/(?P<pk>\d+)/edit/$', serviceproviders_views.serviceproviders_edit, name='serviceproviders_edit'),

    url(r'^systems/$', systems_views.Systems.as_view(), name='systems'),
    url(r'^systems/(?P<pk>\d+)$', systems_views.SystemsDetail.as_view(), name='systemsdetail'),
    url(r'^systems/add/$', systems_views.systems_add, name='systems_add'),
    url(r'^systems/(?P<pk>\d+)/edit/$', systems_views.systems_edit, name='systems_edit'),
    url(r'^systems/creator/$', systems_creator.systems_creator, name='systems_creator'),
    url(r'^systems/exporter/markdown/domainsorted/$', domainsorted.domainsorted, name='systems_exporter_markdown_domainsorted'),
    url(r'^systems/exporter/markdown/systemsorted/$', systemsorted.systemsorted, name='systems_exporter_markdown_systemsorted'),
    url(r'^systems/exporter/spreadsheet/csv/systems/$', spreadsheet_csv.systems, name='systems_exporter_spreadsheet_csv'),
    url(r'^systems/exporter/spreadsheet/xls/systems/$', xls.systems, name='systems_exporter_spreadsheet_xls'),
    url(r'^systems/importer/api/giraf/systems/$', giraf.systems, name='systems_importer_api_giraf'),
    url(r'^systems/importer/file/csv/systems_ips/$', file_csv.systems_ips, name='systems_importer_file_csv_systems_ips'),
    url(r'^systems/importer/file/csv/systems_tags/$', file_csv.systems_tags, name='systems_importer_file_csv_systems_tags'),

    url(r'^systemstatuss/$', systemstatuss_views.Systemstatuss.as_view(), name='systemstatuss'),
    url(r'^systemstatuss/(?P<pk>\d+)$', systemstatuss_views.SystemstatussDetail.as_view(), name='systemstatussdetail'),

    url(r'^systemtypes/$', systemtypes_views.Systemtypes.as_view(), name='systemtypes'),
    url(r'^systemtypes/(?P<pk>\d+)$', systemtypes_views.SystemtypesDetail.as_view(), name='systemtypesdetail'),
    url(r'^systemtypes/add$', systemtypes_views.systemtypes_add, name='systemtypes_add'),
    url(r'^systemtypes/add_popup$', systemtypes_views.systemtypes_add_popup, name='systemtypes_add_popup'),
    url(r'^systemtypes/(?P<pk>\d+)/edit/$', systemtypes_views.systemtypes_edit, name='systemtypes_edit'),

    url(r'^systemusers/$', systemusers_views.Systemusers.as_view(), name='systemusers'),
    url(r'^systemusers/(?P<pk>\d+)$', systemusers_views.SystemusersDetail.as_view(), name='systemusersdetail'),
    url(r'^systemusers/add$', systemusers_views.systemusers_add, name='systemusers_add'),
    url(r'^systemusers/(?P<pk>\d+)/edit/$', systemusers_views.systemusers_edit, name='systemusers_edit'),

    url(r'^tags/$', tags_views.Tags.as_view(), name='tags'),
    url(r'^tags/(?P<pk>\d+)$', tags_views.TagsDetail.as_view(), name='tagsdetail'),
    url(r'^tags/add$', tags_views.tags_add, name='tags_add'),
    url(r'^tags/(?P<pk>\d+)/edit/$', tags_views.tags_edit, name='tags_edit'),
    url(r'^tags/(?P<pk>\d+)/delete/$', tags_views.tags_delete, name='tags_delete'),

    url(r'^tasks/$', tasks_views.Tasks.as_view(), name='tasks'),
    url(r'^tasks/(?P<pk>\d+)$', tasks_views.TasksDetail.as_view(), name='tasksdetail'),
    url(r'^tasks/add/$', tasks_views.tasks_add, name='tasks_add'),
    url(r'^tasks/(?P<pk>\d+)/edit/$', tasks_views.tasks_edit, name='tasks_edit'),
    url(r'^tasks/creator$', tasks_creator.tasks_creator, name='tasks_creator'),

    url(r'^tasks/(?P<pk>\d+)/start/$', tasks_views.tasks_start, name='tasks_start'),
    url(r'^tasks/(?P<pk>\d+)/finish/$', tasks_views.tasks_finish, name='tasks_finish'),
    url(r'^tasks/(?P<pk>\d+)/renew/$', tasks_views.tasks_renew, name='tasks_renew'),
    url(r'^tasks/(?P<pk>\d+)/set_user/$', tasks_views.tasks_set_user, name='tasks_set_user'),
    url(r'^tasks/(?P<pk>\d+)/unset_user/$', tasks_views.tasks_unset_user, name='tasks_unset_user'),

    url(r'^tasknames/$', tasknames_views.Tasknames.as_view(), name='tasknames'),
    url(r'^tasknames/(?P<pk>\d+)$', tasknames_views.TasknamesDetail.as_view(), name='tasknamesdetail'),
    url(r'^tasknames/add$', tasknames_views.tasknames_add, name='tasknames_add'),
    url(r'^tasknames/(?P<pk>\d+)/edit/$', tasknames_views.tasknames_edit, name='tasknames_edit'),

    url(r'^taskprioritys/$', taskprioritys_views.Taskprioritys.as_view(), name='taskprioritys'),
    url(r'^taskprioritys/(?P<pk>\d+)$', taskprioritys_views.TaskprioritysDetail.as_view(), name='taskprioritysdetail'),

    url(r'^taskstatuss/$', taskstatuss_views.Taskstatuss.as_view(), name='taskstatuss'),
    url(r'^taskstatuss/(?P<pk>\d+)$', taskstatuss_views.TaskstatussDetail.as_view(), name='taskstatussdetail'),

]
