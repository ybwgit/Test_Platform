# Generated by Django 2.0 on 2018-01-18 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_platform', '0005_my_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='devices_phone',
            name='used',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
