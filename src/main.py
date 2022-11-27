# uvicorn main:app --reload
import uvicorn


from fastapi import FastAPI

# , Query, HTTPException, Path
# from typing import Union
#
# from pydantic import BaseModel
# from typing import Optional
# import json

from src.config.settings import database, metadata, engine

app = FastAPI()
app.state.database = database


@app.get("/")
def read_root():
    return {"msg": "Hello it is FastAPI-NSI project"}
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



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
