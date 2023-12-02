from app.models.question import Question
from app.models.selector import selector
from . import session


def get_questions(quiz_id):
    try:
        return ((session.query(Question)
                .join(selector, Question.id == selector.c.question_id)
                .filter(selector.c.quiz_id == quiz_id))
                .all())
    except Exception as exception:
        print(f'Error: {str(exception)}')
        session.rollback()
        raise
