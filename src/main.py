# uvicorn main:app --reload
import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from src import settings

from src.routers import api_router
from src.database import database, metadata, engine

app = FastAPI()
# root_path="/api/v1"
# metadata.create_all(engine) # for first creatng objects

app.state.database = database


# Root API
@app.get("/", status_code=200,
         name='Get Info',
         tags=['Главная'],
         description='Получает информацию о сервисе')
def root() -> JSONResponse:
    url_swagger = f"http://{settings.SERVER_HOST}:{settings.SERVER_PORT}/docs"

    return JSONResponse(status_code=200,
                        content={
                            "msg": "Success",
                            "Info": "Hello it is FastAPI-NSI project",
                            "Swagger Documentation": url_swagger})


app.include_router(api_router)


@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.database
    metadata.create_all(engine)
    if not database_.is_connected:
        print(f"connecting... {database_.url}")
        await database_.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()


if __name__ == "__main__":
    # set_logger()
    uvicorn.run("main:app", host=settings.SERVER_HOST, port=settings.SERVER_PORT, reload=True)
