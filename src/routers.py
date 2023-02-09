from fastapi import APIRouter

from src.area.endpoint import area_router
from src.field.endpoint import fields_router
from src.lu.endpoint import lu_router
from src.ngo.endpoint import ngo_router
from src.ngp.endpoint import ngp_router
from src.ngr.endpoint import ngr_router
from src.well.endpoint import well_router

api_router = APIRouter(prefix='/api/v1')


@api_router.get("/health", description="Health Check", tags=["Health Check"])
def ping():
    """Health check."""
    return {"msg": "pong!"}



api_router.include_router(ngp_router, prefix="/ngp", tags=["НГ Провинции"])  #
api_router.include_router(ngo_router, prefix="/ngo", tags=["НГ Области"])  #
api_router.include_router(ngr_router, prefix="/ngr", tags=["НГ Районы"])  #
api_router.include_router(fields_router, prefix="/fields", tags=["Месторождения"])  #
api_router.include_router(lu_router, prefix="/lu", tags=["Лицензионные участки"])  #
api_router.include_router(area_router, prefix="/area", tags=["Площади"])  #
api_router.include_router(well_router, prefix="/well", tags=["Скважины"])  #