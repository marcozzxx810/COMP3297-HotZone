# Generated by Django 3.1.2 on 2020-10-24 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_auto_20201024_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='patientHKID',
            field=models.CharField(max_length=20),
        ),
    ]
