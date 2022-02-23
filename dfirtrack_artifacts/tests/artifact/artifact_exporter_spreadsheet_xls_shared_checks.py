from dfirtrack_artifacts.models import Artifact, Artifactstatus, Artifacttype


def artifact_exporter_spreadsheet_xls_complete_spreadsheet_check(
    self, artifactlist, mocktime, xls_user
):
    """test for complete spreadsheet content"""

    """ prepare objects section """

    # get objects
    artifact_1 = Artifact.objects.get(
        artifact_name='artifact_exporter_spreadsheet_xls_artifact_1_all_attributes'
    )
    artifact_2 = Artifact.objects.get(
        artifact_name='artifact_exporter_spreadsheet_xls_artifact_2_no_attributes'
    )

    # create lists for easier comparison with whole columns - artifactstatus
    artifactstatus_id_list = ['ID']
    artifactstatus_name_list = ['Artifactstatus']
    artifactstatus_note_list = ['Note']
    all_artifactstatus = Artifactstatus.objects.all().order_by('artifactstatus_name')
    for artifactstatus_object in all_artifactstatus:
        '''
        the conversion to float was carried out,
        because otherwise the return values from the spreadsheet would have had to be converted to int,
        which would have been more time-consuming
        '''
        artifactstatus_id_list.append(float(artifactstatus_object.artifactstatus_id))
        artifactstatus_name_list.append(artifactstatus_object.artifactstatus_name)
        if artifactstatus_object.artifactstatus_note:
            artifactstatus_note_list.append(artifactstatus_object.artifactstatus_note)
        else:
            artifactstatus_note_list.append('---')

    # create lists for easier comparison with whole columns - artifacttype
    artifacttype_id_list = ['ID']
    artifacttype_name_list = ['Artifacttype']
    artifacttype_note_list = ['Note']
    all_artifacttype = Artifacttype.objects.all().order_by('artifacttype_name')
    for artifacttype_object in all_artifacttype:
        '''
        the conversion to float was carried out,
        because otherwise the return values from the spreadsheet would have had to be converted to int,
        which would have been more time-consuming
        '''
        artifacttype_id_list.append(float(artifacttype_object.artifacttype_id))
        artifacttype_name_list.append(artifacttype_object.artifacttype_name)
        if artifacttype_object.artifacttype_note:
            artifacttype_note_list.append(artifacttype_object.artifacttype_note)
        else:
            artifacttype_note_list.append('---')

    # get sheets
    sheet_artifacts = artifactlist.sheet_by_name('artifacts')
    sheet_artifactstatus = artifactlist.sheet_by_name('artifactstatus')
    sheet_artifacttype = artifactlist.sheet_by_name('artifacttype')

    """ compare values section """

    # compare number of rows and columns
    self.assertEqual(sheet_artifacts.nrows, 6)
    self.assertEqual(sheet_artifacts.ncols, 23)
    self.assertEqual(sheet_artifactstatus.nrows, 14)
    self.assertEqual(sheet_artifactstatus.ncols, 3)
    self.assertEqual(sheet_artifacttype.nrows, 7)
    self.assertEqual(sheet_artifacttype.ncols, 3)

    # compare headlines
    self.assertEqual(
        sheet_artifacts.row_values(0),
        [
            'Artifact ID',
            'Artifact',
            'System ID',
            'System',
            'Artifactstatus',
            'Artifactpriority',
            'Artifacttype',
            'Source path',
            'Storage path',
            'Internal note',
            'External note',
            'Analysis result',
            'MD5',
            'SHA1',
            'SHA256',
            'Case ID',
            'Case',
            'Tags',
            'Assigned to',
            'Created',
            'Created by',
            'Modified',
            'Modified by',
        ],
    )
    self.assertEqual(
        sheet_artifactstatus.row_values(0), ['ID', 'Artifactstatus', 'Note']
    )
    self.assertEqual(sheet_artifacttype.row_values(0), ['ID', 'Artifacttype', 'Note'])

    # compare content - artifact 1
    self.assertEqual(int(sheet_artifacts.cell(1, 0).value), artifact_1.artifact_id)
    self.assertEqual(sheet_artifacts.cell(1, 1).value, artifact_1.artifact_name)
    self.assertEqual(int(sheet_artifacts.cell(1, 2).value), artifact_1.system.system_id)
    self.assertEqual(sheet_artifacts.cell(1, 3).value, artifact_1.system.system_name)
    self.assertEqual(
        sheet_artifacts.cell(1, 4).value,
        artifact_1.artifactstatus.artifactstatus_name,
    )
    self.assertEqual(
        sheet_artifacts.cell(1, 5).value,
        artifact_1.artifactpriority.artifactpriority_name,
    )
    self.assertEqual(
        sheet_artifacts.cell(1, 6).value, artifact_1.artifacttype.artifacttype_name
    )
    self.assertEqual(sheet_artifacts.cell(1, 7).value, artifact_1.artifact_source_path)
    self.assertEqual(sheet_artifacts.cell(1, 8).value, artifact_1.artifact_storage_path)
    self.assertEqual(
        sheet_artifacts.cell(1, 9).value, 'artifact note for internal usage'
    )  # artifact_note_internal
    self.assertEqual(
        sheet_artifacts.cell(1, 10).value, 'artifact note for external usage'
    )  # artifact_note_external
    self.assertEqual(
        sheet_artifacts.cell(1, 11).value, 'artifact note for analysis result'
    )  # artifact_note_analysisresult
    self.assertEqual(sheet_artifacts.cell(1, 12).value, artifact_1.artifact_md5)
    self.assertEqual(sheet_artifacts.cell(1, 13).value, artifact_1.artifact_sha1)
    self.assertEqual(sheet_artifacts.cell(1, 14).value, artifact_1.artifact_sha256)
    self.assertEqual(int(sheet_artifacts.cell(1, 15).value), artifact_1.case.case_id)
    self.assertEqual(sheet_artifacts.cell(1, 16).value, artifact_1.case.case_name)
    self.assertEqual(sheet_artifacts.cell(1, 17).value, 'tag_1 tag_2')
    self.assertEqual(
        sheet_artifacts.cell(1, 18).value,
        str(artifact_1.artifact_assigned_to_user_id),
    )
    self.assertEqual(sheet_artifacts.cell(1, 19).value, '2012-11-10 12:34')
    self.assertEqual(
        sheet_artifacts.cell(1, 20).value,
        str(artifact_1.artifact_created_by_user_id),
    )
    self.assertEqual(sheet_artifacts.cell(1, 21).value, '2012-11-10 12:34')
    self.assertEqual(
        sheet_artifacts.cell(1, 22).value,
        str(artifact_1.artifact_modified_by_user_id),
    )

    # compare content - artifact 2
    self.assertEqual(int(sheet_artifacts.cell(2, 0).value), artifact_2.artifact_id)
    self.assertEqual(sheet_artifacts.cell(2, 1).value, artifact_2.artifact_name)
    self.assertEqual(int(sheet_artifacts.cell(2, 2).value), artifact_2.system.system_id)
    self.assertEqual(sheet_artifacts.cell(2, 3).value, artifact_2.system.system_name)
    self.assertEqual(
        sheet_artifacts.cell(2, 4).value,
        artifact_2.artifactstatus.artifactstatus_name,
    )
    self.assertEqual(
        sheet_artifacts.cell(2, 5).value,
        artifact_2.artifactpriority.artifactpriority_name,
    )
    self.assertEqual(
        sheet_artifacts.cell(2, 6).value, artifact_2.artifacttype.artifacttype_name
    )
    self.assertEqual(sheet_artifacts.cell(2, 7).value, '')
    self.assertEqual(sheet_artifacts.cell(2, 8).value, artifact_2.artifact_storage_path)
    self.assertEqual(sheet_artifacts.cell(2, 9).value, '')
    self.assertEqual(sheet_artifacts.cell(2, 10).value, '')
    self.assertEqual(sheet_artifacts.cell(2, 11).value, '')
    self.assertEqual(sheet_artifacts.cell(2, 12).value, '')
    self.assertEqual(sheet_artifacts.cell(2, 13).value, '')
    self.assertEqual(sheet_artifacts.cell(2, 14).value, '')
    self.assertEqual(sheet_artifacts.cell(2, 15).value, '')
    self.assertEqual(sheet_artifacts.cell(2, 16).value, '')
    self.assertEqual(sheet_artifacts.cell(2, 17).value, '')
    self.assertEqual(sheet_artifacts.cell(2, 18).value, '')
    self.assertEqual(sheet_artifacts.cell(2, 19).value, '2009-08-07 23:45')
    self.assertEqual(
        sheet_artifacts.cell(2, 20).value,
        str(artifact_1.artifact_created_by_user_id),
    )
    self.assertEqual(sheet_artifacts.cell(2, 21).value, '2009-08-07 23:45')
    self.assertEqual(
        sheet_artifacts.cell(2, 22).value,
        str(artifact_1.artifact_modified_by_user_id),
    )

    # compare content - artifactstatus worksheet (whole columns)
    self.assertEqual(sheet_artifactstatus.col_values(0), artifactstatus_id_list)
    self.assertEqual(sheet_artifactstatus.col_values(1), artifactstatus_name_list)
    self.assertEqual(sheet_artifactstatus.col_values(2), artifactstatus_note_list)

    # compare content - artifacttype worksheet (whole columns)
    self.assertEqual(sheet_artifacttype.col_values(0), artifacttype_id_list)
    self.assertEqual(sheet_artifacttype.col_values(1), artifacttype_name_list)
    self.assertEqual(sheet_artifacttype.col_values(2), artifacttype_note_list)

    # compare content - metadata
    self.assertEqual(sheet_artifacts.cell(4, 0).value, 'Created:')
    self.assertEqual(
        sheet_artifacts.cell(4, 1).value, mocktime.strftime('%Y-%m-%d %H:%M')
    )
    self.assertEqual(sheet_artifacts.cell(5, 0).value, 'Created by:')
    self.assertEqual(
        sheet_artifacts.cell(5, 1).value,
        xls_user,
    )

    # return to test function
    return
