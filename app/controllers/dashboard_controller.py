from flask import render_template, session, redirect, url_for


def show_dashboard_page():
    user_id = session.get('user_id')

    if user_id is None:
        return redirect(url_for("show_login_page"))

    return render_template("dashboard.html")
