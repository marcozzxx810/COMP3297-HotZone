# Generated by Django 3.1.2 on 2020-10-24 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('case_record', '0002_remove_caserecord_visitedloc'),
        ('visited_location', '0003_auto_20201024_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitedlocation',
            name='case_record',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='case_record.caserecord'),
        ),
    ]
