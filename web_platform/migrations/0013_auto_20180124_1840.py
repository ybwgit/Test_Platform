# Generated by Django 2.0 on 2018-01-24 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_platform', '0012_course_subject_show_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='my_report',
            name='App_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='my_report',
            name='terminal_number',
            field=models.CharField(default=22, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='my_report',
            name='test_type',
            field=models.CharField(default=23, max_length=30),
            preserve_default=False,
        ),
    ]
