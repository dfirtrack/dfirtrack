from constance import config as constance_config
from dfirtrack_main.logger.default_logger import debug_logger, info_logger
import os
import shutil


def clean_directory(request_user):
    """ function to clean the system path within the markdown directory """

    # clean or create markdown directory
    if os.path.exists(constance_config.MARKDOWN_PATH + "/docs/systems/"):
        # remove markdown directory (recursivly)
        shutil.rmtree(constance_config.MARKDOWN_PATH + "/docs/systems/")
        # recreate markdown directory
        os.mkdir(constance_config.MARKDOWN_PATH + "/docs/systems/")
        # call logger
        debug_logger(request_user, " SYSTEM_MARKDOWN_ALL_SYSTEMS_DIRECTORY_CLEANED")
    else:
        # create markdown directory
        os.makedirs(constance_config.MARKDOWN_PATH + "/docs/systems/")
        # call logger
        info_logger(request_user, " SYSTEM_MARKDOWN_FOLDER_CREATED")
