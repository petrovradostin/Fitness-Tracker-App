from sqlalchemy import create_engine, MetaData, Column, Integer
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db" 

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
metadata = MetaData()

@as_declarative()
class Base:
    id: any
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    @declared_attr
    def id(cls):
        return Column(Integer, primary_key=True, index=True)
