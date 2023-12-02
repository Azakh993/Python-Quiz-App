from . import Base
from sqlalchemy import Column, Integer, ForeignKey


class Selector(Base):
    __tablename__ = 'selector'

    quiz_id = Column('quiz_id', Integer, ForeignKey('quizzes.id'))
    question_id = Column('question_id', Integer, ForeignKey('questions.id'))