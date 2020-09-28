#!/bin/bash

export APPDIR=/dfirtrack
export PGPASSFILE=$APPDIR/docker/.pgpass
export PGHOST=db
export PGUSER=dfirtrack

until psql -h $PGHOST -U $PGUSER -c '\q'
do
    echo "Waiting for Postgres..."
    sleep 1
done

service nginx start
$APPDIR/manage.py migrate
$APPDIR/manage.py qcluster &
gunicorn --log-file=/var/log/gunicorn.log --workers 4 --bind localhost:5000 dfirtrack.wsgi &
sleep 10
echo "Container started"
echo "!!!! You may run docker/setup_admin.sh from the host system to create a new superuser !!!!"
sleep infinity 