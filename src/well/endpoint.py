from typing import List

from fastapi import APIRouter
from starlette.responses import JSONResponse

from src.schemas import s_well
# from src.models import WELL
from src.well.services import well_reload, well_get_all, well_get_all_count, well_get_geojson_file

# from src.ngo.services import ngo_reload, ngo_get_all, ngo_get_all_count, ngo_get_geojson_file


well_router = APIRouter()


@well_router.get(path='/',
                 status_code=200,
                 response_model=List[s_well],
                 name='Получить список скважин',
                 tags=['Скважины'],
                 description='Получает список Скважин и координаты')
async def ngo_get():
    content = await well_get_all()
    return content


@well_router.get(path='/count',
                 status_code=200,
                 name='Получить Скважины',
                 tags=['Скважины'],
                 description='Получает количество Скважин')
async def ngo_get_count():
    content = await well_get_all_count()
    return content


#

@well_router.get(path='/reload',
                 status_code=200,
                 name='Обновить список Скважин',
                 tags=['Скважины'],
                 description='Загружает список Скважин из GeoJSON (файла или сервиса)')
async def ngo_reload_get():
    content_json = await well_reload()
    return JSONResponse(content=content_json)


@well_router.get(path='/geojson',
                 status_code=200,
                 name='Получить файл в формате GeoJSON',
                 tags=['Скважины'],
                 description='Получить файл в формате GeoJSON')
async def ngo_get_geojson():
    content_json = await well_get_geojson_file()
    return JSONResponse(content=content_json)
