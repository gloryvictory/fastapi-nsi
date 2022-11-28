from datetime import datetime
import ormar

from src.config.db import database, metadata


class MainMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


class Fields(ormar.Model):
    class Meta(MainMeta):
        tablename: str = "Fields"
        pass 
        
    id: int = ormar.Integer(primary_key=True)
    name_ru: str = ormar.String(max_length=255)
    create_date: datetime = ormar.DateTime(default=datetime.now)
