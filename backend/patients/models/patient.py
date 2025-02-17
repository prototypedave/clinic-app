from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models import Q

class PatientManager(models.Manager):
    def check_if_patient_exists(self, mobile):
        """ Returns the patient ID with the given mobile, if exists """
        try:
            patient = self.get(mobile=mobile)
            return patient.id
        except self.model.DoesNotExist:
            return None
    

class Patient(models.Model):
    class GenderChoices(models.TextChoices):
        """ Ensures only this fields can be provided """
        MALE = 'M', _('Male')
        FEMALE = 'F', _('Female')

    first_name = models.CharField(_('First Name'), null=False, blank=False, max_length=30)
    middle_name = models.CharField(_('Second Name'), null=True, blank=True, max_length=30)
    last_name = models.CharField(_('Last Name'), null=False, blank=False, max_length=30)
    mobile = models.CharField(_('Telephone Number'), unique=True, null=False, blank=False)
    age = models.DateField(_('Date of Birth'), null=False, blank=False)
    address = models.CharField(_('Patient Home Address'), null=True, blank=True, max_length=30)
    guardian = models.BooleanField(_('if parent'), null=False, blank=False, default=False)
    family_history = models.CharField(_('Family Illness'), null=True, blank=True)
    gender = models.CharField(_('Sex'), max_length=1, choices=GenderChoices.choices, null=False, blank=False)
    email = models.CharField(_('Email'), null=True, blank=True)
    
    objects =  PatientManager()

    class Meta:
        verbose_name = _('patient')
        verbose_name_plural = _('patients')

    def get_patient_name(self):
        """ Returns patient's full name """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()
    
    def get_patient_short_name(self):
        """ Returns only the first name of the patient """
        return self.first_name