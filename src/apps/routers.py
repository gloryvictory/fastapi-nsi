from fastapi import APIRouter

from src.apps.fileds.endpoint import fields_router

api_router = APIRouter()


api_router.include_router(fields_router, prefix="/fields", tags=["fields"])
