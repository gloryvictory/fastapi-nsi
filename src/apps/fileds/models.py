from datetime import datetime
import ormar

from src.config.db import database, metadata


class MainMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


class BaseClass(ormar.Model):
    class Meta(MainMeta):
        # tablename = "Fields"
        pass
    # primary_key=True
    id: int = ormar.Integer(primary_key=True)
    name_ru: str = ormar.String(max_length=255)
    lat: float = ormar.Float(scale=6, precision=8)
    lon: float = ormar.Float(scale=6, precision=8)
    crs: int = ormar.Integer()
    hash: str = ormar.String(max_length=255)
    create_date: datetime = ormar.DateTime(default=datetime.now)


class Fields(BaseClass):
    class Meta(MainMeta):
        tablename = "Fields"
        pass
