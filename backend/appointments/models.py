from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models import Q
from users.models.Users import User

class Appointments(models.Model):
    start = models.DateTimeField(_('start'), null=False, blank=False)
    end = models.DateTimeField(_('end'), null=False, blank=False)
    title = models.CharField(_('title'), max_length=50, blank=False)
    creation_time = models.DateTimeField(auto_now=True)
    attended = models.BooleanField(_('attended'), default=False)
    reason = models.CharField(_('reason'), blank=True)
    first_name = models.CharField(_('first name'), blank=True)
    middle_name = models.CharField(_('middle name'), blank=True)
    last_name = models.CharField(_('last name'), blank=True)
    missed = models.BooleanField(_('missed'), default=False)
    missed_reason = models.CharField(_('missed reason'), blank=True)
    reschedule_reason = models.CharField(_('reschedule reason'), blank=True)
    scheduled_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='scheduled_by', null=True, blank=True)
    follow_up_approach = models.CharField(_('Follow up approach'), blank=True)
    mobile = models.CharField(_('mobile'), default=False, blank=False, max_length=13)
    email = models.CharField(_('email'), blank=False, default=False, max_length=50)

    class Meta:
        verbose_name = _('appointment')
        verbose_name_plural = _('appointments')

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    @classmethod
    def get_upcoming_appointments(cls):
        # Retrieve all records where 'attended' is False and missed is false
        appointments = cls.objects.filter(Q(attended=False) and Q(missed=False))
        return [{
            'id': appointment.pk,
            'start': appointment.start.strftime('%Y-%m-%d %H:%M'),
            'end': appointment.end.strftime('%Y-%m-%d %H:%M'),
            'title': appointment.title,
            'calendarId' : 'patient',
        } for appointment in appointments]
    
    @classmethod
    def get_missed_appointments(cls):
        appointments = cls.objects.filter(missed=True)
        return [{
            'id': appointment.pk,
            'start': appointment.start.strftime('%Y-%m-%d %H:%M'),
            'end': appointment.end.strftime('%Y-%m-%d %H:%M'),
            'title': appointment.title,
            'calendarId' : 'patient',
        } for appointment in appointments]
    
    @classmethod
    def get_all_appointments(cls):
        appointments = cls.objects.all()
        return [{
            'id': appointment.pk,
            'start': appointment.start.strftime('%Y-%m-%d %H:%M'),
            'end': appointment.end.strftime('%Y-%m-%d %H:%M'),
            'title': appointment.title,
            'calendarId' : 'patient',
        } for appointment in appointments]
    

    def get_reason(self):
        # returns missed reason for a given appointment
        return self.missed_reason