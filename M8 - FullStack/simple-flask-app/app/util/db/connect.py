from sqlalchemy import create_engine

# dotenv is the library to parse .env values
from dotenv import dotenv_values



config = dotenv_values(".env")

# instead of host , port , database and user we can use the following connection url
DATABASE_URL = config.get('DATABASE_URL')


def db_engine():
    engine = create_engine(DATABASE_URL,echo=True,hide_parameters=True)
    return engine