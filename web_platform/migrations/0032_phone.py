# Generated by Django 2.0 on 2018-02-27 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_platform', '0031_auto_20180205_1834'),
    ]

    operations = [
        migrations.CreateModel(
            name='phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_code', models.CharField(max_length=30)),
            ],
        ),
    ]
