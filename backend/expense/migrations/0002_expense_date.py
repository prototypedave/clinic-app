# Generated by Django 4.2.16 on 2025-01-21 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='date',
            field=models.DateField(null=True, verbose_name='date'),
        ),
    ]
