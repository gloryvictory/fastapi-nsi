from datetime import datetime
from typing import List

from pydantic.main import BaseModel


class Field(BaseModel):
    id: int
    name_ru: str
    lat: float
    lon: float
    # crs: int
    # hash: str
    # create_date: datetime
