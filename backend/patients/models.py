from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import date, timedelta
from django.db.models import Q

class Patient(models.Model):
    first_name = models.CharField(_('First Name'), null=False, blank=False, max_length=30)
    middle_name = models.CharField(_('Second Name'), null=True, blank=True, max_length=30)
    last_name = models.CharField(_('Last Name'), null=False, blank=False, max_length=30)
    mobile = models.CharField(_('Telephone Number'), unique=True, null=False, blank=False)
    

    class Meta:
        verbose_name = _('patient')
        verbose_name_plural = _('patients')


class PatientRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='patient', null=True, blank=True)
    reason = models.CharField(_('Reason for visit'), null=False, blank=False)
    visit_date = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = _('records')
        verbose_name_plural = _('records')