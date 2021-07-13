from sqlalchemy import Column, Integer, String

from sqlalchemy.orm import declarative_base

from app.util.db.connect import db_engine

import bcrypt


Base = declarative_base()

engine = db_engine()

class User(Base):
     __tablename__ = 'users'
     id = Column(Integer, primary_key=True)
     name = Column(String)
     last_name = Column(String)
     email = Column(String)
     password_hash = Column(String(256), nullable=False)
     def toJSON(self):
        return {
            'id' : self.id,
            'name': self.name,
            'last_name': self.last_name,
            'email': self.email
        }
        
     def hash_password(self):
        self.password_hash=bcrypt.hashpw(password=self.password_hash.encode("utf8"),salt=bcrypt.gensalt()).decode("utf8")
        return self.password_hash

     def check_password(self,claimed_password):
         return bcrypt.checkpw(password=claimed_password.encode("utf8"),hashed_password=self.password_hash.encode("utf8"))
         


Base.metadata.create_all(engine)