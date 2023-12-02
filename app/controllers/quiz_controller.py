from flask import render_template, redirect, url_for, request, session
from .controller_helper import validate_login
from app.services.quiz_service import get_quiz_data, correct_quiz


def show_quiz_page():
    validate_login()
    quiz_id = session.get("quiz_id")
    subject, questions = get_quiz_data(quiz_id)
    return render_template("quiz.html", points=None, subject=subject, questions=questions)


def show_quiz_result():
    if request.method == "POST":
        user_id = validate_login()

        dashboard_request = request.form.get("exit")
        if dashboard_request is not None:
            return redirect(url_for("show_dashboard_page"))

        quiz_id = session.get('quiz_id')
        subject, questions = get_quiz_data(quiz_id)

        question_id_to_answer = process_form()
        points = correct_quiz(user_id, quiz_id, question_id_to_answer)

        return render_template("quiz.html", points=points, subject=subject, questions=questions)

    return show_quiz_result()


def process_form():
    form_dict = request.form.to_dict()
    question_id_to_answer_dict = {int(key[-1]): value for key, value in form_dict.items()}
    return question_id_to_answer_dict
