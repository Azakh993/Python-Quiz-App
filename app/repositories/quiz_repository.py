from app.models.quiz import Quiz
from . import session


def get_all_quizzes():
    try:
        return session.query(Quiz).all()
    except Exception as exception:
        print(f'Error: {str(exception)}')
        session.rollback()
        raise
