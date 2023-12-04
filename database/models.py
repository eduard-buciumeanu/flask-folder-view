from app import app
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Folder(Base):
    __tablename__ = 'folders'
    id = Column(Integer, primary_key=True)
    folder_name = Column(String(50), unique=True, nullable=False)
    folder_path = Column(String, unique=True, nullable=False)


engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
Base.metadata.create_all(bind=engine)