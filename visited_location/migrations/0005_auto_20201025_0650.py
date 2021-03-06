# Generated by Django 3.1.2 on 2020-10-25 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('case_record', '0003_auto_20201024_1700'),
        ('visited_location', '0004_visitedlocation_case_record'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locNameEN', models.CharField(max_length=100)),
                ('locAddressEN', models.CharField(max_length=100)),
                ('locX', models.FloatField()),
                ('locY', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='VisitedLocationRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitedLocDateFrom', models.DateField()),
                ('visitedLocDateTo', models.DateField()),
                ('visitedLocCategory', models.CharField(max_length=50)),
                ('case_record', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='case_record.caserecord')),
            ],
        ),
        migrations.DeleteModel(
            name='VisitedLocation',
        ),
    ]
