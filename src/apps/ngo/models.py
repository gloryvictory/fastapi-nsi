from src.apps.base.models import BaseClass, MainMeta


class NGO(BaseClass):
    class Meta(MainMeta):
        tablename = "Ngo"
        pass
