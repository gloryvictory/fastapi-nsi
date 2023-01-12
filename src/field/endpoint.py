from typing import List

from fastapi import APIRouter
from starlette.responses import JSONResponse

from src.schemas import Field
from .services import fields_reload, fields_get_all, fields_get_geojson_file, fields_get_all_count

fields_router = APIRouter()


@fields_router.get(path='/',
                   status_code=200,
                   response_model=List[Field],
                   name='Получить список Месторождений',
                   tags=['Месторождения'],
                   description='Получает список месторождений и координаты центров')
async def fields_get():
    content = await fields_get_all()
    # print(content)
    return content


@fields_router.get(path='/count',
                   status_code=200,
                   name='Получить количество Месторождений',
                   tags=['Месторождения'],
                   description='Получает количество месторождений')
async def fields_get_count():
    content = await fields_get_all_count()
    return content


@fields_router.get(path='/reload',
                   status_code=200,
                   name='Обновить список Месторождений',
                   tags=['Месторождения'],
                   description='Загружает список месторождений и координаты центров из GeoJSON (файла или сервиса)')
async def fields_reload_get():
    content_json = await fields_reload()
    return JSONResponse(content=content_json)


#
@fields_router.get(path='/geojson',
                   status_code=200,
                   name='Получить файл в формате GeoJSON',
                   tags=['Месторождения'],
                   description='Получить файл в формате GeoJSON')
async def fields_get_geojson():
    # content_json = await fields_reload()
    content_json = await fields_get_geojson_file()
    return JSONResponse(content=content_json)
