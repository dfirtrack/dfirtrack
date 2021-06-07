# About deploying Dfirtrack as Docker Container

## How to run the DFIRTrack Docker Container

To run dfirtrack in a docker container simply execute `docker-compose up` in the /docker/dev or /docker/prod directory of this repo. **Before doing so, please check the .env file that is located in the same directory and make necessary changes.** This file is used to set internal variables, e.g. passwords and usernames. Make sure to rebuild the container (e.g. with `docker-compose up --build`) whenever there are changes in the .env file.

The container uses the local version of dfirtrack. It uses gunicorn and nginx to serve the application and a separate container for the postgres database. The database is using a docker volume to persist changes - when you want to start with a fresh database, simply delete the volume.

To be able to use the container in a cloud environment, most of the settings can also be changed with environment variables. The following list shows the available environment variables.

```
DB_NAME: dfirtrack               # name of the database
DB_USER: test                    # username of the database
DB_PASSWORD: secret              # password of the database
DB_HOST: db                      # hostname of the database
DB_PORT: 5432                    # port of the database
FQDN: dfirtrack.test             # fqdn for dfirtrack
DISABLE_HTTPS: 'false'            # 'true' to disable HTTPS
SECRET_KEY: sup3r_s3cr3t_k3y     # django secret key
```

Note: The build process of the container creates the SSL certificate with the FQDN in the `.env` file. When you change the FQDN in the environment variables, SSL requests won't work. You should only change the `FQDN` parameter, if you also want to set `DISABLE_HTTPS` to `'true'`. In production environments, the `DISABLE_HTTPS` setting should only be used behind a load balancer or another proxy which enables encryption.

## Prod vs Dev Container

Both, the `prod` as well as the `dev` container, are built upon the same fundamentals. That means the the general form of deployment (codebase, gunicorn, nginx) is the same, no matter which container you choose. The main difference between them is that, with the `dev` container you are able to modify the files in the repo on your host system and the changes will reflect immediately in the container. This is achieved by mounting the repo dir from your host as a host volume to the docker container. Since this is not really "the docker way" some tricks have to be used. These entail, for example, that all static files are collected on every startup of the container and that files created by the container might show up in your hosts repo.

In summary, the `dev` container is intended for developing purposes and not needed, unless you want to actively change the dfirtrack code. **If you just want to use dfirtrack, you should always use the `prod` container.**