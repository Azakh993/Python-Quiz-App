from app.repositories.quiz_repository import get_quiz
from app.repositories.question_repository import get_questions


def process_options(questions):
    for question in questions:
        split_options = question.options.split(',')
        question.options = split_options


def get_quiz_data(quiz_id):
    subject = get_quiz(quiz_id).subject
    questions = get_questions(quiz_id)
    process_options(questions)
    return subject, questions

