from pydantic.main import BaseModel


class BaseModel_NSI(BaseModel):
    id: int
    name_ru: str
    lat: float
    lon: float
    # crs: int
    # hash: str
    # create_date: datetime


class s_field(BaseModel_NSI):
    pass


class s_lu(BaseModel_NSI):
    nom_lic: str
    pass


class s_ngo(BaseModel_NSI):
    pass


class s_ngp(BaseModel_NSI):
    pass


class s_ngr(BaseModel_NSI):
    pass


class s_well(BaseModel_NSI):
    area: str
    pass


class s_area(BaseModel_NSI):
    pass
