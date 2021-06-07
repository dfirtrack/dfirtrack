FROM python:3.8

# create dfirtrack dir, copy repo to it and install requirements - we use /dfirtrack-static to keep /dfirtrack empty for "dynamic" dir
WORKDIR /dfirtrack-static
COPY . /dfirtrack-static
RUN apt-get update && apt-get -y install postgresql-client nano nginx
RUN pip install -r requirements.txt

# create default mkdocs.yml
RUN mkdocs new markdown
RUN mkdir -p markdown/docs/systems
COPY docker/shared_files/mkdocs.yml markdown/mkdocs.yml

# copy nginx configs
RUN rm /etc/nginx/sites-enabled/default
COPY docker/shared_files/nginx.site.conf /etc/nginx/sites-available/dfirtrack
COPY docker/shared_files/nginx.site.insecure.conf /etc/nginx/sites-available/dfirtrack_insecure
RUN mkdir /etc/nginx/ssl

# create certificate for tls and modify nginx config accordingly
WORKDIR /dfirtrack-static
ARG openssl_o
ARG fqdn
ARG openssl_ou
RUN openssl req -newkey rsa:4096 -days 365 -nodes -x509 -subj "/O=$openssl_o/CN=$fqdn/OU=$openssl_ou" -keyout /etc/nginx/ssl/nginx.key -out /etc/nginx/ssl/nginx.crt
RUN sed -i "s/server_name dfirtrack_app;/server_name $fqdn;/" /etc/nginx/sites-available/dfirtrack
RUN sed -i "s/server_name dfirtrack_app;/server_name $fqdn;/" /etc/nginx/sites-available/dfirtrack_insecure

# copy dfirtrack local settings and modify fqdn, postgres user and password
ARG pgpass_pw
ARG pgpass_user
COPY docker/shared_files/local_settings.py dfirtrack/local_settings.py
RUN sed -i "s/{{ fqdn }}/$fqdn/" dfirtrack/local_settings.py
RUN sed -i "s/{{ postgresql_user }}/$pgpass_user/" dfirtrack/local_settings.py
RUN sed -i "s/{{ postgresql_user_password }}/$pgpass_pw/" dfirtrack/local_settings.py

# copy entrypoint and set disable_https flag according to .env
ARG disable_https
COPY docker/dev/entrypoint.sh docker/dev/entrypoint.sh
RUN sed -i "s/{{ postgresql_user_password }}/$pgpass_pw/" docker/dev/entrypoint.sh
RUN sed -i "s/{{ disable_https }}/$disable_https/" docker/dev/entrypoint.sh

ARG django_secret_key
RUN sed -i "s/SECRET_KEY = os.getenv('SECRET_KEY', 'CHANGEME')/SECRET_KEY = os.getenv('SECRET_KEY', '$django_secret_key')/" dfirtrack/settings.py

EXPOSE 80
EXPOSE 443
ENTRYPOINT docker/dev/entrypoint.sh