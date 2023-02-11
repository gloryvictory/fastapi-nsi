from datetime import datetime
import ormar

from src.database import database, metadata


class MainMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


class BaseClass(ormar.Model):
    class Meta(MainMeta):
        abstract = True
        # tablename = "Fields"
        pass

    id: int = ormar.Integer(primary_key=True)
    name_ru: str = ormar.String(max_length=255, index=True)
    # lat: float = ormar.Float(scale=6, precision=8)
    lat: float = ormar.Float(precision=21, scale=18)
    lon: float = ormar.Float(precision=21, scale=18)
    crs: int = ormar.Integer()
    hash: str = ormar.String(max_length=255)
    create_date: datetime = ormar.DateTime(default=datetime.now)


class Field(BaseClass):
    class Meta(MainMeta):
        tablename = "field"
        pass


class LU(BaseClass):
    class Meta(MainMeta):
        tablename = "lu"
        pass

    nom_lic: str = ormar.String(max_length=255)


class NGO(BaseClass):
    class Meta(MainMeta):
        tablename = "ngo"
        pass


class NGP(BaseClass):
    class Meta(MainMeta):
        tablename = "ngp"
        pass


class NGR(BaseClass):
    class Meta(MainMeta):
        tablename = "ngr"
        pass


class WELL(BaseClass):
    class Meta(MainMeta):
        tablename = "well"
        pass

    area: str = ormar.String(max_length=255, index=True )

# Немного по другим правилам...
class AREA(ormar.Model):
    class Meta(MainMeta):
        tablename = "area"
        pass

    id: int = ormar.Integer(primary_key=True)
    name_ru: str = ormar.String(max_length=255, index=True )
    create_date: datetime = ormar.DateTime(default=datetime.now)