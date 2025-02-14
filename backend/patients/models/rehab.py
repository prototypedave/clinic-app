from django.db import models
from django.utils.translation import gettext_lazy as _

class RehabilitationRecord(models.Model):
    diagnosis = models.CharField(_('Diagnosis'), max_length=50, null=False, blank=False)
    injury_date = models.DateField(_('Onset'))
    injury_type = models.CharField(_('Condition of INJURY'), max_length=100, null=False, blank=False)
 