from pydantic import BaseModel
import datetime


class TableMLSchema(BaseModel):
    Cabinet: int
    ML_Time_Start: datetime.time
    ML_Time_End: datetime.time
    Data: datetime.date


class TimeTableSchema(BaseModel):
    PLANNING_ID: int
    DoctorName: str
    PlanningDate: datetime.datetime = datetime.datetime.utcnow()
    PlanningDateTimeStart: datetime.datetime = datetime.datetime.utcnow()
    PlanningDateTimeEnd: datetime.datetime = datetime.datetime.utcnow()
    SlotMinutes: int
    Comment: str
    PatientArrived: int
    ArriveDateTime: datetime.datetime = datetime.datetime.utcnow()
    PATIENTS_ID: int
    SPECIALISATION_ID: int
    DoctorSpecialty: str
    FM_SERV_ID: int
    ServiceCode: str
    ServiceName: str
    FM_ORG_ID: int
    ClinicName: str
    CabinetName: int
    WebName: int
