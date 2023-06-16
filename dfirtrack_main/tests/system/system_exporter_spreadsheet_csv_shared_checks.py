import csv

from dfirtrack_main.models import System


def system_exporter_spreadsheet_csv_complete_spreadsheet_check(
    self, csv_decoded, mocktime, csv_user, is_interactive=False
):
    """test for complete spreadsheet content"""

    """ get file section """

    # open systemlist as csv object
    csv_reader = csv.reader(csv_decoded, delimiter=',')

    """ prepare objects section """

    # get objects
    system_1 = System.objects.get(system_name='system_1_all_attributes')
    system_2 = System.objects.get(system_name='system_2_no_attributes')

    """ compare values section """

    # check only for interactive CSV download
    if is_interactive:
        # compare number of rows
        self.assertEqual(
            len(csv_decoded), 7
        )  # last linebreak leads to additional line because of split

    # TODO: there must be a more convenient way to random access csv cells directly than iterating over lines and switch for line numbers
    # TODO: like with 'xlrd' for xls files for example

    # set counter
    i = 1
    # compare lines
    for csv_line in csv_reader:
        if csv_line:
            if i == 1:
                self.assertEqual(csv_line[0], 'ID')
                self.assertEqual(csv_line[1], 'System')
                self.assertEqual(csv_line[2], 'DNS name')
                self.assertEqual(csv_line[3], 'Domain')
                self.assertEqual(csv_line[4], 'Systemstatus')
                self.assertEqual(csv_line[5], 'Analysisstatus')
                self.assertEqual(csv_line[6], 'Reason')
                self.assertEqual(csv_line[7], 'Recommendation')
                self.assertEqual(csv_line[8], 'Systemtype')
                self.assertEqual(csv_line[9], 'IPs')
                self.assertEqual(csv_line[10], 'OS')
                self.assertEqual(csv_line[11], 'Companies')
                self.assertEqual(csv_line[12], 'Location')
                self.assertEqual(csv_line[13], 'Serviceprovider')
                self.assertEqual(csv_line[14], 'Tags')
                self.assertEqual(csv_line[15], 'Cases')
                self.assertEqual(csv_line[16], 'Assigned to')
                self.assertEqual(csv_line[17], 'Created')
                self.assertEqual(csv_line[18], 'Created by')
                self.assertEqual(csv_line[19], 'Modified')
                self.assertEqual(csv_line[20], 'Modified by')
            elif i == 2:
                self.assertEqual(csv_line[0], str(system_1.system_id))
                self.assertEqual(csv_line[1], 'system_1_all_attributes')
                self.assertEqual(csv_line[2], 'dnsname_1')
                self.assertEqual(csv_line[3], 'domain_1')
                self.assertEqual(csv_line[4], 'systemstatus_1')
                self.assertEqual(csv_line[5], 'analysisstatus_1')
                self.assertEqual(csv_line[6], 'reason_1')
                self.assertEqual(csv_line[7], 'recommendation_1')
                self.assertEqual(csv_line[8], 'systemtype_1')
                self.assertEqual(csv_line[9], '127.0.0.1 127.0.0.2 127.0.0.3')
                self.assertEqual(csv_line[10], 'os_1')
                self.assertEqual(csv_line[11], 'company_1 company_2 company_3')
                self.assertEqual(csv_line[12], 'location_1')
                self.assertEqual(csv_line[13], 'serviceprovider_1')
                self.assertEqual(csv_line[14], 'tag_1 tag_2 tag_3')
                self.assertEqual(csv_line[15], 'case_1 case_2 case_3')
                self.assertEqual(
                    csv_line[16], 'testuser_system_exporter_spreadsheet_csv'
                )
                self.assertEqual(csv_line[17], '2011-12-13 14:15')
                self.assertEqual(
                    csv_line[18], 'testuser_system_exporter_spreadsheet_csv'
                )
                self.assertEqual(csv_line[19], '2011-12-13 14:15')
                self.assertEqual(
                    csv_line[20], 'testuser_system_exporter_spreadsheet_csv'
                )
            elif i == 3:
                self.assertEqual(csv_line[0], str(system_2.system_id))
                self.assertEqual(csv_line[1], 'system_2_no_attributes')
                self.assertEqual(csv_line[2], '')
                self.assertEqual(csv_line[3], '')
                self.assertEqual(csv_line[4], 'systemstatus_1')
                self.assertEqual(csv_line[5], '')
                self.assertEqual(csv_line[6], '')
                self.assertEqual(csv_line[7], '')
                self.assertEqual(csv_line[8], '')
                self.assertEqual(csv_line[9], '')
                self.assertEqual(csv_line[10], '')
                self.assertEqual(csv_line[11], '')
                self.assertEqual(csv_line[12], '')
                self.assertEqual(csv_line[13], '')
                self.assertEqual(csv_line[14], '')
                self.assertEqual(csv_line[15], '')
                self.assertEqual(csv_line[16], '')
                self.assertEqual(csv_line[17], '2009-08-17 16:15')
                self.assertEqual(
                    csv_line[18], 'testuser_system_exporter_spreadsheet_csv'
                )
                self.assertEqual(csv_line[19], '2009-08-17 16:15')
                self.assertEqual(
                    csv_line[20], 'testuser_system_exporter_spreadsheet_csv'
                )
            elif i == 5:
                self.assertEqual(csv_line[0], 'Created:')
                self.assertEqual(csv_line[1], mocktime.strftime('%Y-%m-%d %H:%M'))
            elif i == 6:
                self.assertEqual(csv_line[0], 'Created by:')
                self.assertEqual(csv_line[1], csv_user)
        # increase counter
        i += 1

    # compare number of rows (needs to be at the end because 'line_num' is some kind of pointer)
    if is_interactive:
        self.assertEqual(csv_reader.line_num, 7)
    else:
        self.assertEqual(csv_reader.line_num, 6)

    # return to test function
    return
