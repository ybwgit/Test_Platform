# Generated by Django 2.0 on 2018-03-09 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_platform', '0034_pad_pesourcelist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pad_pesourcelist',
            old_name='course_code',
            new_name='courseCode',
        ),
    ]
