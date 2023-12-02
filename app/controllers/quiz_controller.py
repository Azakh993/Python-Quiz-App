from flask import render_template, redirect, url_for, request, session
from .controller_helper import validate_login
from app.services.quiz_service import get_quiz_data


def show_quiz_page():
    validate_login()
    quiz_id = session.get("quiz_id")
    subject, questions = get_quiz_data(quiz_id)
    return render_template("quiz.html", subject=subject, questions=questions)


def show_quiz_result():
    if request.method == "POST":
        user_id = validate_login()
        quiz_id = request.form.get("quiz_id")

        if quiz_id is None:
            return redirect(url_for("show_dashboard_page"))
