# Generated by Django 2.0 on 2018-03-05 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_platform', '0032_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='subject_total',
            field=models.CharField(default=36, max_length=30),
            preserve_default=False,
        ),
    ]
