import yaml

from dfirtrack_main.logger.default_logger import warning_logger


def read_or_create_mkdocs_yml(username, mkdconfpath):

    # open mkdocs.yml for reading
    try:
        mkdconffile = open(mkdconfpath)

        # read YAML to dict
        mkdconfdict = yaml.safe_load(mkdconffile)

        # close mkdocs.yml
        mkdconffile.close()

    except FileNotFoundError:
        # call logger
        warning_logger(username, " SYSTEM_EXPORTER_MARKDOWN no mkdocs.yml found")
        # set empty dummydict for non-existing file to make code work as usual (just for the first execution because afterwards 'mkdocs.yml' will be there)
        mkdconfdict = {"pages": [{"Systems": []}]}

    return mkdconfdict
