# Generated by Django 4.2.3 on 2023-07-27 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0005_prescriptionmedicament'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='firstname',
            new_name='firs_name',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='lastname',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='lastname',
            new_name='last_name',
        ),
    ]