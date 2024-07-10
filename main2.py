from sqlalchemy import create_engine, Column, Integer, String, DateTime, select, extract, func
from datetime import datetime
from sqlalchemy.orm import sessionmaker, declarative_base
from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import uvicorn
import psycopg2
import openpyxl

data_start = '2024-05-03 15:00:00'
data_end = '2024-05-03 17:00:00'
data = data_start[:10]
cab = '1414'
DATABASE_URL = "postgresql+psycopg2://postgres:aaaaaa@localhost/test_data"  # подставить свои параметры
conn = psycopg2.connect(
    dbname='test_data',
    user='postgres',
    password='aaaaaa',
    host='127.0.0.1'
)
cur = conn.cursor()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

app = FastAPI()

templates = Jinja2Templates(directory="templates")

insert_query = """
    INSERT INTO table_ml(
        "Cabinet",
        "ML_Time_Start",
        "ML_Time_End",
        "Data"
    ) VALUES (%s, %s, %s, %s);

"""

cur.execute(insert_query, (cab, data_start, data_end, data))
conn.commit()
#cur.close()
#conn.close()
class MyTable(Base):
    __tablename__ = "test_table"
    PLANNING_ID = Column(Integer, primary_key=True, index=True)
    DoctorName = Column(String, index=True)
    PlanningDate = Column(DateTime, index=True)
    PlanningDateTimeStart = Column(DateTime, index=True)
    PlanningDateTimeEnd = Column(DateTime, index=True)
    SlotMinutes = Column(Integer)
    Comment = Column(String)
    PatientArrived = Column(Integer)
    ArriveDateTime = Column(DateTime)
    PATIENTS_ID = Column(Integer)
    SPECIALISATION_ID = Column(Integer)
    DoctorSpecialty = Column(String)
    FM_SERV_ID = Column(Integer)
    ServiceCode = Column(String)
    ServiceName = Column(String)
    FM_ORG_ID = Column(Integer)
    ClinicName = Column(String)
    CabinetName = Column(Integer, index=True)
    WebName = Column(Integer)

class table_ML(Base):
    __tablename__ = 'table_ml'
    Cabinet = Column(Integer, primary_key=True)
    ML_Time_Start = Column(DateTime, index=True)
    ML_Time_End = Column(DateTime, index=True)
    Data = Column(DateTime)
    Warn = Column(String)
Base.metadata.create_all(bind=engine)


'''@app.get("/", response_class=HTMLResponse)
def read_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})'''




@app.get("/ml-out", response_class=HTMLResponse)
def ml_output(request: Request):
    session = SessionLocal()
    try:
        query = select(MyTable).join(
            table_ML,
            MyTable.CabinetName == table_ML.Cabinet
        ).filter(
            MyTable.PlanningDate == table_ML.Data,
            extract('hour', MyTable.PlanningDateTimeStart) == extract('hour', table_ML.ML_Time_Start)
        )
        result = session.execute(query).first()
        if result and session.query(MyTable).filter(MyTable.PatientArrived)!=0:
            message = 'OK'
        else:
            message = 'Failed'
            fail_query = """
            INSERT INTO table_ml(
                "WARN"
            ) VALUES(%s);
            
            """

            cur.execute(fail_query, message)
            conn.commit()


        return templates.TemplateResponse("result.html", {"request": request, "message": message})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        session.close()

if __name__ == "__main__":
    uvicorn.run('main2:app')
