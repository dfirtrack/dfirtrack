from django.conf.urls import url
from dfirtrack_main.views import generic_views
from dfirtrack_main.views import analysisstatus_views, analystmemo_views, case_views, company_views, contact_views, division_views, dnsname_views, domain_views, domainuser_views, entry_views, headline_views, ip_views, location_views, os_views, osimportname_views, reason_views, recommendation_views, reportitem_views, serviceprovider_views, system_views, systemstatus_views, systemtype_views, systemuser_views, tag_views, task_views, taskname_views, taskpriority_views, taskstatus_views
from dfirtrack_main.creator import system_creator, tag_creator, task_creator
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

    url(r'^analysisstatus/$', analysisstatus_views.AnalysisstatusList.as_view(), name='analysisstatus_list'),
    url(r'^analysisstatus/(?P<pk>\d+)/$', analysisstatus_views.AnalysisstatusDetail.as_view(), name='analysisstatus_detail'),

    url(r'^analystmemo/$', analystmemo_views.AnalystmemoList.as_view(), name='analystmemo_list'),
    url(r'^analystmemo/(?P<pk>\d+)/$', analystmemo_views.AnalystmemoDetail.as_view(), name='analystmemo_detail'),
    url(r'^analystmemo/add/$', analystmemo_views.AnalystmemoCreate.as_view(), name='analystmemo_create'),
    url(r'^analystmemo/(?P<pk>\d+)/edit/$', analystmemo_views.AnalystmemoUpdate.as_view(), name='analystmemo_update'),

    url(r'^case/$', case_views.CaseList.as_view(), name='case_list'),
    url(r'^case/(?P<pk>\d+)/$', case_views.CaseDetail.as_view(), name='case_detail'),
    url(r'^case/add/$', case_views.CaseCreate.as_view(), name='case_create'),
    url(r'^case/(?P<pk>\d+)/edit/$', case_views.CaseUpdate.as_view(), name='case_update'),

    url(r'^company/$', company_views.CompanyList.as_view(), name='company_list'),
    url(r'^company/(?P<pk>\d+)/$', company_views.CompanyDetail.as_view(), name='company_detail'),
    url(r'^company/add/$', company_views.CompanyCreate.as_view(), name='company_create'),
    url(r'^company/add_popup/$', company_views.CompanyCreatePopup.as_view(), name='company_add_popup'),
    url(r'^company/(?P<pk>\d+)/edit/$', company_views.CompanyUpdate.as_view(), name='company_update'),

    url(r'^contact/$', contact_views.ContactList.as_view(), name='contact_list'),
    url(r'^contact/(?P<pk>\d+)/$', contact_views.ContactDetail.as_view(), name='contact_detail'),
    url(r'^contact/add/$', contact_views.ContactCreate.as_view(), name='contact_create'),
    url(r'^contact/add_popup/$', contact_views.ContactCreatePopup.as_view(), name='contact_add_popup'),
    url(r'^contact/(?P<pk>\d+)/edit/$', contact_views.ContactUpdate.as_view(), name='contact_update'),

    url(r'^division/$', division_views.DivisionList.as_view(), name='division_list'),
    url(r'^division/(?P<pk>\d+)/$', division_views.DivisionDetail.as_view(), name='division_detail'),
    url(r'^division/add/$', division_views.DivisionCreate.as_view(), name='division_create'),
    url(r'^division/(?P<pk>\d+)/edit/$', division_views.DivisionUpdate.as_view(), name='division_update'),

    url(r'^dnsname/$', dnsname_views.DnsnameList.as_view(), name='dnsname_list'),
    url(r'^dnsname/(?P<pk>\d+)/$', dnsname_views.DnsnameDetail.as_view(), name='dnsname_detail'),
    url(r'^dnsname/add/$', dnsname_views.DnsnameCreate.as_view(), name='dnsname_create'),
    url(r'^dnsname/add_popup/$', dnsname_views.DnsnameCreatePopup.as_view(), name='dnsname_add_popup'),
    url(r'^dnsname/(?P<pk>\d+)/edit/$', dnsname_views.DnsnameUpdate.as_view(), name='dnsname_update'),

    url(r'^domain/$', domain_views.DomainList.as_view(), name='domain_list'),
    url(r'^domain/(?P<pk>\d+)/$', domain_views.DomainDetail.as_view(), name='domain_detail'),
    url(r'^domain/add/$', domain_views.DomainCreate.as_view(), name='domain_create'),
    url(r'^domain/add_popup/$', domain_views.DomainCreatePopup.as_view(), name='domain_add_popup'),
    url(r'^domain/(?P<pk>\d+)/edit/$', domain_views.DomainUpdate.as_view(), name='domain_update'),

    url(r'^domainuser/$', domainuser_views.DomainuserList.as_view(), name='domainuser_list'),
    url(r'^domainuser/(?P<pk>\d+)/$', domainuser_views.DomainuserDetail.as_view(), name='domainuser_detail'),
    url(r'^domainuser/add/$', domainuser_views.DomainuserCreate.as_view(), name='domainuser_create'),
    url(r'^domainuser/(?P<pk>\d+)/edit/$', domainuser_views.DomainuserUpdate.as_view(), name='domainuser_update'),

    url(r'^entry/$', entry_views.EntryList.as_view(), name='entry_list'),
    url(r'^entry/(?P<pk>\d+)/$', entry_views.EntryDetail.as_view(), name='entry_detail'),
    url(r'^entry/add/$', entry_views.EntryCreate.as_view(), name='entry_create'),
    url(r'^entry/(?P<pk>\d+)/edit/$', entry_views.EntryUpdate.as_view(), name='entry_update'),

    url(r'^entry/importer/api/giraf/entry/$', giraf.entry, name='entry_importer_api_giraf'),
    url(r'^entry/importer/file/markdown/entry/$', markdown.entry, name='entry_importer_file_markdown'),

    url(r'^headline/$', headline_views.HeadlineList.as_view(), name='headline_list'),
    url(r'^headline/(?P<pk>\d+)/$', headline_views.HeadlineDetail.as_view(), name='headline_detail'),
    url(r'^headline/add/$', headline_views.HeadlineCreate.as_view(), name='headline_create'),
    url(r'^headline/(?P<pk>\d+)/edit/$', headline_views.HeadlineUpdate.as_view(), name='headline_update'),

    url(r'^ip/$', ip_views.IpList.as_view(), name='ip_list'),
    url(r'^ip/(?P<pk>\d+)/$', ip_views.IpDetail.as_view(), name='ip_detail'),

    url(r'^location/$', location_views.LocationList.as_view(), name='location_list'),
    url(r'^location/(?P<pk>\d+)/$', location_views.LocationDetail.as_view(), name='location_detail'),
    url(r'^location/add/$', location_views.LocationCreate.as_view(), name='location_create'),
    url(r'^location/add_popup/$', location_views.LocationCreatePopup.as_view(), name='location_add_popup'),
    url(r'^location/(?P<pk>\d+)/edit/$', location_views.LocationUpdate.as_view(), name='location_update'),

    url(r'^os/$', os_views.OsList.as_view(), name='os_list'),
    url(r'^os/(?P<pk>\d+)/$', os_views.OsDetail.as_view(), name='os_detail'),
    url(r'^os/add/$', os_views.OsCreate.as_view(), name='os_create'),
    url(r'^os/add_popup/$', os_views.OsCreatePopup.as_view(), name='os_add_popup'),
    url(r'^os/(?P<pk>\d+)/edit/$', os_views.OsUpdate.as_view(), name='os_update'),

    url(r'^osimportname/$', osimportname_views.OsimportnameList.as_view(), name='osimportname_list'),
    url(r'^osimportname/add/$', osimportname_views.OsimportnameCreate.as_view(), name='osimportname_create'),
    url(r'^osimportname/(?P<pk>\d+)/edit/$', osimportname_views.OsimportnameUpdate.as_view(), name='osimportname_update'),

    url(r'^reason/$', reason_views.ReasonList.as_view(), name='reason_list'),
    url(r'^reason/(?P<pk>\d+)/$', reason_views.ReasonDetail.as_view(), name='reason_detail'),
    url(r'^reason/add/$', reason_views.ReasonCreate.as_view(), name='reason_create'),
    url(r'^reason/add_popup/$', reason_views.ReasonCreatePopup.as_view(), name='reason_add_popup'),
    url(r'^reason/(?P<pk>\d+)/edit/$', reason_views.ReasonUpdate.as_view(), name='reason_update'),

    url(r'^recommendation/$', recommendation_views.RecommendationList.as_view(), name='recommendation_list'),
    url(r'^recommendation/(?P<pk>\d+)/$', recommendation_views.RecommendationDetail.as_view(), name='recommendation_detail'),
    url(r'^recommendation/add/$', recommendation_views.RecommendationCreate.as_view(), name='recommendation_create'),
    url(r'^recommendation/add_popup/$', recommendation_views.RecommendationCreatePopup.as_view(), name='recommendation_create_popup'),
    url(r'^recommendation/(?P<pk>\d+)/edit/$', recommendation_views.RecommendationUpdate.as_view(), name='recommendation_update'),

    url(r'^reportitem/$', reportitem_views.ReportitemList.as_view(), name='reportitem_list'),
    url(r'^reportitem/(?P<pk>\d+)/$', reportitem_views.ReportitemDetail.as_view(), name='reportitem_detail'),
    url(r'^reportitem/add/$', reportitem_views.ReportitemCreate.as_view(), name='reportitem_create'),
    url(r'^reportitem/(?P<pk>\d+)/edit/$', reportitem_views.ReportitemUpdate.as_view(), name='reportitem_update'),

    url(r'^reportitem/importer/file/filesystem/reportitem/$', filesystem.reportitem, name='reportitem_importer_file_filesystem'),

    url(r'^serviceprovider/$', serviceprovider_views.ServiceproviderList.as_view(), name='serviceprovider_list'),
    url(r'^serviceprovider/(?P<pk>\d+)/$', serviceprovider_views.ServiceproviderDetail.as_view(), name='serviceprovider_detail'),
    url(r'^serviceprovider/add/$', serviceprovider_views.ServiceproviderCreate.as_view(), name='serviceprovider_create'),
    url(r'^serviceprovider/add_popup/$', serviceprovider_views.ServiceproviderCreatePopup.as_view(), name='serviceprovider_add_popup'),
    url(r'^serviceprovider/(?P<pk>\d+)/edit/$', serviceprovider_views.ServiceproviderUpdate.as_view(), name='serviceprovider_update'),

    url(r'^system/$', system_views.SystemList.as_view(), name='system_list'),
    url(r'^system/(?P<pk>\d+)/$', system_views.SystemDetail.as_view(), name='system_detail'),
    url(r'^system/add/$', system_views.SystemCreate.as_view(), name='system_create'),
    url(r'^system/(?P<pk>\d+)/edit/$', system_views.SystemUpdate.as_view(), name='system_update'),

    url(r'^system/creator/$', system_creator.system_creator, name='system_creator'),
    url(r'^system/exporter/markdown/domainsorted/$', domainsorted.domainsorted, name='system_exporter_markdown_domainsorted'),
    url(r'^system/exporter/markdown/systemsorted/$', systemsorted.systemsorted, name='system_exporter_markdown_systemorted'),
    url(r'^system/exporter/spreadsheet/csv/system/$', spreadsheet_csv.system, name='system_exporter_spreadsheet_csv'),
    url(r'^system/exporter/spreadsheet/xls/system/$', xls.system, name='system_exporter_spreadsheet_xls'),
    url(r'^system/importer/api/giraf/system/$', giraf.system, name='system_importer_api_giraf'),
    url(r'^system/importer/file/csv/system_ip/$', file_csv.system_ip, name='system_importer_file_csv_system_ip'),
    url(r'^system/importer/file/csv/system_tag/$', file_csv.system_tag, name='system_importer_file_csv_system_tag'),

    url(r'^systemstatus/$', systemstatus_views.SystemstatusList.as_view(), name='systemstatus_list'),
    url(r'^systemstatus/(?P<pk>\d+)/$', systemstatus_views.SystemstatusDetail.as_view(), name='systemstatus_detail'),

    url(r'^systemtype/$', systemtype_views.SystemtypeList.as_view(), name='systemtype_list'),
    url(r'^systemtype/(?P<pk>\d+)/$', systemtype_views.SystemtypeDetail.as_view(), name='systemtype_detail'),
    url(r'^systemtype/add/$', systemtype_views.SystemtypeCreate.as_view(), name='systemtype_create'),
    url(r'^systemtype/add_popup/$', systemtype_views.SystemtypeCreatePopup.as_view(), name='systemtype_add_popup'),
    url(r'^systemtype/(?P<pk>\d+)/edit/$', systemtype_views.SystemtypeUpdate.as_view(), name='systemtype_update'),

    url(r'^systemuser/$', systemuser_views.SystemuserList.as_view(), name='systemuser_list'),
    url(r'^systemuser/(?P<pk>\d+)/$', systemuser_views.SystemuserDetail.as_view(), name='systemuser_detail'),
    url(r'^systemuser/add/$', systemuser_views.SystemuserCreate.as_view(), name='systemuser_create'),
    url(r'^systemuser/(?P<pk>\d+)/edit/$', systemuser_views.SystemuserUpdate.as_view(), name='systemuser_update'),

    url(r'^tag/$', tag_views.TagList.as_view(), name='tag_list'),
    url(r'^tag/(?P<pk>\d+)/$', tag_views.TagDetail.as_view(), name='tag_detail'),
    url(r'^tag/add/$', tag_views.TagCreate.as_view(), name='tag_create'),
    url(r'^tag/(?P<pk>\d+)/edit/$', tag_views.TagUpdate.as_view(), name='tag_update'),
    url(r'^tag/(?P<pk>\d+)/delete/$', tag_views.TagDelete.as_view(), name='tag_delete'),

    url(r'^tag/creator/$', tag_creator.tag_creator, name='tag_creator'),

    url(r'^task/$', task_views.TaskList.as_view(), name='task_list'),
    url(r'^task/closed/$', task_views.TaskClosed.as_view(), name='task_closed'),
    url(r'^task/(?P<pk>\d+)/$', task_views.TaskDetail.as_view(), name='task_detail'),
    url(r'^task/add/$', task_views.TaskCreate.as_view(), name='task_create'),
    url(r'^task/(?P<pk>\d+)/edit/$', task_views.TaskUpdate.as_view(), name='task_update'),

    url(r'^task/(?P<pk>\d+)/start/$', task_views.TaskStart.as_view(), name='task_start'),
    url(r'^task/(?P<pk>\d+)/finish/$', task_views.TaskFinish.as_view(), name='task_finish'),
    url(r'^task/(?P<pk>\d+)/renew/$', task_views.TaskRenew.as_view(), name='task_renew'),
    url(r'^task/(?P<pk>\d+)/set_user/$', task_views.TaskSetUser.as_view(), name='task_set_user'),
    url(r'^task/(?P<pk>\d+)/unset_user/$', task_views.TaskUnsetUser.as_view(), name='task_unset_user'),

    url(r'^task/creator/$', task_creator.task_creator, name='task_creator'),

    url(r'^taskname/$', taskname_views.TasknameList.as_view(), name='taskname_list'),
    url(r'^taskname/(?P<pk>\d+)/$', taskname_views.TasknameDetail.as_view(), name='taskname_detail'),
    url(r'^taskname/add/$', taskname_views.TasknameCreate.as_view(), name='taskname_create'),
    url(r'^taskname/(?P<pk>\d+)/edit/$', taskname_views.TasknameUpdate.as_view(), name='taskname_update'),

    url(r'^taskpriority/$', taskpriority_views.TaskpriorityList.as_view(), name='taskpriority_list'),
    url(r'^taskpriority/(?P<pk>\d+)/$', taskpriority_views.TaskpriorityDetail.as_view(), name='taskpriority_detail'),

    url(r'^taskstatus/$', taskstatus_views.TaskstatusList.as_view(), name='taskstatus_list'),
    url(r'^taskstatus/(?P<pk>\d+)/$', taskstatus_views.TaskstatusDetail.as_view(), name='taskstatus_detail'),

]
