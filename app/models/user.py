from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(VARCHAR, unique=True, nullable=False)
    password = Column(VARCHAR, unique=False, nullable=False)

