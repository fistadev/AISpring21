from sqlalchemy import Column, Integer, String

from sqlalchemy.orm import declarative_base

from app.util.db.connect import db_engine


Base = declarative_base()

engine = db_engine()

class Project(Base):
     __tablename__ = 'projects'
     id = Column(Integer, primary_key=True)
     title = Column(String)
     description = Column(String)
     cover = Column(String)
     liveLink = Column(String)
     githubLink = Column(String)
     def toJSON(self):
        return {
            'id' : self.id,
            'title': self.title,
            'description': self.description,
            'cover': self.cover,
            'liveLink': self.liveLink,
            'githubLink': self.githubLink
        }



Base.metadata.create_all(engine)