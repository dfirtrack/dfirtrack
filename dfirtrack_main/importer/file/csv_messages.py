from django.contrib import messages

def final_messages(request, systems_created_counter, systems_updated_counter, systems_skipped_counter):

    # call final messages
    if systems_created_counter > 0:
        if systems_created_counter  == 1:
            messages.success(request, str(systems_created_counter) + ' system was created.')
        else:
            messages.success(request, str(systems_created_counter) + ' systems were created.')
    if systems_updated_counter > 0:
        if systems_updated_counter  == 1:
            messages.success(request, str(systems_updated_counter) + ' system was updated.')
        else:
            messages.success(request, str(systems_updated_counter) + ' systems were updated.')
    if systems_skipped_counter > 0:
        if systems_skipped_counter  == 1:
            messages.warning(request, str(systems_skipped_counter) + ' system was skipped.')
        else:
            messages.warning(request, str(systems_skipped_counter) + ' systems were skipped.')
