from app.repositories.quiz_repository import get_quiz
from app.repositories.question_repository import get_questions
import copy


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

