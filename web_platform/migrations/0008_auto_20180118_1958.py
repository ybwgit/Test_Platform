# Generated by Django 2.0 on 2018-01-18 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_platform', '0007_my_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='my_report',
            name='create_time',
            field=models.DateField(auto_now=True),
        ),
    ]
