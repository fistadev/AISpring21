from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from utils.db.connect import db_engine

engine = db_engine()

Base = declarative_base()


class User (Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True)
    name = Column(String)
    last_name= Column(String)
    email = Column(String)
    password_hash = Column(String(256),nullable=False)
    def toJSON(self):
        return {
            'id': self.id,
            'name':self.name,
            'last_name':self.last_name,
            'email':self.email,
        }


Base.metadata.create_all(engine)

