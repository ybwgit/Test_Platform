# Generated by Django 2.0 on 2018-01-19 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_platform', '0010_course'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='course_name',
            new_name='name',
        ),
    ]