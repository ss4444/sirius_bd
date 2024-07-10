import databases
import sqlalchemy

postgres_dsn = "postgresql://meta_db_user:meta_db_password@localhost:5432/db"

metadata = sqlalchemy.MetaData()
database = databases.Database(postgres_dsn)
