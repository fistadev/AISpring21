import jwt

import datetime


# dotenv is the library to parse .env values
from dotenv import dotenv_values



config = dotenv_values(".env")

# instead of host , port , database and user we can use the following connection url
JWT_SECRET = config.get('JWT_SECRET')



def generate_token(id):
    exp = datetime.datetime.utcnow() + datetime.timedelta(hours=8)
    return jwt.encode({"id": id,"exp":exp}, JWT_SECRET, algorithm="HS256")

def verify_token(token):
    return jwt.decode(token, JWT_SECRET, algorithms=["HS256"])