from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import date, timedelta
from django.db.models import Q

class MedicineManager(models.Manager):
    def almost_expired(self, num_days):
        """
            Returns all medicines that are almost expired from the given number of days
        """
        today = date.today()
        return self.objects.filter(expiry_date__lte=today + timedelta(days=num_days))
    
    def almost_finished(self, qty):
        """
            Returns all medicines that are finished or almost finished 
        """
        return self.objects.filter(quantity__lte=qty)


class Medicine(models.Model):
    expiry_date = models.DateField(_('Expiry Date'), blank=False, null=False)
    batch_number = models.CharField(_('Batch Number'), unique=True)
    quantity = models.PositiveIntegerField(_('Quantity'), blank=False, null=False, default=0)

    objects = MedicineManager()
    
    class Meta:
        verbose_name = _('medicine')
        verbose_name_plural = _('Medicine')
    
    def get_time_left_to_expiry(self):
        """ Returns number of days left till expiry """
        return (self.expiry_date - date.today()).days 
    
    def get_quantity_remaining(self):
        """ Returns given medicine quantity remaining """
        return self.quantity
    

