from flask import render_template, session, redirect, url_for

from app.services.dashboard_service import generate_dashboard_data


def show_dashboard_page():
    user_id = session.get('user_id')

    if user_id is None:
        return redirect(url_for("show_login_page"))

    quizzes_and_results_dict = generate_dashboard_data(user_id)

    return render_template("dashboard.html", quizzes_and_results_dict=quizzes_and_results_dict)
