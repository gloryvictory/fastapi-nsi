from typing import List

from fastapi import APIRouter
from starlette.responses import JSONResponse

from src.schemas import s_ngr
from src.ngr.services import ngr_reload, ngr_get_all, ngr_get_all_count, ngr_get_geojson_file

ngr_router = APIRouter()


@ngr_router.get(path='/reload',
                status_code=200,
                name='Обновить список НГ Районов',
                tags=['НГ Районы'],
                description='Загружает список НГ Районов и координаты центров из GeoJSON (файла или сервиса)')
async def ngr_reload_get():
    content_json = await ngr_reload()
    return JSONResponse(content=content_json)


@ngr_router.get(path='/',
                status_code=200,
                response_model=List[s_ngr],
                name='Получить список НГ Районов',
                tags=['НГ Районы'],
                description='Получает список НГ Районов и координаты центров')
async def ngr_get():
    content = await ngr_get_all()
    # print(content)
    return content


@ngr_router.get(path='/count',
                status_code=200,
                name='Получить количество НГ Районов',
                tags=['НГ Районы'],
                description='Получает количество НГ Районов')
async def ngr_get_count():
    content = await ngr_get_all_count()
    return content


@ngr_router.get(path='/geojson',
                status_code=200,
                name='Получить файл в формате GeoJSON',
                tags=['НГ Районы'],
                description='Получить файл в формате GeoJSON')
async def ngr_get_geojson():
    # content_json = await ngr_reload()
    content_json = await ngr_get_geojson_file()
    return JSONResponse(content=content_json)
