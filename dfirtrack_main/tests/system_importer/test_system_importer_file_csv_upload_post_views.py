    # TODO: [code] rebuild test

#    def test_system_importer_file_csv_upload_post_double(self):
#        """ test importer view """
#
#        systemcsv = open(os.path.join(BASE_DIR, 'dfirtrack_main/tests/system/files/system_importer_file_csv_testfile_double.csv'), 'r')
#        # compare
#        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
#        self.assertEqual(len(System.objects.filter(system_name='system_double')), 2)
#        self.assertEqual(str(messages[0]), 'System system_double already exists multiple times. Nothing was changed for this system.')
#

    # TODO: [code] rebuild test

#    def test_system_importer_file_csv_upload_post_wrong(self):
#        """ test importer view """
#
#        systemcsv = open(os.path.join(BASE_DIR, 'dfirtrack_main/tests/system/files/system_importer_file_csv_testfile_wrong.csv'), 'r')
#        # compare
#        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
#        self.assertEqual(str(messages[0]), 'Value for system in row 1 was an empty string. System not created.')
#        self.assertEqual(str(messages[1]), 'Value for system in row 2 was too long. System not created.')
#

    # TODO: [code] rebuild test

#    def test_system_importer_file_csv_upload_post_skip(self):
#        """ test importer view """
#
#        systemcsv = open(os.path.join(BASE_DIR, 'dfirtrack_main/tests/system/files/system_importer_file_csv_testfile_skip.csv'), 'r')
#        # compare
#        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
#        self.assertEqual(str(messages[0]), '2 systems were skipped.')
#        self.assertEqual(system_skip_1.analysisstatus, None)
#        self.assertEqual(system_skip_1.systemstatus, systemstatus_1)
#        self.assertTrue(system_skip_1.ip.filter(ip_ip='127.1.1.1').exists())
#        self.assertFalse(system_skip_1.ip.filter(ip_ip='127.2.2.2').exists())
#        self.assertEqual(system_skip_2.analysisstatus, None)
#        self.assertEqual(system_skip_2.systemstatus, systemstatus_1)
#        self.assertTrue(system_skip_2.ip.filter(ip_ip='127.3.3.3').exists())
#        self.assertFalse(system_skip_2.ip.filter(ip_ip='127.4.4.4').exists())

    # TODO: [code] rebuild test

#    def test_system_importer_file_csv_upload_post_update_discard_manytomany(self):
#        """ test importer view """
#
#        systemcsv = open(os.path.join(BASE_DIR, 'dfirtrack_main/tests/system/files/system_importer_file_csv_testfile_update_discard_manytomany.csv'), 'r')
#        # compare - general
#        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
#        self.assertEqual(str(messages[0]), '2 systems were updated.')
#        # compare - system_update_discard_manytomany_1
#        self.assertFalse(system_update_discard_manytomany_1.case.filter(case_name='case_1').exists())
#        self.assertTrue(system_update_discard_manytomany_1.case.filter(case_name='case_2').exists())
#        self.assertFalse(system_update_discard_manytomany_1.company.filter(company_name='company_1').exists())
#        self.assertTrue(system_update_discard_manytomany_1.company.filter(company_name='company_2').exists())
#        self.assertFalse(system_update_discard_manytomany_1.ip.filter(ip_ip='10.1.1.1').exists())
#        self.assertTrue(system_update_discard_manytomany_1.ip.filter(ip_ip='10.3.3.3').exists())
#        self.assertEqual(system_update_discard_manytomany_1.systemstatus, systemstatus_2)
#        self.assertFalse(system_update_discard_manytomany_1.tag.filter(tag_name='tag_1').exists())
#        self.assertTrue(system_update_discard_manytomany_1.tag.filter(tag_name='tag_2').exists())
#        # compare - system_update_discard_manytomany_2
#        self.assertTrue(system_update_discard_manytomany_2.case.filter(case_name='case_2').exists())
#        self.assertTrue(system_update_discard_manytomany_2.company.filter(company_name='company_2').exists())
#        self.assertFalse(system_update_discard_manytomany_2.ip.filter(ip_ip='10.2.2.2').exists())
#        self.assertTrue(system_update_discard_manytomany_2.ip.filter(ip_ip='10.4.4.4').exists())
#        self.assertEqual(system_update_discard_manytomany_2.systemstatus, systemstatus_2)
#        self.assertTrue(system_update_discard_manytomany_2.tag.filter(tag_name='tag_2').exists())
#

    # TODO: [code] rebuild test

#    def test_system_importer_file_csv_upload_post_update_keep_manytomany(self):
#        """ test importer view """
#
#        systemcsv = open(os.path.join(BASE_DIR, 'dfirtrack_main/tests/system/files/system_importer_file_csv_testfile_update_keep_manytomany.csv'), 'r')
#        # compare - general
#        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
#        self.assertEqual(str(messages[0]), '2 systems were updated.')
#        # compare - system_update_keep_manytomany_1
#        self.assertTrue(system_update_keep_manytomany_1.case.filter(case_name='case_1').exists())
#        self.assertTrue(system_update_keep_manytomany_1.case.filter(case_name='case_2').exists())
#        self.assertTrue(system_update_keep_manytomany_1.company.filter(company_name='company_1').exists())
#        self.assertTrue(system_update_keep_manytomany_1.company.filter(company_name='company_2').exists())
#        self.assertTrue(system_update_keep_manytomany_1.ip.filter(ip_ip='10.5.5.5').exists())
#        self.assertTrue(system_update_keep_manytomany_1.ip.filter(ip_ip='10.7.7.7').exists())
#        self.assertEqual(system_update_keep_manytomany_1.systemstatus, systemstatus_2)
#        self.assertTrue(system_update_keep_manytomany_1.tag.filter(tag_name='tag_1').exists())
#        self.assertTrue(system_update_keep_manytomany_1.tag.filter(tag_name='tag_2').exists())
#        # compare - system_update_keep_manytomany_2
#        self.assertTrue(system_update_keep_manytomany_2.case.filter(case_name='case_2').exists())
#        self.assertTrue(system_update_keep_manytomany_2.company.filter(company_name='company_2').exists())
#        self.assertTrue(system_update_keep_manytomany_2.ip.filter(ip_ip='10.6.6.6').exists())
#        self.assertTrue(system_update_keep_manytomany_2.ip.filter(ip_ip='10.8.8.8').exists())
#        self.assertEqual(system_update_keep_manytomany_2.systemstatus, systemstatus_2)
#        self.assertTrue(system_update_keep_manytomany_2.tag.filter(tag_name='tag_2').exists())

    # TODO: [code] rebuild test

#    def test_system_importer_file_csv_upload_post_create_single(self):
#        """ test importer view """
#
#        systemcsv = open(os.path.join(BASE_DIR, 'dfirtrack_main/tests/system/files/system_importer_file_csv_testfile_create_single.csv'), 'r')
#        # compare
#        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
#        self.assertEqual(str(messages[0]), '1 system was created.')
#        self.assertTrue(System.objects.filter(system_name='system_create_single_1').exists())
#        self.assertFalse(system_1.ip.filter(ip_ip='127.1.2.31').exists())
#        self.assertEqual(system_1.analysisstatus, analysisstatus_1)
#        self.assertEqual(system_1.systemstatus, systemstatus_1)
#

    # TODO: [code] rebuild test

#    def test_system_importer_file_csv_upload_post_update_single(self):
#        """ test importer view """
#
#        systemcsv = open(os.path.join(BASE_DIR, 'dfirtrack_main/tests/system/files/system_importer_file_csv_testfile_update_single.csv'), 'r')
#        # compare
#        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
#        self.assertEqual(str(messages[0]), '1 system was updated.')
#        self.assertTrue(System.objects.filter(system_name='system_update_single_1').exists())
#        self.assertTrue(system_1.ip.filter(ip_ip='127.2.3.41').exists())
#        self.assertTrue(system_1.ip.filter(ip_ip='127.2.3.42').exists())
#        self.assertEqual(system_1.analysisstatus, analysisstatus_1)
#        self.assertEqual(system_1.systemstatus, systemstatus_2)
#

    # TODO: [code] rebuild test

#    def test_system_importer_file_csv_upload_post_skip_single(self):
#        """ test importer view """
#
#        systemcsv = open(os.path.join(BASE_DIR, 'dfirtrack_main/tests/system/files/system_importer_file_csv_testfile_skip_single.csv'), 'r')
#        # compare
#        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
#        self.assertEqual(str(messages[0]), '1 system was skipped.')
#        self.assertTrue(System.objects.filter(system_name='system_skip_single_1').exists())
#        self.assertTrue(system_1.ip.filter(ip_ip='127.3.4.51').exists())
#        self.assertFalse(system_1.ip.filter(ip_ip='127.3.4.52').exists())
#        self.assertEqual(system_1.analysisstatus, None)
#        self.assertEqual(system_1.systemstatus, systemstatus_1)
#

    # TODO: [code] rebuild test

#    def test_system_importer_file_csv_upload_post_invalid_ip(self):
#        """ test importer view """
#
#        systemcsv = open(os.path.join(BASE_DIR, 'dfirtrack_main/tests/system/files/system_importer_file_csv_testfile_invalid_ip.csv'), 'r')
#        # compare
#        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
#        self.assertEqual(str(messages[0]), 'Value for ip address in row 1 was not a valid IP address.')
#        self.assertEqual(str(messages[1]), '1 system was created.')
#        self.assertTrue(System.objects.filter(system_name='system_invalid_ip_1').exists())
#        self.assertEqual(system_1.analysisstatus, analysisstatus_1)
#        self.assertEqual(system_1.systemstatus, systemstatus_1)
