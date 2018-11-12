#!/bin/bash

export APPDIR=/app
export PGPASSFILE=$APPDIR/docker/.pgpass
export PGHOST=db
export PGUSER=dfirtrack

until psql -h $PGHOST -U $PGUSER -c '\q'
do
    echo "Waiting for Postgres..."
    sleep 1
done

$APPDIR/manage.py migrate
$APPDIR/manage.py qcluster &
$APPDIR/manage.py runserver
