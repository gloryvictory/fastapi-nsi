from src.apps.base.models import BaseClass, MainMeta


class NGP(BaseClass):
    class Meta(MainMeta):
        tablename = "Ngp"
        pass
