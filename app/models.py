import ormar
from app.core.db import database, metadata
from uuid import UUID, uuid4
import datetime

base_ormar_config = ormar.OrmarConfig(
    database=database,
    metadata=metadata
)


class TableMl(ormar.Model):
    ormar_config = base_ormar_config.copy(tablename="table_ml")

    id: UUID = ormar.UUID(primary_key=True, default=uuid4)
    Cabinet: int = ormar.Integer(nullable=False)
    ML_Time_Start: datetime.time = ormar.Time(nullable=False)
    ML_Time_End: datetime.time = ormar.Time(nullable=False)
    Data: datetime.date = ormar.Date(nullable=False)


class TimeTable(ormar.Model):
    ormar_config = base_ormar_config.copy(tablename="timetable")

    id: UUID = ormar.UUID(primary_key=True, default=uuid4)
    PLANNING_ID: int = ormar.Integer(nullable=True)
    DoctorName: str = ormar.String(max_length=1000, nullable=True)
    PlanningDate: datetime.datetime = ormar.DateTime(nullable=True)
    PlanningDateTimeStart: datetime.datetime = ormar.DateTime(nullable=True)
    PlanningDateTimeEnd: datetime.datetime = ormar.DateTime(nullable=True)
    SlotMinutes: int = ormar.Integer(nullable=True)
    Comment: str = ormar.String(max_length=1000, nullable=True)
    PatientArrived: int = ormar.Integer(nullable=False)
    ArriveDateTime: datetime.datetime = ormar.DateTime(nullable=True)
    PATIENTS_ID: int = ormar.Integer(nullable=True)
    SPECIALISATION_ID: int = ormar.Integer(nullable=True)
    DoctorSpecialty: str = ormar.String(max_length=1000, nullable=True)
    FM_SERV_ID: int = ormar.Integer(nullable=True)
    ServiceCode: str = ormar.String(max_length=1000, nullable=True)
    ServiceName: str = ormar.String(max_length=1000, nullable=True)
    FM_ORG_ID: int = ormar.Integer(nullable=True)
    ClinicName: str = ormar.String(max_length=1000, nullable=True)
    CabinetName: int = ormar.Integer(nullable=True)
    WebName: int = ormar.Integer(nullable=True)
