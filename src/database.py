# CREATE USER nsi WITH ENCRYPTED PASSWORD 'nsipass';
# CREATE DATABASE nsi WITH OWNER nsi;
# GRANT ALL PRIVILEGES ON DATABASE nsi TO nsi;
# CREATE SCHEMA IF NOT EXISTS nsi AUTHORIZATION nsi;
# SET search_path to nsi;
#
# GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO nsi;
# GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO nsi;
# GRANT ALL PRIVILEGES ON ALL FUNCTIONS  IN SCHEMA public TO nsi;
# GRANT rds_superuser TO nsi;


import databases
import sqlalchemy

# sys.path.append("..")
# import src.settings as settings
from src import settings


# import settings

# engine = sqlalchemy.create_engine(settings.DB_SQLITE)
# database = databases.Database(settings.DB_SQLITE)
engine = sqlalchemy.create_engine(settings.DB_DSN)
database = databases.Database(settings.DB_DSN)
metadata = sqlalchemy.MetaData(schema=settings.DB_SCHEMA) # чтобы складывать в одну схему nsi



# MetaData(schema="alpha")
# 3. Database creation and tables creation
metadata.create_all(engine)
