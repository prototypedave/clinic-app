from .register import RegisterPatient
from .emergencyForm import EmergencyRecordView
from .schedule import SchedulePatientView
from .disease import DiseaseRecordView

__all__ = [
    "RegisterPatient",
    "EmergencyRecordView",
    "SchedulePatientView",
    "DiseaseRecordView",
]