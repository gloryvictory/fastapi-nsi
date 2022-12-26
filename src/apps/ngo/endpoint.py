from typing import List

from fastapi import APIRouter
from starlette.responses import JSONResponse

from src.apps.ngo.schemas import  NGO
from src.apps.ngo.services import ngo_reload, ngo_get_all, ngo_get_all_count, ngo_get_geojson_file

# from src.apps.fileds.services import ngo_reload, ngo_get_all, ngo_get_geojson_file, ngo_get_all_count

ngo_router = APIRouter()

@ngo_router.get(path='/reload',
                   status_code=200,
                   name='Обновить список НГ Областей',
                   tags=['НГ Области'],
                   description='Загружает список НГ Областей и координаты центров из GeoJSON (файла или сервиса)')
async def ngo_reload_get():
    content_json =  await ngo_reload()
    return JSONResponse(content=content_json)




@ngo_router.get(path='/',
                   status_code=200,
                   response_model=List[NGO],
                   name='Получить список НГ Областей',
                   tags=['НГ Области'],
                   description='Получает список НГ Областей и координаты центров')
async def ngo_get():
    content = await ngo_get_all()
    return content


@ngo_router.get(path='/count',
                   status_code=200,
                   name='Получить количество НГ Областей',
                   tags=['НГ Области'],
                   description='Получает количество НГ Областей')
async def ngo_get_count():
    content = await ngo_get_all_count()
    return content


@ngo_router.get(path='/geojson',
                   status_code=200,
                   name='Получить файл в формате GeoJSON',
                   tags=['НГ Области'],
                   description='Получить файл в формате GeoJSON')
async def ngo_get_geojson():
    content_json = await ngo_get_geojson_file()
    return JSONResponse(content=content_json)
