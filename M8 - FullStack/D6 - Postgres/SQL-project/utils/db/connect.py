from dotenv import dotenv_values
from sqlalchemy import create_engine

config = dotenv_values(".env")

HOST = config.get("HOST")
DB = config.get("DB")
USER = config.get("USER")
PASSWORD = config.get("PASSWORD")
PORT = config.get("PORT")

# print(HOST)


def db_engine():
    ##    "postgresql://USER:PASSWORD@HOST:PORT/DBNAME"
    URL = "postgresql://{}:{}@{}:{}/{}".format(USER, PASSWORD, HOST, PORT, DB)
    engine = create_engine(URL, echo=True, hide_parameters=True)
    return engine
