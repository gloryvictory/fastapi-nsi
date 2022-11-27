import databases
import sqlalchemy

from time import strftime   # Load just the strftime Module from Time

API_VERSION = "/api/v1"

FILE_LOG_NAME = 'fastapi-nsi'
FILE_LOG = str(strftime("%Y-%m-%d-%H-%M-%S") + '_' + FILE_LOG_NAME + '.log')
FILE_LOG_FORMAT = '%(asctime)s %(levelname)s %(message)s'

FILE_FIELDS = 'fields.geojson'

# FOLDER_IN  = 'C:\\TEMP\\Geodex_files'
FOLDER_OUT = 'log'
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


engine = sqlalchemy.create_engine(DB_SQLITE)

metadata = sqlalchemy.MetaData()
database = databases.Database(DB_SQLITE)


