import databases
import sqlalchemy

# sys.path.append("..")
# import src.settings as settings
from src import settings


# import settings

engine = sqlalchemy.create_engine(settings.DB_SQLITE)
metadata = sqlalchemy.MetaData()
database = databases.Database(settings.DB_SQLITE)

# 3. Database creation and tables creation
metadata.create_all(engine)
