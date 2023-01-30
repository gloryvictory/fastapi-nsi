from typing import List

from fastapi import APIRouter
from starlette.responses import JSONResponse

from src.schemas import s_lu
from src.lu.services import lu_reload, lu_get_all, lu_get_all_count, lu_get_geojson_file

# from src.apps.field.services import lu_reload, lu_get_all, lu_get_geojson_file, lu_get_all_count

lu_router = APIRouter()

@lu_router.get(path='/reload',
                   status_code=200,
                   name='Обновить список Лицензионных участков',
                   tags=['Лицензионные участки'],
                   description='Загружает список Лицензионных участков и координаты центров из GeoJSON (файла или сервиса)')
async def lu_reload_get():
    content_json = await lu_reload()
    return JSONResponse(content=content_json)




@lu_router.get(path='/',
                   status_code=200,
                   response_model=List[s_lu],
                   name='Получить список Лицензионных участков',
                   tags=['Лицензионные участки'],
                   description='Получает список Лицензионных участков и координаты центров')
async def lu_get():
    content = await lu_get_all()
    # print(content)
    return content


@lu_router.get(path='/count',
                   status_code=200,
                   name='Получить количество Лицензионных участков',
                   tags=['Лицензионные участки'],
                   description='Получает количество Лицензионных участков')
async def lu_get_count():
    content = await lu_get_all_count()
    return content


@lu_router.get(path='/geojson',
                   status_code=200,
                   name='Получить файл в формате GeoJSON',
                   tags=['Лицензионные участки'],
                   description='Получить файл в формате GeoJSON')
async def lu_get_geojson():
    # content_json = await lu_reload()
    content_json = await lu_get_geojson_file()
    return JSONResponse(content=content_json)
