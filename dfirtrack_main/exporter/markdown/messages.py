from django.contrib import messages
from django.contrib.messages import constants
from dfirtrack_main.async_messages import message_user


def start_message(request, sorted_text):
    """ export started """

    # create message text depending on sorting
    message_text = f'System exporter markdown (sorted by {sorted_text}) started'

    # call sync message for single user
    messages.success(request, message_text)

    # return to calling function in '...sorted'
    return

def end_message(request_user, sorted_text):
    """ export finished """

    # create message text depending on sorting
    message_text = f'System exporter markdown (sorted by {sorted_text}) finished'

    # call async message for single user
    message_user(
        request_user,
        message_text,
        constants.SUCCESS,
    )

    # return to calling function in '...sorted'
    return
