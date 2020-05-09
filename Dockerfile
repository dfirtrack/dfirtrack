FROM python:3.7
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN apt-get update && apt-get -y install postgresql-client
RUN pip install -r requirements.txt
RUN mkdir log markdown static
WORKDIR markdown
RUN mkdir -p docs/systems
RUN mkdocs new markdown
COPY docker/mkdocs.yml .
WORKDIR /app
RUN chmod 0600 docker/.pgpass
COPY docker/settings.py dfirtrack/
RUN ./manage.py collectstatic
EXPOSE 8000
ENTRYPOINT ./docker/run_dfirtrack.sh
