import os
from sqlalchemy import create_engine

username = os.getenv("DB_USER")
password = os.getenv("DB_PASS")
host = os.getenv("DB_HOST")
database = os.getenv("DB_NAME")

engine = create_engine(
    f"mysql+mysqldb://{username}:{password}@{host}/{database}",
)

conn = engine.connect()
