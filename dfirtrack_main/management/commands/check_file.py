import csv
import os


def check_file(self, importfile, delimiter, quotechar):

    '''file system checks'''

    # file does not exist (has to be checked before the other checks)
    if not os.path.isfile(importfile):
        # write message to stdout
        self.stdout.write(self.style.ERROR(f'File "{importfile}" does not exist.'))
        # return (file does not exist)
        return None

    # file is empty
    if os.stat(importfile).st_size == 0:
        # write message to stdout
        self.stdout.write(self.style.ERROR(f'File "{importfile}" is empty.'))
        # return (file is empty)
        return None

    # no read permission
    if not os.access(importfile, os.R_OK):
        # write message to stdout
        self.stdout.write(
            self.style.ERROR(f'No read permission for file "{importfile}".')
        )
        # return (no read permission))
        return None

    # try to open file
    try:
        # open file
        importcsv = open(importfile)

    # file does not exist
    except FileNotFoundError:
        # write message to stdout
        self.stdout.write(self.style.ERROR(f'File "{importfile}" does not exist.'))
        # return (file does not exist)
        return None

    '''file type checks'''

    # read rows out of csv
    rows = csv.reader(importcsv, delimiter=delimiter, quotechar=quotechar)

    try:
        # try to iterate over rows
        for row in rows:
            # do nothing
            pass

    # wrong file type
    except (UnicodeDecodeError, csv.Error):

        # write message to stdout
        self.stdout.write(
            self.style.ERROR(
                f'File "{importfile}" does not seem to be a valid CSV file.'
            )
        )
        # close file
        importcsv.close()
        # return (wrong file type)
        return

    # jump to begin of file again after iterating in file check
    importcsv.seek(0)

    # return file handle
    return importcsv
