# Generated by Django 4.2.16 on 2025-02-10 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0005_patientrecord_appointment'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiseaseManagementRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnosis', models.CharField(verbose_name='Diagnosis')),
                ('dod', models.DateField(verbose_name='Date of Diagnosis')),
                ('smoking', models.TextField(blank=True, null=True, verbose_name='Smoking Status')),
                ('severity', models.CharField(verbose_name='Severity of the Disease')),
                ('alcohol', models.TextField(blank=True, null=True, verbose_name='Alcohol Status')),
                ('physical', models.TextField(blank=True, null=True, verbose_name='Physical Activities')),
                ('diet', models.TextField(blank=True, null=True, verbose_name='Diet')),
            ],
        ),
        migrations.AddField(
            model_name='patientrecord',
            name='management',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='management', to='patients.diseasemanagementrecord'),
        ),
    ]
