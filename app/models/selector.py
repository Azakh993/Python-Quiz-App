from . import Base
from sqlalchemy import Column, Integer, ForeignKey, Table

selector = Table('selector', Base.metadata,
                 Column('quiz_id', Integer, ForeignKey('quizzes.id'), primary_key=True),
                 Column('question_id', Integer, ForeignKey('questions.id'), primary_key=True)
                 )
