from django.db import models
from django.utils.translation import gettext_lazy as _

class Medicine(models.Model):
    name = models.CharField(_('Medicine Name'), max_length=100)
    manufacturer = models.CharField(_('Manufacturer'), max_length=100)
    category = models.CharField(_('Category'), max_length=50)
    dosage_quantity = models.IntegerField(_('Dosage Quantity'))
    strength = models.CharField(_('Strength'), max_length=50)
    dosage_form = models.CharField(_('Dosage Form'), max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    update thid

    class Meta:
        verbose_name = _('Medicine')
        verbose_name_plural = _('Medicines')
        unique_together = (
            'name', 'manufacturer', 'category', 'dosage_quantity', 'strength', 'dosage_form'
        )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        MedicineHistory.objects.create(
            medicine=self,
            **{field.name: getattr(self, field.name) for field in self._meta.fields if field.name != 'id'}
        )

class MedicineHistory(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, related_name='history')
    name = models.CharField(_('Medicine Name'), max_length=100)
    manufacturer = models.CharField(_('Manufacturer'), max_length=100)
    category = models.JSONField(_('Category'), default=list)
    quantity = models.IntegerField(_('Quantity'))
    strength = models.CharField(_('Strength'), max_length=50)
    dosage_form = models.CharField(_('Dosage Form'), max_length=50)
    price = models.DecimalField(_('Price'), max_digits=10, decimal_places=2, null=True, blank=True)
    stock = models.IntegerField(_('Stock'), null=True, blank=True)
    expiry_date = models.DateField(_('Expiry Date'), null=True, blank=True)
    received_date = models.DateField(_('Received Date'), null=True, blank=True)
    ordered_date = models.DateField(_('Ordered Date'), null=True, blank=True)
    buy_price = models.DecimalField(_('Buy Price'), max_digits=10, decimal_places=2, null=True, blank=True)

    recorded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Medicine History')
        verbose_name_plural = _('Medicine Histories')
        ordering = ['-recorded_at']
