from pydantic.main import BaseModel


class BaseModel_NSI(BaseModel):
    id: int
    name_ru: str
    lat: float
    lon: float
    # crs: int
    # hash: str
    # create_date: datetime


class Field(BaseModel_NSI):
    pass


class LU(BaseModel_NSI):
    nom_lic: str
    pass


class NGO(BaseModel_NSI):
    pass


class NGP(BaseModel_NSI):
    pass


class NGR(BaseModel_NSI):
    pass

