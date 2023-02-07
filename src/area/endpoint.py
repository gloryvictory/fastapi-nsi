from typing import List

from fastapi import APIRouter
from starlette.responses import JSONResponse

from src.area.services import area_reload
from src.schemas import s_area
# from src.ngo.services import area_reload, area_get_all, area_get_all_count, area_get_geojson_file

# from src.apps.field.services import area_reload, area_get_all, area_get_geojson_file, area_get_all_count

area_router = APIRouter()


@area_router.get(path='/reload',
                 status_code=200,
                 name='Обновить список Площадей',
                 tags=['Площади'],
                 description='Загружает список Площадей и координаты центров из GeoJSON (файла или сервиса)')
async def area_reload_get():
    # return JSONResponse(content={"msg": "area"})
    content_json =  await area_reload()
    return JSONResponse(content=content_json)


@area_router.get(path='/',
                 status_code=200,
                 response_model=List[s_area],
                 name='Получить список Площадей',
                 tags=['Площади'],
                 description='Получает список Площадей и координаты центров')
async def area_get():
    # content = await area_get_all()
    # return content
    return JSONResponse(content={"msg": "area"})


@area_router.get(path='/count',
                 status_code=200,
                 name='Получить количество Площадей',
                 tags=['Площади'],
                 description='Получает количество Площадей')
async def area_get_count():
    # content = await area_get_all_count()
    # return content
    return JSONResponse(content={"msg": "area"})


# @area_router.get(path='/geojson',
#                  status_code=200,
#                  name='Получить файл в формате GeoJSON',
#                  tags=['Площади'],
#                  description='Получить файл в формате GeoJSON')
# async def area_get_geojson():
#     # content_json = await area_get_geojson_file()
#     # return JSONResponse(content=content_json)
#     return JSONResponse(content={"msg": "area"})
