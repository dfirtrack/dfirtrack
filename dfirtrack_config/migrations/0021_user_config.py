import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dfirtrack_main", "0019_notestatus_values"),
        ("auth", "0012_alter_user_first_name_max_length"),
        ("dfirtrack_config", "0020_mandatory_markdown_path"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserConfigModel",
            fields=[
                (
                    "user_config_username",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name="filter_username",
                        serialize=False,
                        to="auth.user",
                    ),
                ),
                ("filter_documentation_list_keep", models.BooleanField(default=True)),
                ("filter_system_list_keep", models.BooleanField(default=True)),
                (
                    "filter_documentation_list_case",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="filter_documentation_list_case",
                        to="dfirtrack_main.case",
                    ),
                ),
                (
                    "filter_documentation_list_notestatus",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="filter_documentation_list_notestatus",
                        to="dfirtrack_main.notestatus",
                    ),
                ),
                (
                    "filter_documentation_list_tag",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="filter_documentation_list_tag",
                        to="dfirtrack_main.tag",
                    ),
                ),
                (
                    "filter_system_list_case",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="filter_system_list_case",
                        to="dfirtrack_main.case",
                    ),
                ),
                (
                    "filter_system_list_tag",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="filter_system_list_tag",
                        to="dfirtrack_main.tag",
                    ),
                ),
            ],
        ),
    ]
