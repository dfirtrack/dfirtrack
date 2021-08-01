from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from dfirtrack_main.forms import EntryFileImport, EntryFileImportFields, EntryForm
from dfirtrack_main.models import Case, System, Systemstatus


class EntryFormTestCase(TestCase):
    """entry form tests"""

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(
            username="testuser_entry", password="z2B7MofdZ4suAn6AYGSo"
        )

        # create object
        systemstatus_1 = Systemstatus.objects.create(systemstatus_name="systemstatus_1")

        # create object
        System.objects.create(
            system_name="system_1",
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )

        # create object
        Case.objects.create(
            case_name="case_1",
            case_is_incident=True,
            case_created_by_user_id=test_user,
        )

    def test_entry_time_form_label(self):
        """test form label"""

        # get object
        form = EntryForm()
        # compare
        self.assertEqual(
            form.fields["entry_time"].label,
            "Entry time (for sorting) (YYYY-MM-DD HH:MM:SS) (*)",
        )

    def test_system_form_label(self):
        """test form label"""

        # get object
        form = EntryForm()
        # compare
        self.assertEqual(form.fields["system"].label, "System (*)")
        self.assertEqual(form.fields["system"].empty_label, "Select system")

    def test_entry_sha1_form_label(self):
        """test form label"""

        # get object
        form = EntryForm()
        # compare
        self.assertEqual(form.fields["entry_sha1"].label, "Entry sha1")

    def test_entry_type_form_label(self):
        """test form label"""

        # get object
        form = EntryForm()
        # compare
        self.assertEqual(form.fields["entry_type"].label, "Entry type")

    def test_entry_content_form_label(self):
        """test form label"""

        # get object
        form = EntryForm()
        # compare
        self.assertEqual(form.fields["entry_content"].label, "Entry content")

    def test_entry_note_form_label(self):
        """test form label"""

        # get object
        form = EntryForm()
        # compare
        self.assertEqual(form.fields["entry_note"].label, "Entry note")

    def test_case_form_label(self):
        """test form label"""

        # get object
        form = EntryForm()
        # compare
        self.assertEqual(form.fields["case"].label, "Case")
        self.assertEqual(form.fields["case"].empty_label, "Select case (optional)")

    def test_tag_form_label(self):
        """test form label"""

        # get object
        form = EntryForm()
        # compare
        self.assertEqual(form.fields["tag"].label, "Tags")

    def test_entry_form_empty(self):
        """test minimum form requirements / INVALID"""

        # get object
        form = EntryForm(data={})
        # compare
        self.assertFalse(form.is_valid())

    def test_entry_time_form_filled(self):
        """test minimum form requirements / INVALID"""

        # get object
        form = EntryForm(
            data={
                "entry_time": "2001-02-03 12:34:56",
            }
        )
        # compare
        self.assertFalse(form.is_valid())

    def test_system_form_filled(self):
        """test minimum form requirements / VALID"""

        # get foreign key object id
        system_id = System.objects.get(system_name="system_1").system_id
        # get object
        form = EntryForm(
            data={
                "entry_time": "2009-08-07 12:34:56",
                "system": system_id,
            }
        )
        # compare
        self.assertTrue(form.is_valid())

    def test_entry_sha1_form_filled(self):
        """test additional form content"""

        # get foreign key object id
        system_id = System.objects.get(system_name="system_1").system_id
        # get object
        form = EntryForm(
            data={
                "entry_time": "2009-08-07 12:34:56",
                "system": system_id,
                "entry_sha1": "da39a3ee5e6b4b0d3255bfef95601890afd80709",
            }
        )
        # compare
        self.assertTrue(form.is_valid())

    def test_entry_type_form_filled(self):
        """test additional form content"""

        # get foreign key object id
        system_id = System.objects.get(system_name="system_1").system_id
        # get object
        form = EntryForm(
            data={
                "entry_time": "2009-08-07 12:34:56",
                "system": system_id,
                "entry_type": "type_1",
            }
        )
        # compare
        self.assertTrue(form.is_valid())

    def test_entry_content_form_filled(self):
        """test additional form content"""

        # get foreign key object id
        system_id = System.objects.get(system_name="system_1").system_id
        # get object
        form = EntryForm(
            data={
                "entry_time": "2009-08-07 12:34:56",
                "system": system_id,
                "entry_content": "lorem ipsum",
            }
        )
        # compare
        self.assertTrue(form.is_valid())

    def test_entry_note_form_filled(self):
        """test additional form content"""

        # get foreign key object id
        system_id = System.objects.get(system_name="system_1").system_id
        # get object
        form = EntryForm(
            data={
                "entry_time": "2009-08-07 12:34:56",
                "system": system_id,
                "entry_note": "lorem ipsum",
            }
        )
        # compare
        self.assertTrue(form.is_valid())

    def test_entry_case_form_filled(self):
        """test additional form content"""

        # get foreign key object id
        case_id = Case.objects.get(case_name="case_1").case_id
        # get foreign key object id
        system_id = System.objects.get(system_name="system_1").system_id
        # get object
        form = EntryForm(
            data={
                "entry_time": "2009-08-07 12:34:56",
                "system": system_id,
                "case": case_id,
            }
        )
        # compare
        self.assertTrue(form.is_valid())

    def test_entry_sha1_proper_chars(self):
        """test for max length"""

        # define datetime string
        entry_time_string = "2009-08-07 12:34:56"
        # get foreign key object id
        system_id = System.objects.get(system_name="system_1").system_id
        # get object
        form = EntryForm(
            data={
                "entry_time": entry_time_string,
                "system": system_id,
                "entry_sha1": "ssssssssssssssssssssssssssssssssssssssss",
            }
        )
        # compare
        self.assertTrue(form.is_valid())

    def test_entry_sha1_too_many_chars(self):
        """test for max length"""

        # define datetime string
        entry_time_string = "2009-08-07 12:34:56"
        # get foreign key object id
        system_id = System.objects.get(system_name="system_1").system_id
        # get object
        form = EntryForm(
            data={
                "entry_time": entry_time_string,
                "system": system_id,
                "entry_sha1": "sssssssssssssssssssssssssssssssssssssssss",
            }
        )
        # compare
        self.assertFalse(form.is_valid())

    def test_entry_type_proper_chars(self):
        """test for max length"""

        # define datetime string
        entry_time_string = "2009-08-07 12:34:56"
        # get foreign key object id
        system_id = System.objects.get(system_name="system_1").system_id
        # get object
        form = EntryForm(
            data={
                "entry_time": entry_time_string,
                "system": system_id,
                "entry_type": "tttttttttttttttttttttttttttttt",
            }
        )
        # compare
        self.assertTrue(form.is_valid())

    def test_entry_type_too_many_chars(self):
        """test for max length"""

        # define datetime string
        entry_time_string = "2009-08-07 12:34:56"
        # get foreign key object id
        system_id = System.objects.get(system_name="system_1").system_id
        # get object
        form = EntryForm(
            data={
                "entry_time": entry_time_string,
                "system": system_id,
                "entry_type": "ttttttttttttttttttttttttttttttt",
            }
        )
        # compare
        self.assertFalse(form.is_valid())

    """
         EntryFileImport Form Tests
    """

    def test_entry_file_import_system_form_label(self):
        """test form label"""

        # get object
        form = EntryFileImport()
        # compare
        self.assertEqual(form.fields["system"].label, "System (*)")
        self.assertEqual(form.fields["system"].empty_label, "Select system")
        self.assertEqual(form.fields["system"].widget.attrs["class"], "form-select")

    def test_entry_file_import_case_form_label(self):
        """test form label"""

        # get object
        form = EntryFileImport()
        # compare
        self.assertEqual(form.fields["case"].label, "Case")
        self.assertEqual(form.fields["case"].empty_label, "Select case (optional)")
        self.assertEqual(form.fields["case"].widget.attrs["class"], "form-select")

    def test_entry_file_import_entryfile_form_label(self):
        """test form label"""

        # get object
        form = EntryFileImport()
        # compare
        self.assertEqual(form.fields["entryfile"].label, "CSV file (*)")
        self.assertEqual(form.fields["entryfile"].widget.attrs["class"], "form-control")

    def test_entry_file_import_form_filled(self):
        """test additional form content"""

        # get foreign key object id
        system_id = System.objects.get(system_name="system_1").system_id
        # mock csv file
        csv_file = SimpleUploadedFile(
            "test.csv", b"datetime,timestamp_desc,message", content_type="text/csv"
        )
        # get object
        form = EntryFileImport({"system": system_id}, {"entryfile": csv_file})
        # compare
        self.assertTrue(form.is_valid())

    """
         EntryFileImportFields Form Tests
    """

    def test_entry_file_import_fileds_entry_time_form_label(self):
        """test form label"""

        # get object
        form = EntryFileImportFields([])
        # compare
        self.assertEqual(form.fields["entry_time"].label, "Datetime field")
        self.assertEqual(form.fields["entry_time"].widget.attrs["class"], "form-select")

    def test_entry_file_import_fileds_entry_type_form_label(self):
        """test form label"""

        # get object
        form = EntryFileImportFields([])
        # compare
        self.assertEqual(form.fields["entry_type"].widget.attrs["class"], "form-select")

    def test_entry_file_import_fileds_entry_content_form_label(self):
        """test form label"""

        # get object
        form = EntryFileImportFields([])
        # compare
        self.assertEqual(
            form.fields["entry_content"].widget.attrs["class"], "form-select"
        )

    def test_entry_file_import_fileds_empty_choices(self):
        """ " test dynamic choices"""

        # get object
        form = EntryFileImportFields([])

        self.assertEqual(form.fields["entry_time"].choices, [(-1, "--")])
        self.assertEqual(form.fields["entry_type"].choices, [(-1, "--")])
        self.assertEqual(form.fields["entry_content"].choices, [(-1, "--")])

    def test_entry_file_import_fileds_mock_choices(self):
        """ " test dynamic choices"""

        # get object
        form = EntryFileImportFields(["c_0", "c_1", "c_2"])

        # expected choices
        result = [
            (-1, "--"),
            (0, "c_0"),
            (1, "c_1"),
            (2, "c_2"),
        ]

        # check
        self.assertEqual(form.fields["entry_time"].choices, result)
        self.assertEqual(form.fields["entry_type"].choices, result)
        self.assertEqual(form.fields["entry_content"].choices, result)
        self.assertEqual(form.fields["entry_tag"].choices, result)

    def test_entry_file_import_fileds_form_filled(self):
        """test filled form"""

        # get object
        form = EntryFileImportFields(
            ["c_0", "c_1", "c_2"],
            data={
                "entry_time": 0,
                "entry_type": 1,
                "entry_content": 2,
            },
        )
        # compare
        self.assertTrue(form.is_valid())

    def test_entry_file_import_fileds_form_error_entry_time(self):
        """test filled form"""

        # get object
        form = EntryFileImportFields(
            ["c_0", "c_1"],
            data={
                "entry_time": -1,
                "entry_type": 0,
                "entry_content": 1,
            },
        )
        # compare
        self.assertFalse(form.is_valid())
        self.assertInHTML("Please select a datetime value.", form.errors["__all__"][0])

    def test_entry_file_import_fileds_form_error_entry_type(self):
        """test filled form"""

        # get object
        form = EntryFileImportFields(
            ["c_0", "c_1"],
            data={
                "entry_time": 0,
                "entry_type": -1,
                "entry_content": 1,
            },
        )
        # compare
        self.assertFalse(form.is_valid())
        self.assertInHTML(
            "Please select an entry type value.", form.errors["__all__"][0]
        )

    def test_entry_file_import_fileds_form_error_entry_content(self):
        """test filled form"""

        # get object
        form = EntryFileImportFields(
            ["c_0", "c_1"],
            data={
                "entry_time": 0,
                "entry_type": 1,
                "entry_content": -1,
            },
        )
        # compare
        self.assertFalse(form.is_valid())
        self.assertInHTML(
            "Please select an entry content value.", form.errors["__all__"][0]
        )

    def test_entry_file_import_fileds_form_filled_with_tag(self):
        """test filled form"""

        # get object
        form = EntryFileImportFields(
            ["c_0", "c_1", "c_2"],
            data={
                "entry_time": 0,
                "entry_type": 1,
                "entry_content": 2,
                "entry_tag": -1,
            },
        )
        # compare
        self.assertTrue(form.is_valid())
