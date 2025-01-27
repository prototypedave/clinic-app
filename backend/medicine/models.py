from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import date, timedelta
from django.db.models import Q

class Medicine(models.Model):
    expiry_date = models.DateField(_('Expiry Date'), blank=False, null=False)
    batch_number = models.CharField(_('Batch Number'), unique=True)
    
    class Meta:
        verbose_name = _('medicine')
        verbose_name_plural = _('Medicine')
    
    def get_time_left_to_expiry(self):
        """ Returns number of days left till expiry """
        return (self.expiry_date - date.today()).days 
    
    @classmethod
    def get_quantity_of_expired_items(cls, num_days):
        """ Returns the number of medicine nearing expiry or have expired """
        today = date.today()
        items_count = cls.objects.filter(expiry_date__lte=today + timedelta(days=num_days)).count()
        return items_count
    
    @classmethod
    def get_medicine_expired_or_nearing_expiry(cls, num_days):
        """ Returns a list of medicine that are almost expired """
        today = date.today()
        almost_expired = cls.objects.filter(expiry_date__lte=today + timedelta(days=num_days))
        return almost_expired