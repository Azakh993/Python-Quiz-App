from flask import render_template, redirect, url_for, request, session
from .controller_helper import validate_login
from app.services.dashboard_service import generate_dashboard_data


def show_dashboard_page():
    user_id = validate_login()
    quizzes_and_results_dict = generate_dashboard_data(user_id)
    return render_template("dashboard.html", quizzes_and_results_dict=quizzes_and_results_dict)


def select_quiz():
    if request.method == "POST":
        validate_login()
        quiz_id = request.form.get("quiz_id")
        session["quiz_id"] = quiz_id
        if quiz_id is not None:
            return redirect(url_for("show_quiz_page"))
