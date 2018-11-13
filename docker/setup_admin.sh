#!/bin/bash

docker container exec -it dfirtrack_app_1 /app/manage.py createsuperuser --noinput --user admin --email admin@test.invalid
docker container exec -it dfirtrack_app_1 /app/manage.py changepassword admin
