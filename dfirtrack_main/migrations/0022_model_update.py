from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dfirtrack_main', '0021_entry_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysisstatus',
            name='analysisstatus_name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='case_id_external',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='case_name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_email',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_phone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='division',
            name='division_name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='dnsname',
            name='dnsname_name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='domain',
            name='domain_name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='domainuser',
            name='domainuser_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='entry',
            name='entry_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='headline',
            name='headline_name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='location_name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='note_title',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='notestatus',
            name='notestatus_name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='os',
            name='os_name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='osarch',
            name='osarch_name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='osimportname',
            name='osimportname_importer',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='osimportname',
            name='osimportname_name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='reason',
            name='reason_name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='recommendation_name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='reportitem',
            name='reportitem_subheadline',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='serviceprovider',
            name='serviceprovider_name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='system',
            name='system_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='systemhistory',
            name='systemhistory_new_value',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='systemhistory',
            name='systemhistory_old_value',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='systemhistory',
            name='systemhistory_type',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='systemstatus',
            name='systemstatus_name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='systemtype',
            name='systemtype_name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='systemuser',
            name='systemuser_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag_name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='taskname',
            name='taskname_name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='taskpriority',
            name='taskpriority_name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='taskstatus',
            name='taskstatus_name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
