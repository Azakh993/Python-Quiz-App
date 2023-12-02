from app.repositories.quiz_repository import get_quiz
from app.repositories.question_repository import get_questions, get_question
import copy

from app.repositories.result_repository import add_or_update_result


def process_options(questions):
    questions_copy = copy.deepcopy(questions)
    for question in questions_copy:
        split_options = question.options.split(',')
        question.options = split_options
    return questions_copy


def get_quiz_data(quiz_id):
    subject = get_quiz(quiz_id).subject
    questions = get_questions(quiz_id)
    processed_questions = process_options(questions)
    return subject, processed_questions


def correct_quiz(user_id, quiz_id, question_id_to_answer):
    correct_answers = 0
    for question_id, answer in question_id_to_answer.items():
        question = get_question(question_id)
        correct_answer = question.answer

        if answer == correct_answer:
            correct_answers += 1

    add_or_update_result(user_id, quiz_id, correct_answers)

    return correct_answers
