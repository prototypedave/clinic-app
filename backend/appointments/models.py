from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models import Q

class Appointments(models.Model):
    start = models.DateTimeField(_('start time'), null=False, blank=False)
    end = models.DateTimeField(_('end time'), null=False, blank=False)
    title = models.CharField(_('title'), max_length=50, blank=False)
    creation_time = models.DateTimeField(auto_now=True)
    attended = models.BooleanField(_('attended'), default=False)
    reason = models.CharField(_('description'), blank=True)
    patientId = models.CharField(_('patient detail'), blank=True)
    missed = models.BooleanField(_('missed'), default=False)
    missed_reason = models.CharField(_('reason for missed appointment'), blank=True)
    reschedule_reason = models.CharField(_('reason for reschedule'), blank=True)

    class Meta:
        verbose_name = _('appointment')
        verbose_name_plural = _('appointments')

    @classmethod
    def get_upcoming_appointments(cls):
        # Retrieve all records where 'attended' is False and missed is false
        appointments = cls.objects.filter(Q(attended=False) and Q(missed=False))
        return [{
            'id': appointment.pk,
            'start': appointment.start,
            'end': appointment.end,
            'title': appointment.title,
            'calendarId' : appointment.patientId,
        } for appointment in appointments]
    
    @classmethod
    def get_missed_appointments(cls):
        appointments = cls.objects.filter(missed=True)
        return [{
            'id': appointment.pk,
            'start': appointment.start,
            'end': appointment.end,
            'title': appointment.title,
            'calendarId' : appointment.patientId,
        } for appointment in appointments]
    
    @classmethod
    def get_all_appointments(cls):
        appointments = cls.objects.all()
        return [{
            'id': appointment.pk,
            'start': appointment.start,
            'end': appointment.end,
            'title': appointment.title,
            'calendarId' : appointment.patientId,
        } for appointment in appointments]
    

    def get_reason(self):
        # returns missed reason for a given appointment
        return self.missed_reason