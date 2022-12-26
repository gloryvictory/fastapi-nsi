from typing import List

from fastapi import APIRouter
from starlette.responses import JSONResponse

from src.apps.ngp.schemas import NGP
from src.apps.ngp.services import ngp_reload, ngp_get_all, ngp_get_all_count, ngp_get_geojson_file

# from src.apps.fileds.services import ngp_reload, ngp_get_all, ngp_get_geojson_file, ngp_get_all_count

ngp_router = APIRouter()

@ngp_router.get(path='/reload',
                   status_code=200,
                   name='Обновить список НГ Провинций',
                   tags=['НГ Провинции'],
                   description='Загружает список НГ Провинций и координаты центров из GeoJSON (файла или сервиса)')
async def ngp_reload_get():
    content_json =  await ngp_reload()
    return JSONResponse(content=content_json)




@ngp_router.get(path='/',
                   status_code=200,
                   response_model=List[NGP],
                   name='Получить список НГ Провинций',
                   tags=['НГ Провинции'],
                   description='Получает список НГ Провинций и координаты центров')
async def ngp_get():
    content = await ngp_get_all()
    # print(content)
    return content


@ngp_router.get(path='/count',
                   status_code=200,
                   name='Получить количество НГ Провинций',
                   tags=['НГ Провинции'],
                   description='Получает количество НГ Провинций')
async def ngp_get_count():
    content = await ngp_get_all_count()
    return content


@ngp_router.get(path='/geojson',
                   status_code=200,
                   name='Получить файл в формате GeoJSON',
                   tags=['НГ Провинции'],
                   description='Получить файл в формате GeoJSON')
async def ngp_get_geojson():
    # content_json = await ngp_reload()
    content_json = await ngp_get_geojson_file()
    return JSONResponse(content=content_json)
