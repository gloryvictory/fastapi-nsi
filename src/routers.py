from fastapi import APIRouter

from src.field.endpoint import fields_router
from src.lu.endpoint import lu_router
from src.ngo.endpoint import ngo_router
from src.ngp.endpoint import ngp_router
from src.ngr.endpoint import ngr_router

api_router = APIRouter(prefix='/api/v1')


@api_router.get("/health", description="Health Check", tags=["Health Check"])
def ping():
    """Health check."""
    return {"msg": "pong!"}


api_router.include_router(fields_router, prefix="/fields", tags=["Месторождения"])  # , description='Месторождения'
api_router.include_router(ngp_router, prefix="/ngp", tags=["НГ Провинции"])  # , description=''
api_router.include_router(ngo_router, prefix="/ngo", tags=["НГ Области"])  # , description=''
api_router.include_router(ngr_router, prefix="/ngr", tags=["НГ Районы"])  # , description=''
api_router.include_router(lu_router, prefix="/lu", tags=["Лицензионные участки"])  # , description=''
