from fastapi import APIRouter
from app.models import TableMl, TimeTable
from app.schemas import TableMLSchema, TimeTableSchema
from uuid import UUID

router = APIRouter()


@router.post("/create")
async def create(data: TableMLSchema):
    await TableMl.objects.create(**data.model_dump())
    return 1


@router.post("/create_time")
async def timtaable_create(data: TimeTableSchema):
    await TimeTable.objects.create(**data.model_dump())
    return 1


@router.get("/get/{cabinet}")
async def get_by_id(cabinet: int):
    list = await TableMl.objects.all(Cabinet=cabinet)
    return list
