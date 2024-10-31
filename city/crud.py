from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from city import models, schemas


async def post_city(db: AsyncSession, city_schema: schemas.CityCreate):
    city = models.City(
        name=city_schema.name,
        additional_info=city_schema.additional_info
    )
    db.add(city)
    await db.commit()
    await db.refresh(city)
    return city


async def get_all_cities(db: AsyncSession) -> list[models.City]:
    city_list = await db.execute(select(models.City))
    return [city[0] for city in city_list.fetchall()]


async def get_city_detail(db: AsyncSession, city_id: int) -> models.City | None:
    city = await db.execute(
        select(models.City).filter(models.City.id == city_id)
    )
    return city.scalars().first()


async def update_city(
    db: AsyncSession,
    city_id: int,
    city_schema: schemas.CityCreate
) -> models.City:
    result = await db.execute(
        select(models.City).filter(models.City.id == city_id)
    )
    city = result.scalars().first()
    if city:
        city.name = city_schema.name
        city.additional_info = city_schema.additional_info
        await db.commit()
        await db.refresh(city)
    return city


async def delete_city(
    db: AsyncSession,
    city_id: int
) -> bool:
    result = await db.execute(
        select(models.City).filter(models.City.id == city_id)
    )
    city = result.scalars().first()
    if city:
        await db.delete(city)
        await db.commit()
        return True
    return False
