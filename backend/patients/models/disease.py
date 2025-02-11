from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models import Q


class DiseaseManagementRecord(models.Model):
    diagnosis = models.CharField(_('Diagnosis'), null=False, blank=False)
    dod = models.DateField(_('Date of Diagnosis'))
    smoking = models.TextField(_('Smoking Status'), null=True, blank=True)
    severity = models.CharField(_('Severity of the Disease'), null=False, blank=False)
    alcohol = models.TextField(_('Alcohol Status'), null=True, blank=True)
    physical = models.TextField(_('Physical Activities'), null=True, blank=True)
    diet = models.TextField(_('Diet'), null=True, blank=True)