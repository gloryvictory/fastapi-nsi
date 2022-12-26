from fastapi import APIRouter

from src.apps.fileds.endpoint import fields_router
from src.apps.ngp.endpoint import ngp_router

api_router = APIRouter(prefix='/api/v1')


api_router.include_router(fields_router, prefix="/fields", tags=["Месторождения"]) # , description='Месторождения'
api_router.include_router(ngp_router, prefix="/ngp", tags=["НГ Провинции"]) # , description='Месторождения'
