# Generated by Django 4.2.1 on 2023-05-21 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_company_companyworker_delete_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companyworker',
            name='company',
        ),
        migrations.RemoveField(
            model_name='companyworker',
            name='person',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='CompanyWorker',
        ),
    ]
