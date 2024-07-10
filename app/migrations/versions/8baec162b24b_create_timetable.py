"""create timetable

Revision ID: 8baec162b24b
Revises: 25683106dec2
Create Date: 2024-07-10 12:43:00.420871

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8baec162b24b'
down_revision: Union[str, None] = '25683106dec2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "timetable",
        sa.Column("id", sa.CHAR(32), nullable=False),
        sa.Column("PLANNING_ID", sa.Integer(), nullable=True),
        sa.Column("DoctorName", sa.String(length=1000), nullable=True),
        sa.Column("PlanningDate", sa.DateTime(), nullable=True),
        sa.Column("PlanningDateTimeStart", sa.DateTime(), nullable=True),
        sa.Column("PlanningDateTimeEnd", sa.DateTime(), nullable=True),
        sa.Column("SlotMinutes", sa.Integer(), nullable=True),
        sa.Column("Comment", sa.String(length=1000), nullable=True),
        sa.Column("PatientArrived", sa.Integer(), nullable=False),
        sa.Column("ArriveDateTime", sa.DateTime(), nullable=True),
        sa.Column("PATIENTS_ID", sa.Integer(), nullable=True),
        sa.Column("SPECIALISATION_ID", sa.Integer(), nullable=True),
        sa.Column("DoctorSpecialty", sa.String(length=1000), nullable=True),
        sa.Column("FM_SERV_ID", sa.Integer(), nullable=True),
        sa.Column("ServiceCode", sa.String(length=1000), nullable=True),
        sa.Column("ServiceName", sa.String(length=1000), nullable=True),
        sa.Column("FM_ORG_ID", sa.Integer(), nullable=True),
        sa.Column("ClinicName", sa.String(length=1000), nullable=True),
        sa.Column("CabinetName", sa.Integer(), nullable=True),
        sa.Column("WebName", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("timetable")
