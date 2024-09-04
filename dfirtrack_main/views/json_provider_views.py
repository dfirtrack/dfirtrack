from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import ForeignKey, Q
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.templatetags.static import static
from djangoql.exceptions import DjangoQLParserError
from djangoql.queryset import apply_search

from dfirtrack_artifacts.models import Artifact, ArtifactQLSchema
from dfirtrack_config.models import MainConfigModel, UserConfigModel
from dfirtrack_config.views.assignment import AssignmentQLSchema
from dfirtrack_main.models import System, SystemQLSchema


def _filter(
    model, queryset, simple_filter_params, filter_params, request_user, dqlschema
):
    '''post request filter everything'''

    # define filter kwargs for or, and filters
    and_filter_kwargs = dict()
    or_filter_kwargs = dict()
    exclude_filter_kwargs = dict()

    # get user config filter for model list view and config views
    if (
        'config' in simple_filter_params
        or model.__name__.lower() in simple_filter_params
    ):
        # set filter view for user config model
        filter_view = simple_filter_params.get(
            'config', f'{model.__name__.lower()}_list'
        )

        # get config
        user_config, created = UserConfigModel.objects.get_or_create(
            user_config_username=request_user, filter_view=filter_view
        )

        # apply dql filter to queryset
        if user_config.filter_query:
            # filter for user query
            if filter_view == 'assignment':
                user_queryset = apply_search(
                    User.objects.all(),
                    user_config.filter_query,
                    schema=AssignmentQLSchema,
                )
                for value in model.__dict__:
                    if 'assigned_to_user_id' in value:
                        and_filter_kwargs[f'{value}__in'] = user_queryset
            else:
                queryset = apply_search(
                    queryset, user_config.filter_query, schema=dqlschema
                )
        elif filter_view == 'assignment':
            user_queryset = User.objects.all()
            for value in model.__dict__:
                if 'assigned_to_user_id' in value:
                    exclude_filter_kwargs[f'{value}__in'] = user_queryset

    # get search value
    search_value = filter_params.get('search[value]')

    # get order column number
    order_column_number = filter_params.get('order[0][column]')
    # get order column
    order_column_name = filter_params.get(f'columns[{order_column_number}][data]')
    # order direction: empty if descending (default), '-' is ascending
    order_dir = '' if filter_params.get('order[0][dir]') == 'asc' else '-'
    # check in model if field is foreign key
    if isinstance(model._meta.get_field(order_column_name), ForeignKey):
        order_column_name = f'{order_column_name}__{order_column_name}_name'

    # create search filter for every column of the model
    if search_value != '':
        # get entries from datatable data fields
        for entry in filter_params:
            if entry.endswith('[data]'):
                # an entry points to a model field
                tmp_column_name = filter_params[entry]
                # if model field is foreign key, foreign key name contains case insensitive
                if isinstance(model._meta.get_field(tmp_column_name), ForeignKey):
                    key = f'{tmp_column_name}__{tmp_column_name}_name__icontains'
                else:
                    # otherwise field contains insensitive
                    key = f'{tmp_column_name}__icontains'

                # add search filter to or kwargs "name or status or etc."
                or_filter_kwargs[key] = search_value

    # simple get filter, relevant for tag, status detail views etc.
    for filter, value in simple_filter_params.items():
        if filter in model.__dict__:
            if not isinstance(value, list):
                and_filter_kwargs[f'{filter}'] = value

    # filter queryset using Q for or_kwargs and filter and_kwargs in seconed step
    filter_results = (
        queryset.filter(Q(**or_filter_kwargs, _connector=Q.OR))
        .filter(**and_filter_kwargs)
        .exclude(**exclude_filter_kwargs)
        .distinct()
        .order_by(order_dir + order_column_name)
    )

    # starting point for records in table
    start = int(filter_params['start'])
    # how many records are to be shown? if all records are to be shown, length is set to -1
    length = (
        int(filter_params['length'])
        if int(filter_params['length']) != -1
        else len(filter_results)
    )

    return list(filter_results), start, start + length


@login_required(login_url="/login")
def filter_system(request):
    model = System
    queryset = System.objects

    if 'case' in request.GET:
        queryset = queryset.filter(case=request.GET['case'])

    if 'tag' in request.GET:
        queryset = queryset.filter(tag=request.GET['tag'])

    # build results (html code) for starting point to how many records to show
    filter_results, start, end = _filter(
        model, queryset, request.GET, request.POST, request.user, SystemQLSchema
    )
    results = list()
    for obj in filter_results:
        results.append(
            {
                "system_id": obj.system_id,
                "system_name": "<a href='"
                + obj.get_absolute_url()
                + "' type='button' class='btn btn-primary btn-sm copy-true'><img src='"
                + static("dfirtrack_main/icons/monitor-light.svg")
                + "' class='icon right-distance copy-false' alt='icon'>"
                + obj.system_name
                + "</a>",
                "systemstatus": render_to_string(
                    'dfirtrack_main/includes/button_systemstatus.html',
                    {'systemstatus': obj.systemstatus},
                ),
                "analysisstatus": (
                    "<span data-toggle='tooltip' data-placement='auto' title='"
                    + str(obj.analysisstatus.analysisstatus_note or "")
                    + "'><a href='"
                    + obj.analysisstatus.get_absolute_url()
                    + "'>"
                    + str(obj.analysisstatus)
                    + "</a></span>"
                    if obj.analysisstatus is not None
                    else "---"
                ),
                "system_create_time": obj.system_create_time.strftime("%Y-%m-%d %H:%M"),
                "system_modify_time": obj.system_modify_time.strftime("%Y-%m-%d %H:%M"),
            }
        )
    # build json dict
    json_dict = {
        'draw': request.POST.get('draw') if request.POST.get('draw') else 1,
        'recordsTotal': queryset.all().count(),
        'recordsFiltered': len(filter_results),
        'data': results[start:end],
    }
    return JsonResponse(json_dict, safe=False)


@login_required(login_url="/login")
def filter_artifacts(request):
    model = Artifact
    queryset = Artifact.objects

    # to filter for open/closed/all artifact status
    if 'status' in request.GET:
        # get main config
        main_config_model = MainConfigModel.objects.get(main_config_name='MainConfig')

        # get open artifact status
        artifactstatus_open = main_config_model.artifactstatus_open.all()

        # filter artifacts based on status
        if request.GET['status'] == 'all':
            pass
        elif request.GET['status'] == 'closed':
            # not in open status
            queryset = queryset.filter(~Q(artifactstatus__in=artifactstatus_open))
        else:
            # in open status
            queryset = queryset.filter(artifactstatus__in=artifactstatus_open)

    # filter artifacts based on case or tag for detailed case or tag view
    # correction of total count for datatables
    if 'case' in request.GET:
        queryset = queryset.filter(case=request.GET['case'])

    if 'tag' in request.GET:
        queryset = queryset.filter(tag=request.GET['tag'])

    # build results (html code) for starting point to how many records to show
    filter_results, start, end = _filter(
        model, queryset, request.GET, request.POST, request.user, ArtifactQLSchema
    )
    results = list()
    for obj in filter_results:
        results.append(
            {
                "artifact_id": obj.artifact_id,
                "artifact_name": f'<a href="{ obj.get_absolute_url()}" type="button" class="btn btn-primary btn-sm top-right copy-true">'
                + f'<img src="{ static("dfirtrack_main/icons/bug-light.svg")}" class="icon-sm right-distance copy-false" alt="icon">'
                + f'{ obj.artifact_name }</a>',
                "artifactstatus": f'<a href="{ obj.artifactstatus.get_absolute_url() }">{ obj.artifactstatus.artifactstatus_name }</a>',
                "artifactpriority": f'<a href="{ obj.artifactpriority.get_absolute_url() }">'
                + render_to_string(
                    'dfirtrack_main/includes/button_priority.html',
                    {'priority_name': obj.artifactpriority.artifactpriority_name},
                )
                + f'{ obj.artifactpriority.artifactpriority_name }</a>',
                "artifacttype": f'<a href="{ obj.artifacttype.get_absolute_url() }">{ obj.artifacttype.artifacttype_name }</a>',
                "system": f'<a href="{obj.system.get_absolute_url()}" type="button" class="btn btn-primary btn-sm copy-true"><img src="{static("dfirtrack_main/icons/monitor-light.svg")}" '
                + f'class="icon right-distance copy-false" alt="icon">{obj.system.system_name}</a>',
                "artifact_requested_time": (
                    obj.artifact_requested_time.strftime("%Y-%m-%d %H:%M")
                    if obj.artifact_requested_time
                    else '---'
                ),
                "artifact_acquisition_time": (
                    obj.artifact_acquisition_time.strftime("%Y-%m-%d %H:%M")
                    if obj.artifact_acquisition_time
                    else '---'
                ),
                "artifact_create_time": obj.artifact_create_time.strftime(
                    "%Y-%m-%d %H:%M"
                ),
                "artifact_modify_time": obj.artifact_modify_time.strftime(
                    "%Y-%m-%d %H:%M"
                ),
            }
        )

    # build json dict
    json_dict = {
        'draw': request.POST.get('draw') if request.POST.get('draw') else 1,
        'recordsTotal': queryset.all().count(),
        'recordsFiltered': len(filter_results),
        'data': results[start:end],
    }
    return JsonResponse(json_dict, safe=False)
