from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models import Q
from patient import Patient

class PatientDependant(models.Model):
    class GenderChoices(models.TextChoices):
        """ Ensures only this fields can be provided """
        MALE = 'M', _('Male')
        FEMALE = 'F', _('Female')

    guardian = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='parent', null=True, blank=True)
    first_name = models.CharField(_('First Name'), null=False, blank=False, max_length=30)
    last_name = models.CharField(_('Last Name'), null=False, blank=False, max_length=30)
    age = models.DateField(_('Date of Birth'), null=False, blank=False)
    gender = models.CharField(_('Sex'), max_length=1, choices=GenderChoices.choices, null=False, blank=False)

    class Meta:
        verbose_name = _('dependant')
        verbose_name_plural = _('dependants')

    def get_dependant_name(self):
        """ Returns patient's full name """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()
    
    def get_dependant_short_name(self):
        """ Returns only the first name of the patient """
        return self.first_name
    
    @classmethod
    def get_dependant_by_name(cls, name, alienId):
        """ First retrieves dependants using FK (guardian) then filters by full name """
        return cls.objects.filter(guardian_id=alienId).filter(
            first_name__iexact=name.split()[0],
            last_name__iexact=name.split()[1] if len(name.split()) > 1 else ""
        )
