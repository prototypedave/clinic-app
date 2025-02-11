from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models import Q


class MaternityCareRecord(models.Model):
    edd = models.DateField(_('Estimated Delivery Date'), null=False, blank=False)
    gravidity = models.IntegerField(_('Number of total pregnancie'), null=True, blank=True)
    parity = models.IntegerField(_('Number of previous deliveries'), null=True, blank=True)
    lmp = models.DateField(_('Last Menstral Period'), null=False, blank=False)
    ppc = models.TextField(_('Previous Pregnancy Complications'), null=True, blank=True)
    pbc = models.TextField(_('Previous Birth Complications'), null=True, blank=True)
    place_of_birth = models.CharField(_('Preferred Place of Birth'), null=True, blank=True)
    pain_management = models.CharField(_('Preferred Pain Management'), null=True, blank=True)