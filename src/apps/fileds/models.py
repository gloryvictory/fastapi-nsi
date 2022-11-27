from datetime import datetime
import ormar

from src.config.settings import database, metadata


class Fields(ormar.Model):
    class Meta:
        tablename: str = "Fields"
        metadata = metadata
        database = database

    id: int = ormar.Integer(primary_key=True)
    name_ru: str = ormar.String(max_length=255)
    create_date: datetime = ormar.DateTime(default=datetime.now)
