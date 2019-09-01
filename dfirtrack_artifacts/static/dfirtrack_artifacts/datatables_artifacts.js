$(document).ready( function () {
    $('#table_artifact').DataTable( {
        "pageLength": 25,
        "lengthMenu": [[10, 25, 50, -1], [10, 25, 50, "All"]],
        "order": [[ 1, "asc" ]]
    } );
} );
