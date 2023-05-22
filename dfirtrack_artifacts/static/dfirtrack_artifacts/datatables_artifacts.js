generic_datatable = {
    "pageLength": 25,
    "lengthMenu": [[10, 25, 50, -1], [10, 25, 50, "All"]],
    "order": [[ 1, "asc" ]],
    "processing":true,
    "serverSide":true,
    "bStateSave": true,
    "columns": [
        { "data": "artifact_id" },
        { "data": "artifact_name" },
        { "data": "artifactstatus" },
        { "data": "artifactpriority" },
        { "data": "artifacttype" },
        { "data": "system" },
        { "data": "artifact_requested_time" },
        { "data": "artifact_acquisition_time" },
        { "data": "artifact_create_time" },
        { "data": "artifact_modify_time" }
    ]
}

reduced_datatable = Object.assign({},
    generic_datatable,
    {
        "columns": [
            { "data": "artifact_id" },
            { "data": "artifact_name" },
            { "data": "artifactstatus" },
            { "data": "artifactpriority" },
            { "data": "artifacttype" },
            { "data": "artifact_requested_time" },
            { "data": "artifact_acquisition_time" },
        ]
    }
)

$(document).ready( function () {

    $('#table_artifact').DataTable(Object.assign({},
        generic_datatable,
        {
            "ajax": {
                "type" : "POST",
                "url": "/filter/artifact/?artifact&status=" + ((window.location.pathname.split('/')[3]) ? window.location.pathname.split('/')[3]: "open"),
                "headers": {'X-CSRFToken': csrftoken}
            }
        }
    ));

    $('#table_artifact_details').DataTable( Object.assign({},
        generic_datatable,
        {
            "ajax": {
                "type" : "POST",
                "url": "/filter/artifact/?" + window.location.pathname.split('/')[1] + "=" + window.location.pathname.split('/')[2],
                "headers": {'X-CSRFToken': csrftoken},
                "complete":  function (json) {
                    console.log(json)
                    total = json.responseJSON.recordsTotal
                    $('#artifact_count').text("("+ total + ")")
                }
            }
        }
    ));
    $('#table_system_artifact_open').DataTable( Object.assign({},
        reduced_datatable,
        {
            "ajax": {
                "type" : "POST",
                "url": "/filter/artifact/?status=open&system=" + window.location.pathname.split('/')[2],
                "headers": {'X-CSRFToken': csrftoken}
            }
        }
    ));
    $('#table_system_artifact_closed').DataTable( Object.assign({},
        reduced_datatable,
        {
            "ajax": {
                "type" : "POST",
                "url": "/filter/artifact/?status=closed&system=" + window.location.pathname.split('/')[2],
                "headers": {'X-CSRFToken': csrftoken}
            }
        }
    ));

    $('#table_artifact_artifactstatus').DataTable( Object.assign({},
        generic_datatable,
        {
            "ajax": {
                "type" : "POST",
                "url": "/filter/artifact/?artifactstatus=" + window.location.pathname.split('/')[4],
                "headers": {'X-CSRFToken': csrftoken}
            }
        }
    ));

    $('#table_artifact_artifactpriority').DataTable( Object.assign({},
        generic_datatable,
        {
            "ajax": {
                "type" : "POST",
                "url": "/filter/artifact/?artifactpriority=" + window.location.pathname.split('/')[4],
                "headers": {'X-CSRFToken': csrftoken}
            }
        }
    ));

    $('#table_artifact_artifacttype').DataTable( Object.assign({},
        generic_datatable,
        {
            "ajax": {
                "type" : "POST",
                "url": "/filter/artifact/?artifacttype=" + window.location.pathname.split('/')[4],
                "headers": {'X-CSRFToken': csrftoken}
            }
        }
    ));
} );
