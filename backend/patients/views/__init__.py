from .register import RegisterPatient
from .emergencyForm import EmergencyRecordView
from .schedule import SchedulePatientView
from .disease import DiseaseRecordView
from .maternityCare import MaternityCareRecordView
from .rehabilitation import RehabilitationRecordView
from .vitals import VitalsRecordView

__all__ = [
    "RegisterPatient",
    "EmergencyRecordView",
    "SchedulePatientView",
    "DiseaseRecordView",
    "MaternityCareRecordView",
    "RehabilitationRecordView",
    "VitalsRecordView",
]