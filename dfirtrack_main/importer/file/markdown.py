from dateutil.parser import parse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from dfirtrack_main.forms import EntryFileImport
from dfirtrack_main.logger.default_logger import debug_logger, warning_logger
from dfirtrack_main.models import Entry
import hashlib
from io import TextIOWrapper

@login_required(login_url="/login")
def entry(request):
    """ this form parses a file and tries to get entries for a single system """

    # form was valid to post
    if request.method == "POST":

        # call logger
        debug_logger(str(request.user), " ENTRY_TXT_IMPORTER_BEGIN")

        # get text out of file (variable results from request object via file upload field)
        entryfile = TextIOWrapper(request.FILES['entryfile'].file, encoding=request.encoding)

        # set row counter (needed for logger)
        i = 0

        # iterate over rows in file
        for row in entryfile:

            # autoincrement row counter
            i += 1

            # skip first two lines # TODO: remove first two lines from parsing script
            if i == 1 or i == 2:
                continue

            # split line from markdown table format to single values
            column = row.split("|")

            # check row for empty value
            if len(column) < 6:
                warning_logger(str(request.user), " ENTRY_TXT_IMPORTER_SYSTEM_COLUMN " + "row_" + str(i) + ":empty_row")
                continue

            # get values of former markdown tables
            entry_date = column[1]
            entry_utc = column[2]
            entry_system = column[3]
            entry_type = column[4]
            entry_content = column[5]

            # remove trailing and leading whitespaces
            entry_date = entry_date.strip()
            entry_utc = entry_utc.strip()
            entry_system = entry_system.strip()
            entry_type = entry_type.strip()
            entry_content = entry_content.strip()

            # concatenate all relevant entry values to a string for hashing
            entry_string = entry_date + entry_utc + entry_system + entry_type + entry_content

            # calculate hash from entry values
            entry_hash = hashlib.sha1(entry_string.encode('utf8'))
            entry_sha1 = entry_hash.hexdigest()

            # get system_id as string from POST object
            system = request.POST['system']

            # check for existing entry_sha1 for this system and skip if it already exist
            try:
                check_entry = Entry.objects.get(system=system, entry_sha1=entry_sha1)
                warning_logger(str(request.user), " ENTRY_TXT_IMPORTER_ENTRY_EXISTS " + "row_" + str(i) + ":entry_exists")
                continue
            except:
                pass

            # convert timing information to datetime object
            entry_time = parse(entry_date + " " + entry_utc + "+00:00")

            # create form with request data
            form = EntryFileImport(request.POST, request.FILES)

            # create entry
            if form.is_valid():

                pass
                # don't save form yet
                entry = form.save(commit=False)

                # set values from file (row / column)
                entry.entry_time = entry_time 
                entry.entry_sha1 = entry_sha1
                entry.entry_date = entry_date 
                entry.entry_utc = entry_utc 
                entry.entry_system = entry_system 
                entry.entry_type = entry_type 
                entry.entry_content = entry_content 

                # set auto values
                entry.entry_created_by_user_id = request.user
                entry.entry_modified_by_user_id = request.user

                # save object
                entry.save()

                # call logger
                entry.logger(str(request.user), ' ENTRY_TXT_IMPORTER_EXECUTED')

        # call logger
        debug_logger(str(request.user), " ENTRY_TXT_IMPORTER_END")

        return redirect(reverse('system_detail', args=(system,)))

    else:
        # show empty form with preselected system
        if request.method == 'GET' and 'system' in request.GET:
            system = request.GET['system']
            form = EntryFileImport(initial={
                'system': system,
            })
        else:
            # show empty form
            form = EntryFileImport()

        # call logger
        debug_logger(str(request.user), " ENTRY_TXT_IMPORTER_ENTERED")
    return render(request, 'dfirtrack_main/entry/entry_file_importer.html', {'form': form})

