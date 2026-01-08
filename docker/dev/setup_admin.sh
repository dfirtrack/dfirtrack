#!/bin/bash

echo "Enter Superuser name:"
read superuser_name
echo "Enter Superuser email:"
read superuser_email
echo ""
docker container exec -it dev-dfirtrack-1 /dfirtrack/manage.py createsuperuser --noinput --username $superuser_name --email $superuser_email
docker container exec -it dev-dfirtrack-1 /dfirtrack/manage.py changepassword $superuser_name
