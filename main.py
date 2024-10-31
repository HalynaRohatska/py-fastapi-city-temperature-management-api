from fastapi import FastAPI

from city import router as city_router
from temperature import router as temperature_router


app = FastAPI()

app.include_router(city_router.router, tags=["cities"])
app.include_router(temperature_router.router, tags=["temperatures"])
