from . import Base
from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.orm import relationship


class Quiz(Base):
    __tablename__ = 'quizzes'

    id = Column(Integer, primary_key=True)
    subject = Column(VARCHAR, unique=True, nullable=False)

    results = relationship('Result', back_populates='quiz')
