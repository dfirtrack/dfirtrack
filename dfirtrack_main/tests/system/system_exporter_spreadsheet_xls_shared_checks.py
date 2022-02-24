from dfirtrack_main.models import (
    Analysisstatus,
    Reason,
    Recommendation,
    System,
    Systemstatus,
    Tag,
)


def system_exporter_spreadsheet_xls_complete_spreadsheet_check(
    self, xls_file, mocktime, xls_user
):
    """test for complete spreadsheet content"""

    """ prepare objects section """

    # get objects
    system_1 = System.objects.get(system_name='system_1_all_attributes')
    system_2 = System.objects.get(system_name='system_2_no_attributes')

    # create lists for easier comparison with whole columns - systemstatus
    systemstatus_id_list = ['ID']
    systemstatus_name_list = ['Systemstatus']
    systemstatus_note_list = ['Note']
    all_systemstatus = Systemstatus.objects.all().order_by('systemstatus_name')
    for systemstatus_object in all_systemstatus:
        # the conversion to float was carried out, because otherwise the return values from the spreadsheet would have had to be converted to int, which would have been more time-consuming
        systemstatus_id_list.append(float(systemstatus_object.systemstatus_id))
        systemstatus_name_list.append(systemstatus_object.systemstatus_name)
        if systemstatus_object.systemstatus_note:
            systemstatus_note_list.append(systemstatus_object.systemstatus_note)
        else:
            systemstatus_note_list.append('')

    # create lists for easier comparison with whole columns - analysisstatus
    analysisstatus_id_list = ['ID']
    analysisstatus_name_list = ['Analysisstatus']
    analysisstatus_note_list = ['Note']
    all_analysisstatus = Analysisstatus.objects.all().order_by('analysisstatus_name')
    for analysisstatus_object in all_analysisstatus:
        # the conversion to float was carried out, because otherwise the return values from the spreadsheet would have had to be converted to int, which would have been more time-consuming
        analysisstatus_id_list.append(float(analysisstatus_object.analysisstatus_id))
        analysisstatus_name_list.append(analysisstatus_object.analysisstatus_name)
        if analysisstatus_object.analysisstatus_note:
            analysisstatus_note_list.append(analysisstatus_object.analysisstatus_note)
        else:
            analysisstatus_note_list.append('')

    # create lists for easier comparison with whole columns - reason
    reason_id_list = ['ID']
    reason_name_list = ['Reason']
    reason_note_list = ['Note']
    all_reason = Reason.objects.all().order_by('reason_name')
    for reason_object in all_reason:
        # the conversion to float was carried out, because otherwise the return values from the spreadsheet would have had to be converted to int, which would have been more time-consuming
        reason_id_list.append(float(reason_object.reason_id))
        reason_name_list.append(reason_object.reason_name)
        if reason_object.reason_note:
            reason_note_list.append(reason_object.reason_note)
        else:
            reason_note_list.append('')

    # create lists for easier comparison with whole columns - recommendation
    recommendation_id_list = ['ID']
    recommendation_name_list = ['Recommendation']
    recommendation_note_list = ['Note']
    all_recommendation = Recommendation.objects.all().order_by('recommendation_name')
    for recommendation_object in all_recommendation:
        # the conversion to float was carried out, because otherwise the return values from the spreadsheet would have had to be converted to int, which would have been more time-consuming
        recommendation_id_list.append(float(recommendation_object.recommendation_id))
        recommendation_name_list.append(recommendation_object.recommendation_name)
        if recommendation_object.recommendation_note:
            recommendation_note_list.append(recommendation_object.recommendation_note)
        else:
            recommendation_note_list.append('')

    # create lists for easier comparison with whole columns - tag
    tag_id_list = ['ID']
    tag_name_list = ['Tag']
    tag_note_list = ['Note']
    all_tag = Tag.objects.all().order_by('tag_name')
    for tag_object in all_tag:
        # the conversion to float was carried out, because otherwise the return values from the spreadsheet would have had to be converted to int, which would have been more time-consuming
        tag_id_list.append(float(tag_object.tag_id))
        tag_name_list.append(tag_object.tag_name)
        if tag_object.tag_note:
            tag_note_list.append(tag_object.tag_note)
        else:
            tag_note_list.append('')

    # get sheets
    sheet_systems = xls_file.sheet_by_name('systems')
    sheet_systemstatus = xls_file.sheet_by_name('systemstatus')
    sheet_analysisstatus = xls_file.sheet_by_name('analysisstatus')
    sheet_reasons = xls_file.sheet_by_name('reasons')
    sheet_recommendations = xls_file.sheet_by_name('recommendations')
    sheet_tags = xls_file.sheet_by_name('tags')

    """ compare values section """

    # compare number of rows and columns
    self.assertEqual(sheet_systems.nrows, 6)
    self.assertEqual(sheet_systems.ncols, 21)
    self.assertEqual(sheet_systemstatus.nrows, 10)
    self.assertEqual(sheet_systemstatus.ncols, 3)
    self.assertEqual(sheet_analysisstatus.nrows, 7)
    self.assertEqual(sheet_analysisstatus.ncols, 3)
    self.assertEqual(sheet_reasons.nrows, 2)
    self.assertEqual(sheet_reasons.ncols, 3)
    self.assertEqual(sheet_recommendations.nrows, 2)
    self.assertEqual(sheet_recommendations.ncols, 3)
    self.assertEqual(sheet_tags.nrows, 9)
    self.assertEqual(sheet_tags.ncols, 3)

    # compare headlines
    self.assertEqual(
        sheet_systems.row_values(0),
        [
            'ID',
            'System',
            'DNS name',
            'Domain',
            'Systemstatus',
            'Analysisstatus',
            'Reason',
            'Recommendation',
            'Systemtype',
            'IP',
            'OS',
            'Company',
            'Location',
            'Serviceprovider',
            'Tag',
            'Case',
            'Assigned to',
            'Created',
            'Created by',
            'Modified',
            'Modified by',
        ],
    )

    # compare content - system 1
    self.assertEqual(int(sheet_systems.cell(1, 0).value), system_1.system_id)
    self.assertEqual(sheet_systems.cell(1, 1).value, system_1.system_name)
    self.assertEqual(sheet_systems.cell(1, 2).value, system_1.dnsname.dnsname_name)
    self.assertEqual(sheet_systems.cell(1, 3).value, system_1.domain.domain_name)
    self.assertEqual(
        sheet_systems.cell(1, 4).value, system_1.systemstatus.systemstatus_name
    )
    self.assertEqual(
        sheet_systems.cell(1, 5).value, system_1.analysisstatus.analysisstatus_name
    )
    self.assertEqual(sheet_systems.cell(1, 6).value, system_1.reason.reason_name)
    self.assertEqual(
        sheet_systems.cell(1, 7).value, system_1.recommendation.recommendation_name
    )
    self.assertEqual(
        sheet_systems.cell(1, 8).value, system_1.systemtype.systemtype_name
    )
    self.assertEqual(sheet_systems.cell(1, 9).value, '127.0.0.1\n127.0.0.2\n127.0.0.3')
    self.assertEqual(sheet_systems.cell(1, 10).value, system_1.os.os_name)
    self.assertEqual(sheet_systems.cell(1, 11).value, 'company_1\ncompany_2\ncompany_3')
    self.assertEqual(sheet_systems.cell(1, 12).value, system_1.location.location_name)
    self.assertEqual(
        sheet_systems.cell(1, 13).value,
        system_1.serviceprovider.serviceprovider_name,
    )
    self.assertEqual(sheet_systems.cell(1, 14).value, 'tag_1\ntag_2\ntag_3')
    self.assertEqual(sheet_systems.cell(1, 15).value, 'case_1\ncase_2\ncase_3')
    self.assertEqual(
        sheet_systems.cell(1, 16).value, 'testuser_system_exporter_spreadsheet_xls'
    )
    self.assertEqual(sheet_systems.cell(1, 17).value, '2001-02-03 04:05')
    self.assertEqual(
        sheet_systems.cell(1, 18).value, 'testuser_system_exporter_spreadsheet_xls'
    )
    self.assertEqual(sheet_systems.cell(1, 19).value, '2001-02-03 04:05')
    self.assertEqual(
        sheet_systems.cell(1, 20).value, 'testuser_system_exporter_spreadsheet_xls'
    )

    # compare content - system 2
    self.assertEqual(int(sheet_systems.cell(2, 0).value), system_2.system_id)
    self.assertEqual(sheet_systems.cell(2, 1).value, system_2.system_name)
    self.assertEqual(sheet_systems.cell(2, 2).value, '')
    self.assertEqual(sheet_systems.cell(2, 3).value, '')
    self.assertEqual(
        sheet_systems.cell(2, 4).value, system_2.systemstatus.systemstatus_name
    )
    self.assertEqual(sheet_systems.cell(2, 5).value, '')
    self.assertEqual(sheet_systems.cell(2, 6).value, '')
    self.assertEqual(sheet_systems.cell(2, 7).value, '')
    self.assertEqual(sheet_systems.cell(2, 8).value, '')
    self.assertEqual(sheet_systems.cell(2, 9).value, '')
    self.assertEqual(sheet_systems.cell(2, 10).value, '')
    self.assertEqual(sheet_systems.cell(2, 11).value, '')
    self.assertEqual(sheet_systems.cell(2, 12).value, '')
    self.assertEqual(sheet_systems.cell(2, 13).value, '')
    self.assertEqual(sheet_systems.cell(2, 14).value, '')
    self.assertEqual(sheet_systems.cell(2, 15).value, '')
    self.assertEqual(sheet_systems.cell(2, 16).value, '')
    self.assertEqual(sheet_systems.cell(2, 17).value, '2009-08-07 06:05')
    self.assertEqual(
        sheet_systems.cell(2, 18).value, 'testuser_system_exporter_spreadsheet_xls'
    )
    self.assertEqual(sheet_systems.cell(2, 19).value, '2009-08-07 06:05')
    self.assertEqual(
        sheet_systems.cell(2, 20).value, 'testuser_system_exporter_spreadsheet_xls'
    )
    # compare content - systemstatus worksheet (whole columns)
    self.assertEqual(sheet_systemstatus.col_values(0), systemstatus_id_list)
    self.assertEqual(sheet_systemstatus.col_values(1), systemstatus_name_list)
    self.assertEqual(sheet_systemstatus.col_values(2), systemstatus_note_list)
    # compare content - analysisstatus worksheet (whole columns)
    self.assertEqual(sheet_analysisstatus.col_values(0), analysisstatus_id_list)
    self.assertEqual(sheet_analysisstatus.col_values(1), analysisstatus_name_list)
    self.assertEqual(sheet_analysisstatus.col_values(2), analysisstatus_note_list)
    # compare content - reason worksheet (whole columns)
    self.assertEqual(sheet_reasons.col_values(0), reason_id_list)
    self.assertEqual(sheet_reasons.col_values(1), reason_name_list)
    self.assertEqual(sheet_reasons.col_values(2), reason_note_list)
    # compare content - recommendation worksheet (whole columns)
    self.assertEqual(sheet_recommendations.col_values(0), recommendation_id_list)
    self.assertEqual(sheet_recommendations.col_values(1), recommendation_name_list)
    self.assertEqual(sheet_recommendations.col_values(2), recommendation_note_list)
    # compare content - tag worksheet (whole columns)
    self.assertEqual(sheet_tags.col_values(0), tag_id_list)
    self.assertEqual(sheet_tags.col_values(1), tag_name_list)
    self.assertEqual(sheet_tags.col_values(2), tag_note_list)
    # compare content - metadata
    self.assertEqual(sheet_systems.cell(4, 0).value, 'Created:')
    self.assertEqual(
        sheet_systems.cell(4, 1).value, mocktime.strftime('%Y-%m-%d %H:%M')
    )
    self.assertEqual(sheet_systems.cell(5, 0).value, 'Created by:')
    self.assertEqual(sheet_systems.cell(5, 1).value, xls_user)

    # return to test function
    return
