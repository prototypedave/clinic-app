from .dependant import DependantSerializer
from .disease import DiseaseManagementSerializer
from .maternity import MaternitySerializer
from .patient import PatientSerializer
from .records import RecordSerializer, EmergencyRecordSerializer, AppointmentRecordSerializer
from .rehab import RehabilitationSerializer
from .vitals import VitalSerializer
from .treatment import TreatmentPlanSerializer

__all__ = [
    "DependantSerializer",
    "DiseaseManagementSerializer",
    "MaternitySerializer",
    "PatientSerializer",
    "RecordSerializer",
    "RehabilitationSerializer",
    "EmergencyRecordSerializer",
    "AppointmentRecordSerializer",
    "VitalSerializer",
    "TreatmentPlanSerializer",
]