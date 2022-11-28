import sys

import databases
import sqlalchemy

# sys.path.append("..")
import src.config.settings as settings

# import settings

engine = sqlalchemy.create_engine(settings.DB_SQLITE)
metadata = sqlalchemy.MetaData()
database = databases.Database(settings.DB_SQLITE)

