from fastapi import APIRouter
from starlette.responses import JSONResponse

from src.apps.fileds.services import reload_fields

fields_router = APIRouter()

@fields_router.get('/')
async def get_category():
    return JSONResponse(status_code=200,
                        content={"message": " fields_router success"})
    # return await models.Category.objects.filter().all()


@fields_router.get('/reload')
async def get_reload():
    content_json = await reload_fields()
    return JSONResponse(status_code=200,
                        content=content_json)
#