# Generated by Django 2.0 on 2018-02-05 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_platform', '0029_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task_management',
            name='create_time',
            field=models.DateTimeField(),
        ),
    ]
