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
    
    def categorize_by_supplier(self, name):
        """
            Returns all medicines supplied by given supplier
        """
        return self.objects.filter(supplier=name)
    
    def get_batch_number_of_given_medicine(self, name, **kwargs):
        """
            Returns the batch number of the given medicine that is almost expired
            Arguments:
            - name (required): Medicine name
            - kwargs (optional): Additional fields such as manufacturer, strength, form to help in refine.
        """
        filters = {'name': name}
        filters.update(kwargs)  # if additional fields are provided in the form key: value

        # filter medicine
        medicine = self.filter(**filters).order_by('expiry_date') # almost expired first
        if medicine.exists():
            return medicine.first().batch_number
        return None
    
    def get_medicine_by_route_of_administration(self, route):
        """
            Returns all medicines that are administered in the given route
        """
        return self.objects.filter(administration=route)
    
    def get_medicine_by_type(self, type):
        """
            Returns all medicines that matches the given type
        """
        return self.objects.filter(Q(type__contains=type))


class Medicine(models.Model):
    name = models.CharField(_('Medicine Name'), blank=False, null=False, max_length=50)
    batch_number = models.CharField(_('Batch Number'), unique=True)
    expiry_date = models.DateField(_('Expiry Date'), blank=False, null=False)
    quantity = models.PositiveIntegerField(_('Quantity'), blank=False, null=False, default=0)
    cost = models.FloatField(_('Unit Cost'), blank=False, null=False, default=0.0)
    price = models.FloatField(_('Price'), blank=False, default=0.0, null=False)
    type = models.JSONField(_('Medicine class'), blank=False, null=False)
    administration = models.CharField(_('Intake Route'), blank=False, null=False)
    strength = models.PositiveBigIntegerField(_('Dose Strength'), blank=False, null=False)
    manufacturer = models.CharField(_('Manufacturer'), max_length=50, blank=False, null=False)
    supplier = models.CharField(_('Supplier'), max_length=50, blank=False, null=False)
    updated_date = models.DateTimeField(auto_now=True)

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
    
    def get_manufacturer(self):
        """ Returns the manufacturers name """
        return self.manufacturer
    
    def get_supplier(self):
        """ Returns the supplier of this given medicine """
        return self.supplier
    
    def get_price(self, qty):
        """ Returns the total price of selling the medicine """
        return self.price * qty
    
    def get_profit(self, qty):
        """ Returns the profit earned from selling the medicine """
        exp = self.price - self.cost  # assuming price will always be higher
        return exp * qty
    

