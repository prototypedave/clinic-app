# Generated by Django 4.2.16 on 2025-01-28 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0006_medicine_administration_medicine_strength_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='medicine',
            options={'verbose_name': 'medicine', 'verbose_name_plural': 'medicines'},
        ),
    ]
