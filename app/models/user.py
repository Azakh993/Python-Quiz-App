from . import Base
from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(VARCHAR, unique=True, nullable=False)
    password = Column(VARCHAR, unique=False, nullable=False)

    results = relationship('Result', back_populates='user')
