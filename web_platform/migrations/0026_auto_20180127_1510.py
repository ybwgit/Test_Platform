# Generated by Django 2.0 on 2018-01-27 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_platform', '0025_my_case_of_api_app_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='my_report',
            name='uuid',
            field=models.CharField(max_length=100),
        ),
    ]
