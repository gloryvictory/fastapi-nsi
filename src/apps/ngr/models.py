from src.apps.base.models import BaseClass, MainMeta


class NGR(BaseClass):
    class Meta(MainMeta):
        tablename = "Ngr"
        pass
