from django.conf.urls import url
from dfirtrack_main.views import generic_views
from dfirtrack_main.views import analysisstatus_views, analystmemo_views, case_views, company_views, contact_views, division_views, dnsname_views, domain_views, domainuser_views, entry_views, headline_views, ip_views, location_views, os_views, osimportname_views, reason_views, recommendation_views, reportitem_views, serviceprovider_views, system_views, systemstatus_views, systemtype_views, systemuser_views, tag_views, task_views, taskname_views, taskpriority_views, taskstatus_views
from dfirtrack_main.creator import systems_creator, tags_creator, tasks_creator
from dfirtrack_main.exporter.spreadsheet import csv as spreadsheet_csv
from dfirtrack_main.exporter.spreadsheet import xls
from dfirtrack_main.exporter.markdown import domainsorted, systemsorted
from dfirtrack_main.importer.api import giraf
from dfirtrack_main.importer.file import csv as file_csv
from dfirtrack_main.importer.file import filesystem, markdown
from dfirtrack_main.models import Analysisstatus, Analystmemo, Case, Company, Contact, Division, Dnsname, Domain, Domainuser, Entry, Headline, Ip, Location, Os, Osimportname, Reason, Recommendation, Reportitem, Serviceprovider, System, Systemstatus, Systemtype, Systemuser, Tag, Task, Taskname, Taskpriority, Taskstatus

urlpatterns = [

    url(r'^about/$', generic_views.AboutView.as_view(), name='about'),
    url(r'^faq/$', generic_views.FaqView.as_view(), name='faq'),

    url(r'^analysisstatus/$', analysisstatus_views.AnalysisstatusList.as_view(), name='analysisstatuslist'),
    url(r'^analysisstatus/(?P<pk>\d+)/$', analysisstatus_views.AnalysisstatusDetail.as_view(), name='analysisstatusdetail'),

    url(r'^analystmemo/$', analystmemo_views.AnalystmemoList.as_view(), name='analystmemolist'),
    url(r'^analystmemo/(?P<pk>\d+)/$', analystmemo_views.AnalystmemoDetail.as_view(), name='analystmemodetail'),
    url(r'^analystmemo/add/$', analystmemo_views.AnalystmemoCreate.as_view(), name='analystmemo_add'),
    url(r'^analystmemo/(?P<pk>\d+)/edit/$', analystmemo_views.AnalystmemoUpdate.as_view(), name='analystmemo_edit'),

    url(r'^case/$', case_views.CaseList.as_view(), name='caselist'),
    url(r'^case/(?P<pk>\d+)/$', case_views.CaseDetail.as_view(), name='casedetail'),
    url(r'^case/add/$', case_views.CaseCreate.as_view(), name='case_add'),
    url(r'^case/(?P<pk>\d+)/edit/$', case_views.CaseUpdate.as_view(), name='case_edit'),

    url(r'^company/$', company_views.CompanyList.as_view(), name='companylist'),
    url(r'^company/(?P<pk>\d+)/$', company_views.CompanyDetail.as_view(), name='companydetail'),
    url(r'^company/add/$', company_views.CompanyCreate.as_view(), name='company_add'),
    url(r'^company/add_popup/$', company_views.CompanyCreatePopup.as_view(), name='company_add_popup'),
    url(r'^company/(?P<pk>\d+)/edit/$', company_views.CompanyUpdate.as_view(), name='company_edit'),

    url(r'^contact/$', contact_views.ContactList.as_view(), name='contactlist'),
    url(r'^contact/(?P<pk>\d+)/$', contact_views.ContactDetail.as_view(), name='contactdetail'),
    url(r'^contact/add/$', contact_views.ContactCreate.as_view(), name='contact_add'),
    url(r'^contact/add_popup/$', contact_views.ContactCreatePopup.as_view(), name='contact_add_popup'),
    url(r'^contact/(?P<pk>\d+)/edit/$', contact_views.ContactUpdate.as_view(), name='contact_edit'),

    url(r'^division/$', division_views.DivisionList.as_view(), name='divisionlist'),
    url(r'^division/(?P<pk>\d+)/$', division_views.DivisionDetail.as_view(), name='divisiondetail'),
    url(r'^division/add/$', division_views.DivisionCreate.as_view(), name='division_add'),
    url(r'^division/(?P<pk>\d+)/edit/$', division_views.DivisionUpdate.as_view(), name='division_edit'),

    url(r'^dnsname/$', dnsname_views.DnsnameList.as_view(), name='dnsnamelist'),
    url(r'^dnsname/(?P<pk>\d+)/$', dnsname_views.DnsnameDetail.as_view(), name='dnsnamedetail'),
    url(r'^dnsname/add/$', dnsname_views.DnsnameCreate.as_view(), name='dnsname_add'),
    url(r'^dnsname/add_popup/$', dnsname_views.DnsnameCreatePopup.as_view(), name='dnsname_add_popup'),
    url(r'^dnsname/(?P<pk>\d+)/edit/$', dnsname_views.DnsnameUpdate.as_view(), name='dnsname_edit'),

    url(r'^domain/$', domain_views.DomainList.as_view(), name='domainlist'),
    url(r'^domain/(?P<pk>\d+)/$', domain_views.DomainDetail.as_view(), name='domaindetail'),
    url(r'^domain/add/$', domain_views.DomainCreate.as_view(), name='domain_add'),
    url(r'^domain/add_popup/$', domain_views.DomainCreatePopup.as_view(), name='domain_add_popup'),
    url(r'^domain/(?P<pk>\d+)/edit/$', domain_views.DomainUpdate.as_view(), name='domain_edit'),

    url(r'^domainuser/$', domainuser_views.DomainuserList.as_view(), name='domainuserlist'),
    url(r'^domainuser/(?P<pk>\d+)/$', domainuser_views.DomainuserDetail.as_view(), name='domainuserdetail'),
    url(r'^domainuser/add/$', domainuser_views.DomainuserCreate.as_view(), name='domainuser_add'),
    url(r'^domainuser/(?P<pk>\d+)/edit/$', domainuser_views.DomainuserUpdate.as_view(), name='domainuser_edit'),

    url(r'^entry/$', entry_views.EntryList.as_view(), name='entrylist'),
    url(r'^entry/(?P<pk>\d+)/$', entry_views.EntryDetail.as_view(), name='entrydetail'),
    url(r'^entry/add/$', entry_views.EntryCreate.as_view(), name='entry_add'),
    url(r'^entry/(?P<pk>\d+)/edit/$', entry_views.EntryUpdate.as_view(), name='entry_edit'),

    url(r'^entry/importer/api/giraf/entry/$', giraf.entry, name='entry_importer_api_giraf'),
    url(r'^entry/importer/file/markdown/entry/$', markdown.entry, name='entry_importer_file_markdown'),

    url(r'^headline/$', headline_views.HeadlineList.as_view(), name='headlinelist'),
    url(r'^headline/(?P<pk>\d+)/$', headline_views.HeadlineDetail.as_view(), name='headlinedetail'),
    url(r'^headline/add/$', headline_views.HeadlineCreate.as_view(), name='headline_add'),
    url(r'^headline/(?P<pk>\d+)/edit/$', headline_views.HeadlineUpdate.as_view(), name='headline_edit'),

    url(r'^ip/$', ip_views.IpList.as_view(), name='iplist'),
    url(r'^ip/(?P<pk>\d+)/$', ip_views.IpDetail.as_view(), name='ipdetail'),

    url(r'^location/$', location_views.LocationList.as_view(), name='locationlist'),
    url(r'^location/(?P<pk>\d+)/$', location_views.LocationDetail.as_view(), name='locationdetail'),
    url(r'^location/add/$', location_views.LocationCreate.as_view(), name='location_add'),
    url(r'^location/add_popup/$', location_views.LocationCreatePopup.as_view(), name='location_add_popup'),
    url(r'^location/(?P<pk>\d+)/edit/$', location_views.LocationUpdate.as_view(), name='location_edit'),

    url(r'^os/$', os_views.OsList.as_view(), name='oslist'),
    url(r'^os/(?P<pk>\d+)/$', os_views.OsDetail.as_view(), name='osdetail'),
    url(r'^os/add/$', os_views.OsCreate.as_view(), name='os_add'),
    url(r'^os/add_popup/$', os_views.OsCreatePopup.as_view(), name='os_add_popup'),
    url(r'^os/(?P<pk>\d+)/edit/$', os_views.OsUpdate.as_view(), name='os_edit'),

    url(r'^osimportname/$', osimportname_views.OsimportnameList.as_view(), name='osimportnamelist'),
    url(r'^osimportname/add/$', osimportname_views.OsimportnameCreate.as_view(), name='osimportname_add'),
    url(r'^osimportname/(?P<pk>\d+)/edit/$', osimportname_views.OsimportnameUpdate.as_view(), name='osimportname_edit'),

    url(r'^reason/$', reason_views.ReasonList.as_view(), name='reasonlist'),
    url(r'^reason/(?P<pk>\d+)/$', reason_views.ReasonDetail.as_view(), name='reasondetail'),
    url(r'^reason/add/$', reason_views.ReasonCreate.as_view(), name='reason_add'),
    url(r'^reason/add_popup/$', reason_views.ReasonCreatePopup.as_view(), name='reason_add_popup'),
    url(r'^reason/(?P<pk>\d+)/edit/$', reason_views.ReasonUpdate.as_view(), name='reason_edit'),

    url(r'^recommendation/$', recommendation_views.RecommendationList.as_view(), name='recommendationlist'),
    url(r'^recommendation/(?P<pk>\d+)/$', recommendation_views.RecommendationDetail.as_view(), name='recommendationdetail'),
    url(r'^recommendation/add/$', recommendation_views.RecommendationCreate.as_view(), name='recommendation_add'),
    url(r'^recommendation/add_popup/$', recommendation_views.RecommendationCreatePopup.as_view(), name='recommendation_add_popup'),
    url(r'^recommendation/(?P<pk>\d+)/edit/$', recommendation_views.RecommendationUpdate.as_view(), name='recommendation_edit'),

    url(r'^reportitem/$', reportitem_views.ReportitemList.as_view(), name='reportitemlist'),
    url(r'^reportitem/(?P<pk>\d+)/$', reportitem_views.ReportitemDetail.as_view(), name='reportitemdetail'),
    url(r'^reportitem/add/$', reportitem_views.ReportitemCreate.as_view(), name='reportitem_add'),
    url(r'^reportitem/(?P<pk>\d+)/edit/$', reportitem_views.ReportitemUpdate.as_view(), name='reportitem_edit'),

    url(r'^reportitem/importer/file/filesystem/reportitem/$', filesystem.reportitem, name='reportitem_importer_file_filesystem'),

    url(r'^serviceproviders/$', serviceprovider_views.ServiceproviderList.as_view(), name='serviceproviderlist'),
    url(r'^serviceproviders/(?P<pk>\d+)$', serviceprovider_views.ServiceproviderDetail.as_view(), name='serviceproviderdetail'),
    url(r'^serviceproviders/add/$', serviceprovider_views.ServiceproviderCreate.as_view(), name='serviceproviders_add'),
    url(r'^serviceproviders/add_popup$', serviceprovider_views.ServiceproviderCreatePopup.as_view(), name='serviceproviders_add_popup'),
    url(r'^serviceproviders/(?P<pk>\d+)/edit/$', serviceprovider_views.ServiceproviderUpdate.as_view(), name='serviceproviders_edit'),

    url(r'^systems/$', system_views.SystemList.as_view(), name='systemlist'),
    url(r'^systems/(?P<pk>\d+)$', system_views.SystemDetail.as_view(), name='systemdetail'),
    url(r'^systems/add/$', system_views.SystemCreate.as_view(), name='systems_add'),
    url(r'^systems/(?P<pk>\d+)/edit/$', system_views.SystemUpdate.as_view(), name='systems_edit'),

    url(r'^systems/creator/$', systems_creator.systems_creator, name='systems_creator'),
    url(r'^systems/exporter/markdown/domainsorted/$', domainsorted.domainsorted, name='systems_exporter_markdown_domainsorted'),
    url(r'^systems/exporter/markdown/systemsorted/$', systemsorted.systemsorted, name='systems_exporter_markdown_systemsorted'),
    url(r'^systems/exporter/spreadsheet/csv/systems/$', spreadsheet_csv.systems, name='systems_exporter_spreadsheet_csv'),
    url(r'^systems/exporter/spreadsheet/xls/systems/$', xls.systems, name='systems_exporter_spreadsheet_xls'),
    url(r'^systems/importer/api/giraf/systems/$', giraf.systems, name='systems_importer_api_giraf'),
    url(r'^systems/importer/file/csv/systems_ip/$', file_csv.systems_ip, name='systems_importer_file_csv_systems_ip'),
    url(r'^systems/importer/file/csv/systems_tags/$', file_csv.systems_tags, name='systems_importer_file_csv_systems_tags'),

    url(r'^systemstatuss/$', systemstatus_views.SystemstatusList.as_view(), name='systemstatuslist'),
    url(r'^systemstatuss/(?P<pk>\d+)$', systemstatus_views.SystemstatusDetail.as_view(), name='systemstatusdetail'),

    url(r'^systemtypes/$', systemtype_views.SystemtypeList.as_view(), name='systemtypelist'),
    url(r'^systemtypes/(?P<pk>\d+)$', systemtype_views.SystemtypeDetail.as_view(), name='systemtypedetail'),
    url(r'^systemtypes/add/$', systemtype_views.SystemtypeCreate.as_view(), name='systemtypes_add'),
    url(r'^systemtypes/add_popup$', systemtype_views.SystemtypeCreatePopup.as_view(), name='systemtypes_add_popup'),
    url(r'^systemtypes/(?P<pk>\d+)/edit/$', systemtype_views.SystemtypeUpdate.as_view(), name='systemtypes_edit'),

    url(r'^systemusers/$', systemuser_views.SystemuserList.as_view(), name='systemuserlist'),
    url(r'^systemusers/(?P<pk>\d+)$', systemuser_views.SystemuserDetail.as_view(), name='systemuserdetail'),
    url(r'^systemusers/add/$', systemuser_views.SystemuserCreate.as_view(), name='systemusers_add'),
    url(r'^systemusers/(?P<pk>\d+)/edit/$', systemuser_views.SystemuserUpdate.as_view(), name='systemusers_edit'),

    url(r'^tags/$', tag_views.TagList.as_view(), name='taglist'),
    url(r'^tags/(?P<pk>\d+)$', tag_views.TagDetail.as_view(), name='tagdetail'),
    url(r'^tags/add/$', tag_views.TagCreate.as_view(), name='tags_add'),
    url(r'^tags/(?P<pk>\d+)/edit/$', tag_views.TagUpdate.as_view(), name='tags_edit'),
    url(r'^tags/(?P<pk>\d+)/delete/$', tag_views.TagDelete.as_view(), name='tags_delete'),

    url(r'^tags/creator$', tags_creator.tags_creator, name='tags_creator'),

    url(r'^tasks/$', task_views.TaskList.as_view(), name='tasklist'),
    url(r'^tasks/closed$', task_views.TaskClosed.as_view(), name='taskclosed'),
    url(r'^tasks/(?P<pk>\d+)$', task_views.TaskDetail.as_view(), name='taskdetail'),
    url(r'^tasks/add/$', task_views.TaskCreate.as_view(), name='tasks_add'),
    url(r'^tasks/(?P<pk>\d+)/edit/$', task_views.TaskUpdate.as_view(), name='tasks_edit'),

    url(r'^tasks/(?P<pk>\d+)/start/$', task_views.TaskStart.as_view(), name='tasks_start'),
    url(r'^tasks/(?P<pk>\d+)/finish/$', task_views.TaskFinish.as_view(), name='tasks_finish'),
    url(r'^tasks/(?P<pk>\d+)/renew/$', task_views.TaskRenew.as_view(), name='tasks_renew'),
    url(r'^tasks/(?P<pk>\d+)/set_user/$', task_views.TaskSetUser.as_view(), name='tasks_set_user'),
    url(r'^tasks/(?P<pk>\d+)/unset_user/$', task_views.TaskUnsetUser.as_view(), name='tasks_unset_user'),

    url(r'^tasks/creator$', tasks_creator.tasks_creator, name='tasks_creator'),

    url(r'^tasknames/$', taskname_views.TasknameList.as_view(), name='tasknamelist'),
    url(r'^tasknames/(?P<pk>\d+)$', taskname_views.TasknameDetail.as_view(), name='tasknamedetail'),
    url(r'^tasknames/add/$', taskname_views.TasknameCreate.as_view(), name='tasknames_add'),
    url(r'^tasknames/(?P<pk>\d+)/edit/$', taskname_views.TasknameUpdate.as_view(), name='tasknames_edit'),

    url(r'^taskprioritys/$', taskpriority_views.TaskpriorityList.as_view(), name='taskprioritylist'),
    url(r'^taskprioritys/(?P<pk>\d+)$', taskpriority_views.TaskpriorityDetail.as_view(), name='taskprioritydetail'),

    url(r'^taskstatuss/$', taskstatus_views.TaskstatusList.as_view(), name='taskstatuslist'),
    url(r'^taskstatuss/(?P<pk>\d+)$', taskstatus_views.TaskstatusDetail.as_view(), name='taskstatusdetail'),

]
