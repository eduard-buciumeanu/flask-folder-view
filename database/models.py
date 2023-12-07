from utils.paths import database_path
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine(f'sqlite:///{database_path}', echo=True)
Base = declarative_base()

class Folder(Base):
    __tablename__ = 'folders'
    id = Column(Integer, primary_key=True)
    folder_name = Column(String(50), unique=True, nullable=False)
    folder_path = Column(String, unique=True, nullable=False)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()