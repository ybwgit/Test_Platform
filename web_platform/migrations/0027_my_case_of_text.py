# Generated by Django 2.0 on 2018-01-29 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_platform', '0026_auto_20180127_1510'),
    ]

    operations = [
        migrations.CreateModel(
            name='my_case_of_text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=300)),
                ('module_name', models.CharField(max_length=300)),
                ('case_name', models.CharField(max_length=1000)),
                ('operation_steps', models.CharField(max_length=2550)),
                ('expected_results', models.CharField(max_length=2550)),
                ('remarks', models.CharField(max_length=2550)),
                ('App_version', models.CharField(max_length=255)),
                ('script_type', models.CharField(max_length=300)),
                ('script_address', models.CharField(max_length=300)),
            ],
        ),
    ]