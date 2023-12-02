from . import Base
from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.orm import relationship
from .selector import selector


class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    text = Column(VARCHAR, nullable=False)
    options = Column(VARCHAR, nullable=False)
    answer = Column(VARCHAR, nullable=False)

    quizzes = relationship('Quiz', secondary='selector', back_populates='questions')
