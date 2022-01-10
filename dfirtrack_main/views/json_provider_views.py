from django.contrib.auth.decorators import login_required
from django.db.models import ForeignKey
from django.http import JsonResponse
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.templatetags.static import static
from django.urls import reverse

from dfirtrack_config.models import UserConfigModel
from dfirtrack_main.models import Case, System, Tag


def get_filter_user_settings(request):
    """get filter values for all referrers from config"""

    # get config
    user_config, created = UserConfigModel.objects.get_or_create(
        user_config_username=request.user
    )

    # add below: new filter values

    '''system list'''

    # case filter
    if user_config.filter_system_list_case:
        # get filter values from config
        system_list_case = Case.objects.get(
            case_id=user_config.filter_system_list_case.case_id
        )
    else:
        system_list_case = None

    # tag filter
    if user_config.filter_system_list_tag:
        # get filter values from config
        system_list_tag = Tag.objects.get(
            tag_id=user_config.filter_system_list_tag.tag_id
        )
    else:
        system_list_tag = None

    '''assignment view'''

    # case filter
    if user_config.filter_assignment_view_case:
        # get filter values from config
        assignment_view_case = Case.objects.get(
            case_id=user_config.filter_assignment_view_case.case_id
        )
    else:
        assignment_view_case = None

    # tag filter
    if user_config.filter_assignment_view_tag:
        # get filter values from config
        assignment_view_tag = Tag.objects.get(
            tag_id=user_config.filter_assignment_view_tag.tag_id
        )
    else:
        assignment_view_tag = None

    # user filter
    if user_config.filter_assignment_view_user:
        # get filter values from config
        assignment_view_user = user_config.filter_assignment_view_user
    else:
        assignment_view_user = None

    return (
        system_list_case,
        system_list_tag,
        assignment_view_case,
        assignment_view_tag,
        assignment_view_user,
    )


def clean_user_config(request):
    """TODO: deprecated according to ticket 13"""

    # get config
    user_config, created = UserConfigModel.objects.get_or_create(
        user_config_username=request.user
    )

    if not user_config.filter_system_list_keep:
        # unset filter case
        user_config.filter_system_list_case = None
        # unset filter tag
        user_config.filter_system_list_tag = None
        # save config
        user_config.save()


@login_required(login_url="/login")
def get_systems_json(request):
    """function to create system query used by datatable JSON"""

    # get referrer
    try:
        referrer = request.headers['referer']
    # if '/system/json/' was called directly for some reason
    except KeyError:
        # call 'system_list' properly to refresh this call
        return redirect(reverse('system_list'))

    # get parameters from GET request and parse them accordingly
    get_params = request.GET
    order_column_number = get_params['order[0][column]']
    order_column_name = get_params['columns[' + order_column_number + '][data]']
    # need to modify order_column_name to order by correct field!
    if order_column_name == "analysisstatus":
        order_column_name = "analysisstatus__analysisstatus_name"
    elif order_column_name == "systemstatus":
        order_column_name = "systemstatus__systemstatus_name"
    # order direction: empty if descending (default), '-' is ascending
    order_dir = '' if (get_params['order[0][dir]'] == 'asc') else '-'
    # search value entered by user
    search_value = get_params['search[value]']
    # check that string contains only alphanumerical chars or spaces (or '_','-',':')
    if not all(
        (x.isalnum() or x.isspace() or x == '_' or x == '-' or x == ':')
        for x in search_value
    ):
        search_value = ''

    # start with empty query
    system_values = System.objects.none()

    # to keep the search dynamic and not hardcode the fields, we go through all columns as they are found in the request here
    for entry in get_params:
        # this matches on these lines: ''' columns[0][data]': ['system_id/system_name/...'] '''
        if '][data]' in entry:
            tmp_column_name = get_params[entry]
            # we start with an empty queryset and add all systems that have a match in one of their relevant fields
            # filter_kwargs is necessary for dynamic filter design
            # if filter_kwargs is empty, all entries will be returned
            if search_value != "":
                if isinstance(System._meta.get_field(tmp_column_name), ForeignKey):
                    filter_kwargs = {
                        tmp_column_name
                        + '__'
                        + tmp_column_name
                        + '_name'
                        + '__icontains': search_value
                    }
                else:
                    filter_kwargs = {tmp_column_name + '__icontains': search_value}
            else:
                filter_kwargs = {}
            # check referrer to show only relevant systems if we are not on /system/
            # analysisstatus detail
            if '/analysisstatus/' in referrer:
                analysisstatus_id = referrer.split("/")[-2]
                filter_kwargs["analysisstatus__analysisstatus_id"] = analysisstatus_id
            # systemstatus detail
            elif '/systemstatus/' in referrer:
                systemstatus_id = referrer.split("/")[-2]
                filter_kwargs["systemstatus__systemstatus_id"] = systemstatus_id
            # case detail
            elif '/case/' in referrer:
                case_id = referrer.split("/")[-2]
                filter_kwargs["case__case_id"] = case_id
            # tag detail
            elif '/tag/' in referrer:
                tag_id = referrer.split("/")[-2]
                filter_kwargs["tag__tag_id"] = tag_id
            # apply search filter
            system_values = system_values | System.objects.filter(**filter_kwargs)

    # get filter values from user config
    (
        system_list_case,
        system_list_tag,
        assignment_view_case,
        assignment_view_tag,
        assignment_view_user,
    ) = get_filter_user_settings(request)

    # add below: new referrers and apply filter values

    # add optional filtering from user_settings
    # system list
    if '/system/' in referrer:
        if system_list_case:
            system_values = system_values.filter(case=system_list_case)
        if system_list_tag:
            system_values = system_values.filter(tag=system_list_tag)
    # assignment view
    elif '/assignment/' in referrer:
        if assignment_view_case:
            system_values = system_values.filter(case=assignment_view_case)
        if assignment_view_tag:
            system_values = system_values.filter(tag=assignment_view_tag)
        if assignment_view_user:
            system_values = system_values.filter(
                system_assigned_to_user_id=assignment_view_user
            )
        else:
            system_values = system_values.filter(system_assigned_to_user_id=None)

    # make the resulting queryset unique and sort it according to user settings
    system_values = system_values.distinct().order_by(order_dir + order_column_name)

    # starting point for records in table
    start = int(get_params['start'])
    # how many records are to be shown? if all records are to be shown, length is set to -1
    length = (
        int(get_params['length'])
        if int(get_params['length']) != -1
        else len(system_values)
    )

    # if there is a search value check that the search value really occurs in one of the visible fields in the table (it is possible that the value only occurs e.g. only in the milliseconds of the data field)
    if search_value != '':
        for i in system_values:
            # extract values from system object
            system_id = i.system_id
            system_name = i.system_name
            systemstatus = i.systemstatus
            analysisstatus = i.analysisstatus
            system_create_time = i.system_create_time.strftime("%Y-%m-%d %H:%M")
            system_modify_time = i.system_modify_time.strftime("%Y-%m-%d %H:%M")

            search_relevant_strings = [
                str(system_id),
                str(system_name),
                str(systemstatus),
                str(analysisstatus),
                str(system_create_time),
                str(system_modify_time),
            ]
            really_contains_search_string = False
            # go through visible fields and check if search string is contained
            for field in search_relevant_strings:
                if search_value in field:
                    really_contains_search_string = True
            # if the searched string was not found, exclude system from queryset
            if not really_contains_search_string:
                system_values = system_values.exclude(system_id=system_id)

    # all matching systems count for metadata display
    system_count = len(system_values)
    # construct the final list with systems that are presented to user
    visible_system_list = []
    for i in system_values[start : (start + length)]:
        # construct the data to be presented in the system table
        visible_system_list.append(
            {
                "system_id": i.system_id,
                "system_name": "<a href='"
                + i.get_absolute_url()
                + "' type='button' class='btn btn-primary btn-sm copy-true'><img src='"
                + static("dfirtrack_main/icons/monitor-light.svg")
                + "' class='icon right-distance copy-false' alt='icon'>"
                + i.system_name
                + "</a>",
                "systemstatus": render_to_string(
                    'dfirtrack_main/includes/button_systemstatus.html',
                    {'systemstatus': i.systemstatus},
                ),
                "analysisstatus": "<span data-toggle='tooltip' data-placement='auto' title='"
                + str(i.analysisstatus.analysisstatus_note or "")
                + "'><a href='"
                + i.analysisstatus.get_absolute_url()
                + "'>"
                + str(i.analysisstatus)
                + "</a></span>"
                if i.analysisstatus is not None
                else "---",
                "system_create_time": i.system_create_time.strftime("%Y-%m-%d %H:%M"),
                "system_modify_time": i.system_modify_time.strftime("%Y-%m-%d %H:%M"),
            }
        )

    # prepare dictionary with relevant data to convert to json
    json_dict = {}
    json_dict['draw'] = int(get_params['draw'])
    json_dict['recordsTotal'] = len(System.objects.all())
    json_dict['recordsFiltered'] = system_count
    json_dict['data'] = visible_system_list

    # filter: clean filtering after providing filter results if persistence option was not selected
    # TODO: deprecated according to ticket 13
    clean_user_config(request)

    # convert dict with data to jsonresponse
    response = JsonResponse(json_dict, safe=False)

    return response
