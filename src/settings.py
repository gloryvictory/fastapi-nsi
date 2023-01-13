import os
from time import strftime  # Load just the strftime Module from Time

API_VERSION = "/api/v1"

DATETIME_CURRENT = str(strftime("%Y-%m-%d-%H-%M-%S"))

FILE_LOG_NAME = 'fastapi-nsi'
FILE_LOG = DATETIME_CURRENT + '_' + FILE_LOG_NAME + '.log'
FILE_LOG_FORMAT = '%(asctime)s %(levelname)s %(message)s'

# FOLDER_IN  = 'C:\\TEMP\\Geodex_files'
FOLDER_BASE = os.getenv("FOLDER_BASE", "C:\\Glory\\Projects\\Python\\zsniigg\\fastapi-nsi\\src")
FOLDER_OUT = 'log'
FOLDER_GEOJSON_OUT = 'geojson'
FOLDER_DATA = 'data'

DB_SQLITE = "sqlite:///fastapi-nsi.db"
# DB_SCHEMA = 'public'
# DB_HOST = 'localhost'
# DB_PORT = '5432'
# DB_USER = 'geodex2'
# DB_PASSWORD = 'geodex2_password'
# DB_NAME = 'geodex2'
# DB_SCHEMA = 'geodex2'
# postgresql://udatauser2:udatauser2pwd@localhost:5432/udatadb2
# DB_DSN = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

SERVER_HOST = os.getenv("SERVER_HOST", "0.0.0.0")
SERVER_PORT = os.getenv("SERVER_PORT", 8000)


CRS_OUT = 4326  # 4326 - WGS 84

FIELDS_FILE_GEOJSON_IN = 'fields_test.geojson' # 'mest.geojson'
FIELDS_FILE_GEOJSON_OUT = 'fields.geojson'
FIELDS_NAME_FIELD = 'name_ru'
FIELDS_FILE_LOG = FIELDS_FILE_GEOJSON_IN + '.log'

NGP_FILE_GEOJSON_IN = 'NGP.geojson' # 'mest.geojson'
NGP_FILE_GEOJSON_OUT = 'NGP.geojson'
NGP_NAME_FIELD = 'province'
NGP_FILE_LOG = NGP_FILE_GEOJSON_IN + '.log'

NGO_FILE_GEOJSON_IN = 'NGO.geojson' # 'mest.geojson'
NGO_FILE_GEOJSON_OUT = 'NGO.geojson'
NGO_NAME_FIELD = 'region'
NGO_FILE_LOG = NGO_FILE_GEOJSON_IN + '.log'

NGR_FILE_GEOJSON_IN = 'NGR.geojson' # 'mest.geojson'
NGR_FILE_GEOJSON_OUT = 'NGR.geojson'
NGR_NAME_FIELD = 'district'
NGR_FILE_LOG = NGR_FILE_GEOJSON_IN + '.log'

LU_FILE_GEOJSON_IN = 'LU.geojson' # 'mest.geojson'
LU_FILE_GEOJSON_OUT = 'LU.geojson'
LU_FILE_LOG = LU_FILE_GEOJSON_IN + '.log'
LU_NAME_FIELD = 'name'
LU_NOM_LIC_FIELD = 'nom_lic'

SKV_FILE_GEOJSON_IN = 'SKV.geojson' # 'mest.geojson'
SKV_FILE_GEOJSON_OUT = 'SKV.geojson'
SKV_FILE_LOG = SKV_FILE_GEOJSON_IN + '.log'
SKV_NAME_FIELD = 'well_name'
SKV_NAME_AREA_FIELD = 'pl'