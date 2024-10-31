from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from dependencies import get_db
from temperature import crud, schemas

router = APIRouter()


@router.get("/temperatures/", response_model=list[schemas.Temperature])
async def get_temperatures(
    city_id: int | None = None,
    db: AsyncSession = Depends(get_db)
):
    return await crud.get_temperatures(city_id=city_id, db=db)


@router.post("/temperatures/update/", response_model=schemas.Temperature)
async def update_temperature(db: AsyncSession = Depends(get_db)):
    await crud.get_and_store_temperatures(db)
    return {"message": "Temperature data updated"}
