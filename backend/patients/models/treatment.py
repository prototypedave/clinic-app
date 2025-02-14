from django.db import models
from django.utils.translation import gettext_lazy as _


class TreatmentPlanModel(models.Model):
    plan = models.TextField(_('Treatment Plan'), null=False, blank=False)
    diagnosis = models.TextField(_('Diagnosis'), null=False, blank=False)
    medication = models.JSONField(_('Prescription'), null=True, blank=True)