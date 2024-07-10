"""create table

Revision ID: 25683106dec2
Revises: 
Create Date: 2024-07-10 12:29:29.334553

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '25683106dec2'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "table_ml",
        sa.Column("id", sa.CHAR(32), nullable=False),
        sa.Column("Cabinet", sa.Integer(), nullable=False),
        sa.Column("ML_Time_Start", sa.Time(), nullable=False),
        sa.Column("ML_Time_End", sa.Time(), nullable=False),
        sa.Column("Data", sa.Date(), nullable=False),
        sa.Column("Warn", sa.String(length=1000), nullable=True),
        sa.PrimaryKeyConstraint("id")
    )


def downgrade() -> None:
    op.drop_table("table_ml")
