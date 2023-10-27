<div>
    <p align="center">
        <img src="dfirtrack_main/static/dfirtrack_main/img/dfirtrack_logo.png" width="600">
    </p>
</div>

<div>
    <p align="center">
        <a href><img src="https://github.com/stuhli/dfirtrack/workflows/Django%20Tests/badge.svg?branch=master" alt="Test badge"></a>
        <a href="https://codecov.io/gh/dfirtrack/dfirtrack" target="_blank"><img src="https://codecov.io/gh/dfirtrack/dfirtrack/branch/master/graph/badge.svg" alt="Codecov coverage"></a>
    </p>
</div>

<div>
    <p align="center">
        <a href><img src="https://github.com/dfirtrack/dfirtrack/workflows/Lint%20Python/badge.svg?branch=master" alt="Test badge"></a>
        <a href><img src="https://github.com/dfirtrack/dfirtrack/workflows/Lint%20Ansible/badge.svg?branch=master" alt="Test badge"></a>
        <a href><img src="https://github.com/dfirtrack/dfirtrack/workflows/Docker%20publish/badge.svg?branch=master" alt="Test badge"></a>
    </p>
</div>

DFIRTrack (Digital Forensics and Incident Response Tracking application) is an open source web application mainly based on [Django](https://www.djangoproject.com/) using a [PostgreSQL](https://www.postgresql.org/) database back end.

In contrast to other great incident response tools, which are mainly case-based and support the work of CERTs, SOCs etc. in their daily business, DFIRTrack is focused on handling one or more major incidents with a lot of affected systems as it is often observed in APT cases.
It is meant to be used as a tool for dedicated incident response teams in large cases.
So, of course, CERTs and SOCs may use DFIRTrack as well, but they may feel it will be more appropriate in special cases instead of every day work.

In contrast to case-based applications, DFIRTrack rather works in a system-based fashion.
It keeps track of the status of various systems and the tasks and forensic artifacts associated with them, keeping the analyst well-informed about the status and number of affected systems at any time during the investigation phase up to the remediation phase of the incident response process.

The [main entities](https://github.com/dfirtrack/dfirtrack/wiki/Data-model) for incident tracking are:

* systems
* artifacts
* tasks
* cases
* tags
* notes and reportitems

![Systems list view](screenshots/systems_list.png)

## Features

One focus is the fast and reliable import and export of systems and associated information.
The goal for importing systems is to provide a fast and error-free procedure.
Moreover, the goal for exporting systems and their status is to have multiple instances of documentation: for instance, detailed Markdown reports for technical staff vs. spreadsheets for non-technical audiences without redundancies and deviations in the data sets.

The following functions are implemented for now:

* Importer
    * [Creator](https://github.com/dfirtrack/dfirtrack/wiki/Import-data#system-creator) (fast creation of multiple related instances via web interface) for systems and associated tasks and tags,
    * [CSV](https://github.com/dfirtrack/dfirtrack/wiki/Import-data#system-file-importer-csv) (modifiable CSV based import, should fit for the export capabilities of many tools).
* Exporter
    * [Markdown](https://github.com/dfirtrack/dfirtrack/wiki/Export-data#system-markdown-exporter) for so-called system reports (for use in a [MkDocs](https://www.mkdocs.org/) structure),
    * Spreadsheet for systems ([CSV](https://github.com/dfirtrack/dfirtrack/wiki/Export-data#system-spreadsheet-exporter-csv) and [XLS](https://github.com/dfirtrack/dfirtrack/wiki/Export-data#system-spreadsheet-exporter-xls)) and artifacts ([XLS](https://github.com/dfirtrack/dfirtrack/wiki/Export-data#artifact-spreadsheet-exporter-xls)).
* [Modificator](https://github.com/dfirtrack/dfirtrack/wiki/Modify-data#modificator)
    * quick change of status of systems.
* [Workflows](https://github.com/dfirtrack/dfirtrack/wiki/Modify-data#workflow)
    * fast automatic generation for tasks and artifacts to one or more systems

## Installation

DFIRTrack is developed for deploying on **Ubuntu**.
Other distributions may work as well but are not tested and are not supported.

For fast and uncomplicated installation on a dedicated server including all dependencies an [Ansible](https://docs.ansible.com/ansible/latest/) playbook and role were written (available in `ansible/`).
For information about deployment with Ansible look at the [Wiki - Ansible](https://github.com/stuhli/dfirtrack/wiki/Ansible).

For development and production two docker environments were prepared as well as pre-build docker images on [docker hub](https://hub.docker.com/r/dfirtrack/dfirtrack) (see [Wiki - Docker](https://github.com/stuhli/dfirtrack/wiki/Docker)).

For installation with your own setup or for quick testing look at the [Wiki - Installation](https://github.com/stuhli/dfirtrack/wiki/Installation).

## Built-in software

The application was created by implementing the following libraries and code:

* [Bootstrap](https://github.com/twbs/bootstrap)
* [clipboard.js](https://github.com/zenorocha/clipboard.js)
* [DataTables](https://github.com/DataTables/DataTables)
* [jQuery](https://github.com/jquery/jquery)
* [Open Iconic](https://github.com/iconic/open-iconic)
* [django-async-messages](https://github.com/codeinthehole/django-async-messages)
* [swagger-ui](https://github.com/swagger-api/swagger-ui)

## Development

There are two main branches:

* `master` ![Django Tests](https://github.com/stuhli/dfirtrack/workflows/Django%20Tests/badge.svg?branch=master)
* `develop` ![Django Tests](https://github.com/stuhli/dfirtrack/workflows/Django%20Tests/badge.svg?branch=develop)

The master branch is stable and reflects major version releases.
New features and changes are added to the develop branch and merged into master after extensive testing.
Everything merged into develop should run stable too but might need manual changes.
To use the current features, please try an installation of develop.

## API

DFIRTrack uses the OpenAPI specification that is provided by the [Django REST framework](https://www.django-rest-framework.org/).
To retrieve the current OpenAPI scheme just visit the the DFIRTrack URL `https://<DFIRTRACKHOST>/api/openapi/`.

If you want to use the DFIRTrack API you can use the following API clients:

* **Python**
    * [Github: dfirtrack/dfirtrack-api-python-client](https://github.com/dfirtrack/dfirtrack-api-python-client)
    * [Github: Python minimalistic API example](https://github.com/dfirtrack/dfirtrack-python-api-example)
* **GO**
    * [Github: dfirtrack/dfirtrackapi](https://github.com/dfirtrack/dfirtrackapi)

## License

See `LICENSE` file in the root directory.

## Disclaimer

Even if some basic error checking is implemented, as of now the usage of DFIRTrack mainly depends on proper handling.

*DFIRTrack was not and most likely will never be intended for usage on publicly available servers. Nevertheless some basic security features were implemented (in particular in connection with the corresponding ansible role) always install DFIRTrack in a secured environment (e. g. a dedicated virtual machine or in a separated network)!*
