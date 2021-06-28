FROM python:3.8

# create dfirtrack dir, copy repo to it and install requirements
WORKDIR /dfirtrack
COPY . /dfirtrack
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
WORKDIR /dfirtrack
ARG openssl_o=testo
ARG fqdn=localhost
ARG openssl_ou=testou
RUN openssl req -newkey rsa:4096 -days 365 -nodes -x509 -subj "/O=$openssl_o/CN=$fqdn/OU=$openssl_ou" -keyout /etc/nginx/ssl/nginx.key -out /etc/nginx/ssl/nginx.crt
RUN sed -i "s/server_name dfirtrack_app;/server_name $fqdn;/" /etc/nginx/sites-available/dfirtrack
RUN sed -i "s/server_name dfirtrack_app;/server_name $fqdn;/" /etc/nginx/sites-available/dfirtrack_insecure

# copy dfirtrack local settings
COPY docker/shared_files/local_settings.py dfirtrack/local_settings.py

# copy entrypoint
COPY docker/prod/entrypoint.sh docker/prod/entrypoint.sh

RUN ./manage.py collectstatic
EXPOSE 80
EXPOSE 443
ENTRYPOINT docker/prod/entrypoint.sh
