from django.db import models
from django.utils.translation import gettext_lazy as _


class VitalsModel(models.Model):
    temperature = models.FloatField(_('temp'), null=False, blank=False)
    pulse = models.FloatField(_('Pulse'), null=True, blank=True)
    blood_pressure = models.CharField(_('bp'), null=True, blank=True)
    respiratory_rate = models.FloatField(_('RR'), null=True, blank=True)
    weight = models.FloatField(_('Weight'), null=True, blank=True)
    height = models.FloatField(_('Height'), null=True, blank=True)
    neurological = models.TextField(_('NA'), null=True, blank=True)
    respiratory = models.TextField(_('RA'), null=True, blank=True)
    cardiovascular = models.TextField(_('CA'), null=True, blank=True)
    gastrointestinal = models.TextField(_('GA'), null=True, blank=True)
    musculoskeleton = models.TextField(_('MA'), null=True, blank=True)
    skin = models.TextField(_('SA'), null=True, blank=True)
    pyschological = models.TextField(_('PA'), null=True, blank=True)
    pain = models.TextField(_('Pain Assessment'), null=True, blank=True)
    fall_risk = models.TextField(_('FR'), null=True, blank=True)