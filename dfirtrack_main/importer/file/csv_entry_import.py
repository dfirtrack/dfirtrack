import csv
import hashlib
from logging import debug
import os
from dfirtrack_main.logger.default_logger import info_logger, debug_logger
from dfirtrack_main.async_messages import message_user
from django.contrib.messages import constants
from django.db import IntegrityError
from dfirtrack_main.models import Case, Entry, System

def csv_entry_import_async(system_id, file_name, field_mapping, request_user, case_id=None):
    """ async timesketch csv import """

    row_count = 0
    fail_count = 0
    dup_count = 0
    
    system = System.objects.get(system_id=system_id)
    case = Case.objects.get(case_id=case_id) if case_id else None
    with open(file_name, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        
        for row in spamreader:
            if row[0] != '__ts_timeline_id':
                try:
                    row_count += 1
                    entry = Entry()
                    entry.system = system
                    entry.entry_created_by_user_id = request_user
                    entry.entry_modified_by_user_id = request_user                
                    m = hashlib.sha1()
                    entry.entry_time = row[field_mapping['entry_time']]
                    m.update(row[1].encode())                
                    entry.entry_type = row[field_mapping['entry_type']]
                    m.update(row[2].encode())
                    entry.entry_content = row[field_mapping['entry_content']]
                    m.update(row[4].encode())                       
                    entry.entry_sha1 = m.hexdigest()
                    entry.case = case
                    entry.save()
                except IntegrityError:
                    dup_count += 1
                except Exception as e:
                    debug_logger(
                        str(request_user),
                        f' ENTRY_TIMESKETCH_IMPORT'
                        f' ERROR: {e}'
                    )
                    fail_count += 1

    os.remove(file_name)
    
    if fail_count == 0 and dup_count != 0:
        message_user(
            request_user,
            f'Imported {row_count-dup_count} entries for system "{system.system_name}". Removed {dup_count} duplicates.',
            constants.SUCCESS
        )
    elif fail_count == 0:
        message_user(
            request_user,
            f'Imported {row_count} entries for system "{system.system_name}".',
            constants.SUCCESS
        )
    else: 
        message_user(
            request_user,
            f'Could not import {fail_count} of {row_count} entries for system "{system.system_name}".',
            constants.WARNING
        )

    # call logger
    info_logger(
        str(request_user),
        f' ENTRY_TIMESKETCH_IMPORT'
        f' created:{row_count}'
        f' failed:{fail_count}'
    )