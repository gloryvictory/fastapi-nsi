# uvicorn main:app --reload
import os

import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from src.config import settings
# , Query, HTTPException, Path
# from typing import Union
#
# from pydantic import BaseModel
# from typing import Optional
# import json
import logging as log

from src.apps.routers import api_router
from src.config.db import database, metadata, engine

app = FastAPI()
# root_path="/api/v1"
# metadata.create_all(engine) # for first creatng objects

app.state.database = database
app.include_router(api_router)


# Root API
@app.get("/")
def root() -> JSONResponse:
    return JSONResponse(status_code=200,
                        content={
                            "msg": "Hello it is FastAPI-NSI project"})


@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.database
    metadata.create_all(engine)
    if not database_.is_connected:
        await database_.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()


def set_logger():
    for handler in log.root.handlers[:]:  # Remove all handlers associated with the root logger object.
        log.root.removeHandler(handler)

    log_folder = settings.FOLDER_OUT
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)

    file_log = str(os.path.join(log_folder, settings.FILE_LOG))  # from cfg.file

    if os.path.isfile(file_log):  # Если выходной LOG файл существует - удаляем его
        os.remove(file_log)
    log.basicConfig(filename=file_log, format=settings.FILE_LOG_FORMAT, level=log.INFO,
                    filemode='w')
    log.info(file_log)


if __name__ == "__main__":
    set_logger()
    uvicorn.run("main:app", host=settings.SERVER_HOST, port=settings.SERVER_PORT, reload=True)
