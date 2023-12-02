from flask import redirect, url_for, session


def validate_login():
    user_id = session.get('user_id')

    if user_id is None:
        return redirect(url_for("show_login_page"))

    return user_id
