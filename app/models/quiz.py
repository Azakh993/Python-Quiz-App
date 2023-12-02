from . import Base
from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.orm import relationship
from .selector import selector


class Quiz(Base):
    __tablename__ = 'quizzes'

    id = Column(Integer, primary_key=True)
    subject = Column(VARCHAR, unique=True, nullable=False)

    questions = relationship('Question', secondary=selector)
    results = relationship('Result', back_populates='quiz')
