from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models import Q
from users.models.Users import User


class Expense(models.Model):
    creation_time = models.DateTimeField(auto_now=True)
    purpose = models.CharField(_("purpose"), blank=False)
    amount = models.FloatField(_("amount"), null=False, blank=False)
    notes = models.CharField(_("notes"), blank=True)
    date = models.DateField(_("date"), blank=False, null=True)
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reported_by', null=True, blank=False)

    class Meta:
        verbose_name = _('expense')
        verbose_name_plural = _('expenses')