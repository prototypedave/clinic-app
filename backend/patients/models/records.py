from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models import Q
from .patient import Patient
from .dependant import PatientDependant
from .disease import DiseaseManagementRecord
from .maternity import MaternityCareRecord
from .rehab import RehabilitationRecord


class PatientRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='patient', null=True, blank=True)
    dependant = models.ForeignKey(PatientDependant, on_delete=models.CASCADE, related_name='dependant', null=True, blank=True)
    management = models.ForeignKey(DiseaseManagementRecord, on_delete=models.CASCADE, related_name='management', null=True, blank=True)
    maternity = models.ForeignKey(MaternityCareRecord, on_delete=models.CASCADE, related_name='maternity', null=True, blank=True)
    injuries = models.ForeignKey(RehabilitationRecord, on_delete=models.CASCADE, related_name='injuries', null=True, blank=True)
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
    
