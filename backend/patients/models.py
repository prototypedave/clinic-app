from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import date, timedelta
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


class DiseaseManagementRecord(models.Model):
    diagnosis = models.CharField(_('Diagnosis'), null=False, blank=False)
    dod = models.DateField(_('Date of Diagnosis'))
    smoking = models.TextField(_('Smoking Status'), null=True, blank=True)
    severity = models.CharField(_('Severity of the Disease'), null=False, blank=False)
    alcohol = models.TextField(_('Alcohol Status'), null=True, blank=True)
    physical = models.TextField(_('Physical Activities'), null=True, blank=True)
    diet = models.TextField(_('Diet'), null=True, blank=True)


class PatientRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='patient', null=True, blank=True)
    dependant = models.ForeignKey(PatientDependant, on_delete=models.CASCADE, related_name='dependant', null=True, blank=True)
    management = models.ForeignKey(DiseaseManagementRecord, on_delete=models.CASCADE, related_name='management')
    reason = models.TextField(_('Reason for visit'), null=False, blank=False)
    complaint = models.TextField(_('Chief Complaint'), null=True, blank=True)
    onset = models.TextField(_('Onset of Symptoms'), null=True, blank=True)
    location = models.TextField(_('Location of Symptoms'), null=True, blank=False)
    severity = models.TextField(_('Severity of the symptoms'), null=True, blank=True)
    character = models.TextField(_('Character of Pain/Symptoms'), null=True, blank=True)
    factors = models.TextField(_('Aggreviating factors'), null=True, blank=True)
    appointment = models.TextField(_('Reason for booking an appointment'), null=True, blank=True)
    visit_date = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=(
                    models.Q(patient__isnull=False) | models.Q(dependant__isnull=False)
                ),
                name='record_must_have_patient_or_dependant'
            ),
            models.CheckConstraint(
                check=(
                    ~models.Q(patient__isnull=False) | ~models.Q(dependant__isnull=False)
                ),
                name='record_cannot_have_both_patient_and_dependant'
            ),
        ]

    def __str__(self):
        if self.patient:
            return f"Record for Patient: {self.patient.get_patient_name()}"
        elif self.dependant:
            return f"Record for Dependant: {self.dependant.get_dependant_name()}"
        return "Unassigned Record"
    
    def get_patient(self):
        if self.patient:
            return {
                'patient': self.patient,
                'model' : 'patient',
            }
        elif self.dependant:
            return {
                'patient' : self.dependant,
                'model' : 'dependant',
            }
        return None
    

