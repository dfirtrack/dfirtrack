from django.conf.urls import url
from dfirtrack_main.views import generic_views
from dfirtrack_main.views import analysisstatus_views, analystmemo_views, case_views, company_views, contact_views, division_views, dnsname_views, domain_views, domainuser_views, entry_views, headline_views, ip_views, location_views, os_views, osimportname_views, reason_views, recommendation_views, reportitem_views, serviceprovider_views, system_views, systemstatus_views, systemtype_views, systemuser_views, tag_views, task_views, taskname_views, taskpriority_views, taskstatus_views
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

    url(r'^analysisstatuss/$', analysisstatus_views.AnalysisstatusList.as_view(), name='analysisstatuslist'),
    url(r'^analysisstatuss/(?P<pk>\d+)$', analysisstatus_views.AnalysisstatusDetail.as_view(), name='analysisstatusdetail'),

    url(r'^analystmemos/$', analystmemo_views.AnalystmemoList.as_view(), name='analystmemolist'),
    url(r'^analystmemos/(?P<pk>\d+)$', analystmemo_views.AnalystmemoDetail.as_view(), name='analystmemodetail'),
    url(r'^analystmemos/add/$', analystmemo_views.AnalystmemoCreate.as_view(), name='analystmemos_add'),
    url(r'^analystmemos/(?P<pk>\d+)/edit/$', analystmemo_views.AnalystmemoUpdate.as_view(), name='analystmemos_edit'),

    url(r'^cases/$', case_views.CaseList.as_view(), name='caselist'),
    url(r'^cases/(?P<pk>\d+)$', case_views.CaseDetail.as_view(), name='casedetail'),
    url(r'^cases/add/$', case_views.CaseCreate.as_view(), name='cases_add'),
    url(r'^cases/(?P<pk>\d+)/edit/$', case_views.CaseUpdate.as_view(), name='cases_edit'),

    url(r'^companys/$', company_views.CompanyList.as_view(), name='companylist'),
    url(r'^companys/(?P<pk>\d+)$', company_views.CompanyDetail.as_view(), name='companydetail'),
    url(r'^companys/add/$', company_views.CompanyCreate.as_view(), name='companys_add'),
    url(r'^companys/add_popup$', company_views.CompanyCreatePopup.as_view(), name='companys_add_popup'),
    url(r'^companys/(?P<pk>\d+)/edit/$', company_views.CompanyUpdate.as_view(), name='companys_edit'),

    url(r'^contacts/$', contact_views.ContactList.as_view(), name='contactlist'),
    url(r'^contacts/(?P<pk>\d+)$', contact_views.ContactDetail.as_view(), name='contactdetail'),
    url(r'^contacts/add/$', contact_views.contacts_add, name='contacts_add'),
    url(r'^contacts/add_popup$', contact_views.contacts_add_popup, name='contacts_add_popup'),
    url(r'^contacts/(?P<pk>\d+)/edit/$', contact_views.contacts_edit, name='contacts_edit'),

    url(r'^divisions/$', division_views.DivisionList.as_view(), name='divisionlist'),
    url(r'^divisions/(?P<pk>\d+)$', division_views.DivisionDetail.as_view(), name='divisiondetail'),
    url(r'^divisions/add/$', division_views.divisions_add, name='divisions_add'),
    url(r'^divisions/(?P<pk>\d+)/edit/$', division_views.divisions_edit, name='divisions_edit'),

    url(r'^dnsnames/$', dnsname_views.DnsnameList.as_view(), name='dnsnamelist'),
    url(r'^dnsnames/(?P<pk>\d+)$', dnsname_views.DnsnameDetail.as_view(), name='dnsnamedetail'),
    url(r'^dnsnames/add/$', dnsname_views.dnsnames_add, name='dnsnames_add'),
    url(r'^dnsnames/add_popup$', dnsname_views.dnsnames_add_popup, name='dnsnames_add_popup'),
    url(r'^dnsnames/(?P<pk>\d+)/edit/$', dnsname_views.dnsnames_edit, name='dnsnames_edit'),

    url(r'^domains/$', domain_views.DomainList.as_view(), name='domainlist'),
    url(r'^domains/(?P<pk>\d+)$', domain_views.DomainDetail.as_view(), name='domaindetail'),
    url(r'^domains/add/$', domain_views.DomainCreate.as_view(), name='domains_add'),
    url(r'^domains/add_popup$', domain_views.DomainCreatePopup.as_view(), name='domains_add_popup'),
    url(r'^domains/(?P<pk>\d+)/edit/$', domain_views.DomainUpdate.as_view(), name='domains_edit'),

    url(r'^domainusers/$', domainuser_views.DomainuserList.as_view(), name='domainuserlist'),
    url(r'^domainusers/(?P<pk>\d+)$', domainuser_views.DomainuserDetail.as_view(), name='domainuserdetail'),
    url(r'^domainusers/add/$', domainuser_views.domainusers_add, name='domainusers_add'),
    url(r'^domainusers/(?P<pk>\d+)/edit/$', domainuser_views.domainusers_edit, name='domainusers_edit'),

    url(r'^entrys/$', entry_views.EntryList.as_view(), name='entrylist'),
    url(r'^entrys/(?P<pk>\d+)$', entry_views.EntryDetail.as_view(), name='entrydetail'),
    url(r'^entrys/add/$', entry_views.entrys_add, name='entrys_add'),
    url(r'^entrys/(?P<pk>\d+)/edit/$', entry_views.entrys_edit, name='entrys_edit'),
    url(r'^entrys/importer/api/giraf/entrys/$', giraf.entrys, name='entrys_importer_api_giraf'),
    url(r'^entrys/importer/file/markdown/entrys/$', markdown.entrys, name='entrys_importer_file_markdown'),

    url(r'^headlines/$', headline_views.HeadlineList.as_view(), name='headlinelist'),
    url(r'^headlines/(?P<pk>\d+)$', headline_views.HeadlineDetail.as_view(), name='headlinedetail'),
    url(r'^headlines/add/$', headline_views.headlines_add, name='headlines_add'),
    url(r'^headlines/(?P<pk>\d+)/edit/$', headline_views.headlines_edit, name='headlines_edit'),

    url(r'^ips/$', ip_views.IpList.as_view(), name='iplist'),
    url(r'^ips/(?P<pk>\d+)$', ip_views.IpDetail.as_view(), name='ipdetail'),

    url(r'^locations/$', location_views.LocationList.as_view(), name='locationlist'),
    url(r'^locations/(?P<pk>\d+)$', location_views.LocationDetail.as_view(), name='locationdetail'),
    url(r'^locations/add/$', location_views.locations_add, name='locations_add'),
    url(r'^locations/add_popup$', location_views.locations_add_popup, name='locations_add_popup'),
    url(r'^locations/(?P<pk>\d+)/edit/$', location_views.locations_edit, name='locations_edit'),

    url(r'^oss/$', os_views.OsList.as_view(), name='oslist'),
    url(r'^oss/(?P<pk>\d+)$', os_views.OsDetail.as_view(), name='osdetail'),
    url(r'^oss/add/$', os_views.oss_add, name='oss_add'),
    url(r'^oss/add_popup$', os_views.oss_add_popup, name='oss_add_popup'),
    url(r'^oss/(?P<pk>\d+)/edit/$', os_views.oss_edit, name='oss_edit'),

    url(r'^osimportnames/$', osimportname_views.OsimportnameList.as_view(), name='osimportnamelist'),
    url(r'^osimportnames/add/$', osimportname_views.osimportnames_add, name='osimportnames_add'),
    url(r'^osimportnames/(?P<pk>\d+)/edit/$', osimportname_views.osimportnames_edit, name='osimportnames_edit'),

    url(r'^reasons/$', reason_views.ReasonList.as_view(), name='reasonlist'),
    url(r'^reasons/(?P<pk>\d+)$', reason_views.ReasonDetail.as_view(), name='reasondetail'),
    url(r'^reasons/add/$', reason_views.reasons_add, name='reasons_add'),
    url(r'^reasons/add_popup$', reason_views.reasons_add_popup, name='reasons_add_popup'),
    url(r'^reasons/(?P<pk>\d+)/edit/$', reason_views.reasons_edit, name='reasons_edit'),

    url(r'^recommendations/$', recommendation_views.RecommendationList.as_view(), name='recommendationlist'),
    url(r'^recommendations/(?P<pk>\d+)$', recommendation_views.RecommendationDetail.as_view(), name='recommendationdetail'),
    url(r'^recommendations/add/$', recommendation_views.recommendations_add, name='recommendations_add'),
    url(r'^recommendations/add_popup$', recommendation_views.recommendations_add_popup, name='recommendations_add_popup'),
    url(r'^recommendations/(?P<pk>\d+)/edit/$', recommendation_views.recommendations_edit, name='recommendations_edit'),

    url(r'^reportitems/$', reportitem_views.ReportitemList.as_view(), name='reportitemlist'),
    url(r'^reportitems/(?P<pk>\d+)$', reportitem_views.ReportitemDetail.as_view(), name='reportitemdetail'),
    url(r'^reportitems/add/$', reportitem_views.reportitems_add, name='reportitems_add'),
    url(r'^reportitems/(?P<pk>\d+)/edit/$', reportitem_views.reportitems_edit, name='reportitems_edit'),
    url(r'^reportitems/importer/file/filesystem/reportitems/$', filesystem.reportitems, name='reportitems_importer_file_filesystem'),

    url(r'^serviceproviders/$', serviceprovider_views.ServiceproviderList.as_view(), name='serviceproviderlist'),
    url(r'^serviceproviders/(?P<pk>\d+)$', serviceprovider_views.ServiceproviderDetail.as_view(), name='serviceproviderdetail'),
    url(r'^serviceproviders/add/$', serviceprovider_views.serviceproviders_add, name='serviceproviders_add'),
    url(r'^serviceproviders/add_popup$', serviceprovider_views.serviceproviders_add_popup, name='serviceproviders_add_popup'),
    url(r'^serviceproviders/(?P<pk>\d+)/edit/$', serviceprovider_views.serviceproviders_edit, name='serviceproviders_edit'),

    url(r'^systems/$', system_views.SystemList.as_view(), name='systemlist'),
    url(r'^systems/(?P<pk>\d+)$', system_views.SystemDetail.as_view(), name='systemdetail'),
    url(r'^systems/add/$', system_views.systems_add, name='systems_add'),
    url(r'^systems/(?P<pk>\d+)/edit/$', system_views.systems_edit, name='systems_edit'),
    url(r'^systems/creator/$', systems_creator.systems_creator, name='systems_creator'),
    url(r'^systems/exporter/markdown/domainsorted/$', domainsorted.domainsorted, name='systems_exporter_markdown_domainsorted'),
    url(r'^systems/exporter/markdown/systemsorted/$', systemsorted.systemsorted, name='systems_exporter_markdown_systemsorted'),
    url(r'^systems/exporter/spreadsheet/csv/systems/$', spreadsheet_csv.systems, name='systems_exporter_spreadsheet_csv'),
    url(r'^systems/exporter/spreadsheet/xls/systems/$', xls.systems, name='systems_exporter_spreadsheet_xls'),
    url(r'^systems/importer/api/giraf/systems/$', giraf.systems, name='systems_importer_api_giraf'),
    url(r'^systems/importer/file/csv/systems_ips/$', file_csv.systems_ips, name='systems_importer_file_csv_systems_ips'),
    url(r'^systems/importer/file/csv/systems_tags/$', file_csv.systems_tags, name='systems_importer_file_csv_systems_tags'),

    url(r'^systemstatuss/$', systemstatus_views.SystemstatusList.as_view(), name='systemstatuslist'),
    url(r'^systemstatuss/(?P<pk>\d+)$', systemstatus_views.SystemstatusDetail.as_view(), name='systemstatusdetail'),

    url(r'^systemtypes/$', systemtype_views.SystemtypeList.as_view(), name='systemtypelist'),
    url(r'^systemtypes/(?P<pk>\d+)$', systemtype_views.SystemtypeDetail.as_view(), name='systemtypedetail'),
    url(r'^systemtypes/add/$', systemtype_views.systemtypes_add, name='systemtypes_add'),
    url(r'^systemtypes/add_popup$', systemtype_views.systemtypes_add_popup, name='systemtypes_add_popup'),
    url(r'^systemtypes/(?P<pk>\d+)/edit/$', systemtype_views.systemtypes_edit, name='systemtypes_edit'),

    url(r'^systemusers/$', systemuser_views.SystemuserList.as_view(), name='systemuserlist'),
    url(r'^systemusers/(?P<pk>\d+)$', systemuser_views.SystemuserDetail.as_view(), name='systemuserdetail'),
    url(r'^systemusers/add/$', systemuser_views.systemusers_add, name='systemusers_add'),
    url(r'^systemusers/(?P<pk>\d+)/edit/$', systemuser_views.systemusers_edit, name='systemusers_edit'),

    url(r'^tags/$', tag_views.TagList.as_view(), name='taglist'),
    url(r'^tags/(?P<pk>\d+)$', tag_views.TagDetail.as_view(), name='tagdetail'),
    url(r'^tags/add/$', tag_views.tags_add, name='tags_add'),
    url(r'^tags/(?P<pk>\d+)/edit/$', tag_views.tags_edit, name='tags_edit'),
    url(r'^tags/(?P<pk>\d+)/delete/$', tag_views.tags_delete, name='tags_delete'),

    url(r'^tasks/$', task_views.TaskList.as_view(), name='tasklist'),
    url(r'^tasks/closed$', task_views.TaskClosed.as_view(), name='taskclosed'),
    url(r'^tasks/(?P<pk>\d+)$', task_views.TaskDetail.as_view(), name='taskdetail'),
    url(r'^tasks/add/$', task_views.tasks_add, name='tasks_add'),
    url(r'^tasks/(?P<pk>\d+)/edit/$', task_views.tasks_edit, name='tasks_edit'),
    url(r'^tasks/creator$', tasks_creator.tasks_creator, name='tasks_creator'),

    url(r'^tasks/(?P<pk>\d+)/start/$', task_views.tasks_start, name='tasks_start'),
    url(r'^tasks/(?P<pk>\d+)/finish/$', task_views.tasks_finish, name='tasks_finish'),
    url(r'^tasks/(?P<pk>\d+)/renew/$', task_views.tasks_renew, name='tasks_renew'),
    url(r'^tasks/(?P<pk>\d+)/set_user/$', task_views.tasks_set_user, name='tasks_set_user'),
    url(r'^tasks/(?P<pk>\d+)/unset_user/$', task_views.tasks_unset_user, name='tasks_unset_user'),

    url(r'^tasknames/$', taskname_views.TasknameList.as_view(), name='tasknamelist'),
    url(r'^tasknames/(?P<pk>\d+)$', taskname_views.TasknameDetail.as_view(), name='tasknamedetail'),
    url(r'^tasknames/add/$', taskname_views.tasknames_add, name='tasknames_add'),
    url(r'^tasknames/(?P<pk>\d+)/edit/$', taskname_views.tasknames_edit, name='tasknames_edit'),

    url(r'^taskprioritys/$', taskpriority_views.TaskpriorityList.as_view(), name='taskprioritylist'),
    url(r'^taskprioritys/(?P<pk>\d+)$', taskpriority_views.TaskpriorityDetail.as_view(), name='taskprioritydetail'),

    url(r'^taskstatuss/$', taskstatus_views.TaskstatusList.as_view(), name='taskstatuslist'),
    url(r'^taskstatuss/(?P<pk>\d+)$', taskstatus_views.TaskstatusDetail.as_view(), name='taskstatusdetail'),

]
