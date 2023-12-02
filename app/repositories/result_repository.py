from collections import OrderedDict

from app.models.result import Result
from . import session


def get_all_results(user_id):
    try:
        results = session.query(Result).filter_by(user_id=user_id).all()
        return OrderedDict((result.quiz_id, result.score) for result in results)

    except Exception as exception:
        print(f'Error: {str(exception)}')
        session.rollback()
        raise


def get_result(username, quiz_id):
    try:
        return session.query(Result).filter_by(username=username, quiz_id=quiz_id).first()
    except Exception as exception:
        print(f'Error: {str(exception)}')
        session.rollback()
        raise


def add_or_update_result(user_id, quiz_id, new_score):
    try:
        result = session.query(Result).filter_by(user_id=user_id, quiz_id=quiz_id).first()

        if result is None:
            new_result = Result(user_id=user_id, quiz_id=quiz_id, score=new_score)
            session.add(new_result)
        else:
            result.score = new_score

        session.commit()

    except Exception as exception:
        print(f'Error: {str(exception)}')
        session.rollback()
        raise