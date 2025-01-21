# Generated by Django 4.2.16 on 2025-01-21 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Medicine Name')),
                ('manufacturer', models.CharField(max_length=100, verbose_name='Manufacturer')),
                ('category', models.CharField(max_length=50, verbose_name='Category')),
                ('dosage_quantity', models.IntegerField(verbose_name='Dosage Quantity')),
                ('strength', models.CharField(max_length=50, verbose_name='Strength')),
                ('dosage_form', models.CharField(max_length=50, verbose_name='Dosage Form')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Medicine',
                'verbose_name_plural': 'Medicines',
                'unique_together': {('name', 'manufacturer', 'category', 'dosage_quantity', 'strength', 'dosage_form')},
            },
        ),
        migrations.CreateModel(
            name='MedicineHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Medicine Name')),
                ('manufacturer', models.CharField(max_length=100, verbose_name='Manufacturer')),
                ('category', models.CharField(max_length=50, verbose_name='Category')),
                ('dosage_quantity', models.IntegerField(verbose_name='Dosage Quantity')),
                ('strength', models.CharField(max_length=50, verbose_name='Strength')),
                ('dosage_form', models.CharField(max_length=50, verbose_name='Dosage Form')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Price')),
                ('stock', models.IntegerField(blank=True, null=True, verbose_name='Stock')),
                ('expiry_date', models.DateField(blank=True, null=True, verbose_name='Expiry Date')),
                ('received_date', models.DateField(blank=True, null=True, verbose_name='Received Date')),
                ('ordered_date', models.DateField(blank=True, null=True, verbose_name='Ordered Date')),
                ('buy_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Buy Price')),
                ('recorded_at', models.DateTimeField(auto_now_add=True)),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history', to='medicine.medicine')),
            ],
            options={
                'verbose_name': 'Medicine History',
                'verbose_name_plural': 'Medicine Histories',
                'ordering': ['-recorded_at'],
            },
        ),
    ]
