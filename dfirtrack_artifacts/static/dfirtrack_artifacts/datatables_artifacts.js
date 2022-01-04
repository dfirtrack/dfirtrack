$(document).ready( function () {
    $('#table_artifact').DataTable( {
        "pageLength": 25,
        "lengthMenu": [[10, 25, 50, -1], [10, 25, 50, "All"]],
        "order": [[ 1, "asc" ]]
    } );
    $('#table_system_artifact_open').DataTable( {
        "pageLength": 10,
        "lengthMenu": [[10, 25, 50, -1], [10, 25, 50, "All"]],
        "order": [[ 1, "asc" ]]
    } );
    $('#table_system_artifact_closed').DataTable( {
        "pageLength": 10,
        "lengthMenu": [[10, 25, 50, -1], [10, 25, 50, "All"]],
        "order": [[ 1, "asc" ]]
    } );
} );
