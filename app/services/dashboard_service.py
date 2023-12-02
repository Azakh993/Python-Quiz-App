from collections import OrderedDict
from app.repositories import quiz_repository, result_repository


def generate_dashboard_data(user_id):
    quizzes = quiz_repository.get_all_quizzes()
    results = result_repository.get_all_results(user_id)

    quizzes_and_results_dict = OrderedDict()

    for quiz in quizzes:
        quiz_id = quiz.id

        if results is not None and results.get(quiz_id) is not None:
            score = results.get(quiz_id)
            quizzes_and_results_dict[quiz] = score
        else:
            quizzes_and_results_dict[quiz] = None

    return quizzes_and_results_dict
