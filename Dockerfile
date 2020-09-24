FROM python:3.7
WORKDIR /app
COPY . /app
RUN sed -i 's/DEBUG = False/DEBUG = True/' .dfirtrack/settings.py
RUN apt-get update && apt-get -y install postgresql-client
RUN pip install -r requirements.txt
RUN mkdir log markdown static
WORKDIR markdown
RUN mkdir -p docs/systems
RUN mkdocs new markdown
COPY docker/mkdocs.yml .
WORKDIR /app
RUN chmod 0600 docker/.pgpass
RUN ./manage.py collectstatic
EXPOSE 8000
ENTRYPOINT ./docker/run_dfirtrack.sh
