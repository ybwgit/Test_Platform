# Generated by Django 2.0 on 2018-01-27 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_platform', '0023_auto_20180126_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='my_case_of_api',
            name='module_name',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
