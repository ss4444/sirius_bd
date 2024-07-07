import ormar
from uuid import UUID, uuid4
from app.core.db import database, metadata


base_ormar_config = ormar.OrmarConfig(
    database=database,
    metadata=metadata
)


class Laboratory(ormar.Model):
    ormar_config = base_ormar_config.copy(tablename="laboratories")

    id: UUID = ormar.UUID(primary_key=True, default=uuid4)
    name: str = ormar.String(max_length=100, nullable=False)
