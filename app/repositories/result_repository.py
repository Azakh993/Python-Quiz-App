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

