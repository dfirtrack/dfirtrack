# How to run the Dfirtrack Docker Container

To run dfirtrack in a docker container simply execute `docker-compose up` in the root directory of this repository. Before doing so, please check the .env file that is located in the same directory and make necessary changes. This file is used to set internal variables, e.g. passwords and usernames. Make sure to rebuild the container (e.g. with `docker-compose up --build`) whenever there are changes in the .env file.

The container uses the local version of dfirtrack. It uses gunicorn and nginx to serve the application and a separate container for the postgres database. Thus, the docker container can be used for development as well as for production purposes.

