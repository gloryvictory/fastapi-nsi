import ormar

from src.apps.base.models import BaseClass, MainMeta


class LU(BaseClass):
    class Meta(MainMeta):
        tablename = "Lu"
        pass
    nom_lic: str = ormar.String(max_length=255)
