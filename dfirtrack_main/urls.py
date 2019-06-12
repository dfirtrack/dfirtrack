from django.conf.urls import url
from dfirtrack_main.views import generic_views
from dfirtrack_main.views import analysisstatuss_views, analystmemos_views, cases_views, companys_views, contacts_views, divisions_views, dnsnames_views, domains_views, domainusers_views, entrys_views, headlines_views, ips_views, locations_views, oss_views, osimportnames_views, reasons_views, recommendations_views, reportitems_views, serviceproviders_views, systems_views, systemstatuss_views, systemtypes_views, systemusers_views, tags_views, tasks_views, tasknames_views, taskprioritys_views, taskstatuss_views
from dfirtrack_main.creator import systems_creator, tasks_creator
from dfirtrack_main.exporter.spreadsheet import csv as spreadsheet_csv
from dfirtrack_main.exporter.spreadsheet import xls
from dfirtrack_main.exporter.markdown import domainsorted, systemsorted
from dfirtrack_main.importer.api import giraf
from dfirtrack_main.importer.file import csv as file_csv
from dfirtrack_main.importer.file import filesystem, markdown
from dfirtrack_main.models import Analysisstatus, Analystmemo, Case, Company, Contact, Division, Dnsname, Domain, Domainuser, Entry, Headline, Ip, Location, Os, Osimportname, Reason, Recommendation, Reportitem, Serviceprovider, System, Systemstatus, Systemtype, Systemuser, Tag, Task, Taskname, Taskpriority, Taskstatus

urlpatterns = [

    url(r'^about/$', generic_views.about, name='about'),
    url(r'^faq/$', generic_views.faq, name='faq'),

    url(r'^analysisstatuss/$', analysisstatuss_views.AnalysisstatusList.as_view(), name='analysisstatuslist'),
    url(r'^analysisstatuss/(?P<pk>\d+)$', analysisstatuss_views.AnalysisstatusDetail.as_view(), name='analysisstatusdetail'),

    url(r'^analystmemos/$', analystmemos_views.AnalystmemoList.as_view(), name='analystmemolist'),
    url(r'^analystmemos/(?P<pk>\d+)$', analystmemos_views.AnalystmemoDetail.as_view(), name='analystmemodetail'),
    url(r'^analystmemos/add/$', analystmemos_views.analystmemos_add, name='analystmemos_add'),
    url(r'^analystmemos/(?P<pk>\d+)/edit/$', analystmemos_views.analystmemos_edit, name='analystmemos_edit'),

    url(r'^cases/$', cases_views.CaseList.as_view(), name='caselist'),
    url(r'^cases/(?P<pk>\d+)$', cases_views.CaseDetail.as_view(), name='casedetail'),
    url(r'^cases/add/$', cases_views.cases_add, name='cases_add'),
    url(r'^cases/(?P<pk>\d+)/edit/$', cases_views.cases_edit, name='cases_edit'),

    url(r'^companys/$', companys_views.CompanyList.as_view(), name='companylist'),
    url(r'^companys/(?P<pk>\d+)$', companys_views.CompanyDetail.as_view(), name='companydetail'),
    url(r'^companys/add/$', companys_views.companys_add, name='companys_add'),
    url(r'^companys/add_popup$', companys_views.companys_add_popup, name='companys_add_popup'),
    url(r'^companys/(?P<pk>\d+)/edit/$', companys_views.companys_edit, name='companys_edit'),

    url(r'^contacts/$', contacts_views.ContactList.as_view(), name='contactlist'),
    url(r'^contacts/(?P<pk>\d+)$', contacts_views.ContactDetail.as_view(), name='contactdetail'),
    url(r'^contacts/add/$', contacts_views.contacts_add, name='contacts_add'),
    url(r'^contacts/add_popup$', contacts_views.contacts_add_popup, name='contacts_add_popup'),
    url(r'^contacts/(?P<pk>\d+)/edit/$', contacts_views.contacts_edit, name='contacts_edit'),

    url(r'^divisions/$', divisions_views.DivisionList.as_view(), name='divisionlist'),
    url(r'^divisions/(?P<pk>\d+)$', divisions_views.DivisionDetail.as_view(), name='divisiondetail'),
    url(r'^divisions/add/$', divisions_views.divisions_add, name='divisions_add'),
    url(r'^divisions/(?P<pk>\d+)/edit/$', divisions_views.divisions_edit, name='divisions_edit'),

    url(r'^dnsnames/$', dnsnames_views.DnsnameList.as_view(), name='dnsnamelist'),
    url(r'^dnsnames/(?P<pk>\d+)$', dnsnames_views.DnsnameDetail.as_view(), name='dnsnamedetail'),
    url(r'^dnsnames/add/$', dnsnames_views.dnsnames_add, name='dnsnames_add'),
    url(r'^dnsnames/add_popup$', dnsnames_views.dnsnames_add_popup, name='dnsnames_add_popup'),
    url(r'^dnsnames/(?P<pk>\d+)/edit/$', dnsnames_views.dnsnames_edit, name='dnsnames_edit'),

    url(r'^domains/$', domains_views.DomainList.as_view(), name='domainlist'),
    url(r'^domains/(?P<pk>\d+)$', domains_views.DomainDetail.as_view(), name='domaindetail'),
    url(r'^domains/add/$', domains_views.domains_add, name='domains_add'),
    url(r'^domains/add_popup$', domains_views.domains_add_popup, name='domains_add_popup'),
    url(r'^domains/(?P<pk>\d+)/edit/$', domains_views.domains_edit, name='domains_edit'),

    url(r'^domainusers/$', domainusers_views.DomainuserList.as_view(), name='domainuserlist'),
    url(r'^domainusers/(?P<pk>\d+)$', domainusers_views.DomainuserDetail.as_view(), name='domainuserdetail'),
    url(r'^domainusers/add/$', domainusers_views.domainusers_add, name='domainusers_add'),
    url(r'^domainusers/(?P<pk>\d+)/edit/$', domainusers_views.domainusers_edit, name='domainusers_edit'),

    url(r'^entrys/$', entrys_views.EntryList.as_view(), name='entrylist'),
    url(r'^entrys/(?P<pk>\d+)$', entrys_views.EntryDetail.as_view(), name='entrydetail'),
    url(r'^entrys/add/$', entrys_views.entrys_add, name='entrys_add'),
    url(r'^entrys/(?P<pk>\d+)/edit/$', entrys_views.entrys_edit, name='entrys_edit'),
    url(r'^entrys/importer/api/giraf/entrys/$', giraf.entrys, name='entrys_importer_api_giraf'),
    url(r'^entrys/importer/file/markdown/entrys/$', markdown.entrys, name='entrys_importer_file_markdown'),

    url(r'^headlines/$', headlines_views.HeadlineList.as_view(), name='headlinelist'),
    url(r'^headlines/(?P<pk>\d+)$', headlines_views.HeadlineDetail.as_view(), name='headlinedetail'),
    url(r'^headlines/add/$', headlines_views.headlines_add, name='headlines_add'),
    url(r'^headlines/(?P<pk>\d+)/edit/$', headlines_views.headlines_edit, name='headlines_edit'),

    url(r'^ips/$', ips_views.IpList.as_view(), name='iplist'),
    url(r'^ips/(?P<pk>\d+)$', ips_views.IpDetail.as_view(), name='ipdetail'),

    url(r'^locations/$', locations_views.LocationList.as_view(), name='locationlist'),
    url(r'^locations/(?P<pk>\d+)$', locations_views.LocationDetail.as_view(), name='locationdetail'),
    url(r'^locations/add/$', locations_views.locations_add, name='locations_add'),
    url(r'^locations/add_popup$', locations_views.locations_add_popup, name='locations_add_popup'),
    url(r'^locations/(?P<pk>\d+)/edit/$', locations_views.locations_edit, name='locations_edit'),

    url(r'^oss/$', oss_views.OsList.as_view(), name='oslist'),
    url(r'^oss/(?P<pk>\d+)$', oss_views.OsDetail.as_view(), name='osdetail'),
    url(r'^oss/add/$', oss_views.oss_add, name='oss_add'),
    url(r'^oss/add_popup$', oss_views.oss_add_popup, name='oss_add_popup'),
    url(r'^oss/(?P<pk>\d+)/edit/$', oss_views.oss_edit, name='oss_edit'),

    url(r'^osimportnames/$', osimportnames_views.OsimportnameList.as_view(), name='osimportnamelist'),
    url(r'^osimportnames/add/$', osimportnames_views.osimportnames_add, name='osimportnames_add'),
    url(r'^osimportnames/(?P<pk>\d+)/edit/$', osimportnames_views.osimportnames_edit, name='osimportnames_edit'),

    url(r'^reasons/$', reasons_views.ReasonList.as_view(), name='reasonlist'),
    url(r'^reasons/(?P<pk>\d+)$', reasons_views.ReasonDetail.as_view(), name='reasondetail'),
    url(r'^reasons/add/$', reasons_views.reasons_add, name='reasons_add'),
    url(r'^reasons/add_popup$', reasons_views.reasons_add_popup, name='reasons_add_popup'),
    url(r'^reasons/(?P<pk>\d+)/edit/$', reasons_views.reasons_edit, name='reasons_edit'),

    url(r'^recommendations/$', recommendations_views.RecommendationList.as_view(), name='recommendationlist'),
    url(r'^recommendations/(?P<pk>\d+)$', recommendations_views.RecommendationDetail.as_view(), name='recommendationdetail'),
    url(r'^recommendations/add/$', recommendations_views.recommendations_add, name='recommendations_add'),
    url(r'^recommendations/add_popup$', recommendations_views.recommendations_add_popup, name='recommendations_add_popup'),
    url(r'^recommendations/(?P<pk>\d+)/edit/$', recommendations_views.recommendations_edit, name='recommendations_edit'),

    url(r'^reportitems/$', reportitems_views.ReportitemList.as_view(), name='reportitemlist'),
    url(r'^reportitems/(?P<pk>\d+)$', reportitems_views.ReportitemDetail.as_view(), name='reportitemdetail'),
    url(r'^reportitems/add/$', reportitems_views.reportitems_add, name='reportitems_add'),
    url(r'^reportitems/(?P<pk>\d+)/edit/$', reportitems_views.reportitems_edit, name='reportitems_edit'),
    url(r'^reportitems/importer/file/filesystem/reportitems/$', filesystem.reportitems, name='reportitems_importer_file_filesystem'),

    url(r'^serviceproviders/$', serviceproviders_views.ServiceproviderList.as_view(), name='serviceproviderlist'),
    url(r'^serviceproviders/(?P<pk>\d+)$', serviceproviders_views.ServiceproviderDetail.as_view(), name='serviceproviderdetail'),
    url(r'^serviceproviders/add/$', serviceproviders_views.serviceproviders_add, name='serviceproviders_add'),
    url(r'^serviceproviders/add_popup$', serviceproviders_views.serviceproviders_add_popup, name='serviceproviders_add_popup'),
    url(r'^serviceproviders/(?P<pk>\d+)/edit/$', serviceproviders_views.serviceproviders_edit, name='serviceproviders_edit'),

    url(r'^systems/$', systems_views.SystemList.as_view(), name='systemlist'),
    url(r'^systems/(?P<pk>\d+)$', systems_views.SystemDetail.as_view(), name='systemdetail'),
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

    url(r'^systemstatuss/$', systemstatuss_views.SystemstatusList.as_view(), name='systemstatuslist'),
    url(r'^systemstatuss/(?P<pk>\d+)$', systemstatuss_views.SystemstatusDetail.as_view(), name='systemstatusdetail'),

    url(r'^systemtypes/$', systemtypes_views.SystemtypeList.as_view(), name='systemtypelist'),
    url(r'^systemtypes/(?P<pk>\d+)$', systemtypes_views.SystemtypeDetail.as_view(), name='systemtypedetail'),
    url(r'^systemtypes/add/$', systemtypes_views.systemtypes_add, name='systemtypes_add'),
    url(r'^systemtypes/add_popup$', systemtypes_views.systemtypes_add_popup, name='systemtypes_add_popup'),
    url(r'^systemtypes/(?P<pk>\d+)/edit/$', systemtypes_views.systemtypes_edit, name='systemtypes_edit'),

    url(r'^systemusers/$', systemusers_views.SystemuserList.as_view(), name='systemuserlist'),
    url(r'^systemusers/(?P<pk>\d+)$', systemusers_views.SystemuserDetail.as_view(), name='systemuserdetail'),
    url(r'^systemusers/add/$', systemusers_views.systemusers_add, name='systemusers_add'),
    url(r'^systemusers/(?P<pk>\d+)/edit/$', systemusers_views.systemusers_edit, name='systemusers_edit'),

    url(r'^tags/$', tags_views.TagList.as_view(), name='taglist'),
    url(r'^tags/(?P<pk>\d+)$', tags_views.TagDetail.as_view(), name='tagdetail'),
    url(r'^tags/add/$', tags_views.tags_add, name='tags_add'),
    url(r'^tags/(?P<pk>\d+)/edit/$', tags_views.tags_edit, name='tags_edit'),
    url(r'^tags/(?P<pk>\d+)/delete/$', tags_views.tags_delete, name='tags_delete'),

    url(r'^tasks/$', tasks_views.TaskList.as_view(), name='tasklist'),
    url(r'^tasks/closed$', tasks_views.TaskClosed.as_view(), name='taskclosed'),
    url(r'^tasks/(?P<pk>\d+)$', tasks_views.TaskDetail.as_view(), name='taskdetail'),
    url(r'^tasks/add/$', tasks_views.tasks_add, name='tasks_add'),
    url(r'^tasks/(?P<pk>\d+)/edit/$', tasks_views.tasks_edit, name='tasks_edit'),
    url(r'^tasks/creator$', tasks_creator.tasks_creator, name='tasks_creator'),

    url(r'^tasks/(?P<pk>\d+)/start/$', tasks_views.tasks_start, name='tasks_start'),
    url(r'^tasks/(?P<pk>\d+)/finish/$', tasks_views.tasks_finish, name='tasks_finish'),
    url(r'^tasks/(?P<pk>\d+)/renew/$', tasks_views.tasks_renew, name='tasks_renew'),
    url(r'^tasks/(?P<pk>\d+)/set_user/$', tasks_views.tasks_set_user, name='tasks_set_user'),
    url(r'^tasks/(?P<pk>\d+)/unset_user/$', tasks_views.tasks_unset_user, name='tasks_unset_user'),

    url(r'^tasknames/$', tasknames_views.TasknameList.as_view(), name='tasknamelist'),
    url(r'^tasknames/(?P<pk>\d+)$', tasknames_views.TasknameDetail.as_view(), name='tasknamedetail'),
    url(r'^tasknames/add/$', tasknames_views.tasknames_add, name='tasknames_add'),
    url(r'^tasknames/(?P<pk>\d+)/edit/$', tasknames_views.tasknames_edit, name='tasknames_edit'),

    url(r'^taskprioritys/$', taskprioritys_views.TaskpriorityList.as_view(), name='taskprioritylist'),
    url(r'^taskprioritys/(?P<pk>\d+)$', taskprioritys_views.TaskpriorityDetail.as_view(), name='taskprioritydetail'),

    url(r'^taskstatuss/$', taskstatuss_views.TaskstatusList.as_view(), name='taskstatuslist'),
    url(r'^taskstatuss/(?P<pk>\d+)$', taskstatuss_views.TaskstatusDetail.as_view(), name='taskstatusdetail'),

]
