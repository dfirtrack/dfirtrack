from django.contrib.auth.models import User
from django.contrib.messages import constants
from dfirtrack_main.async_messages import message_users


def error_message_cron(message_text):
    """ error message for all users if function was called from 'artifact_cron' / 'system_cron' (w/o request) """

    # get all users
    all_users = User.objects.all()

    # call message for all users
    message_users(
        all_users,
        f'[Scheduled task spreadsheet exporter] {message_text}',
        constants.ERROR
    )

    # return to calling function in 'checks'
    return
