# Generated by Django 2.0 on 2018-01-18 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_platform', '0006_devices_phone_used'),
    ]

    operations = [
        migrations.CreateModel(
            name='my_report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('report_data', models.CharField(max_length=3000)),
                ('report_result', models.CharField(max_length=30)),
                ('uuid', models.CharField(max_length=30)),
                ('create_time', models.TimeField()),
            ],
        ),
    ]