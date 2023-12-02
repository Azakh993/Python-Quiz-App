from flask import Flask
from app.controllers import login_controller, dashboard_controller, quiz_controller
from app.config.config import SECRET_KEY

app = Flask(__name__)
app.secret_key = SECRET_KEY

# Login routes
app.route("/login")(login_controller.show_login_page)
app.route("/login", methods=["POST"])(login_controller.login)

# Dashboard routes
app.route("/dashboard")(dashboard_controller.show_dashboard_page)


if __name__ == '__main__':
    app.run(debug=True)