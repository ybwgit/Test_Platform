# Generated by Django 2.0 on 2018-01-27 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_platform', '0024_my_case_of_api_module_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='my_case_of_api',
            name='App_version',
            field=models.CharField(default=4.0, max_length=255),
            preserve_default=False,
        ),
    ]
