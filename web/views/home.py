from flask_login import logout_user
from flask_security import login_required, current_user
from flask import redirect, render_template
from models import User


@login_required
def home():
    return redirect('/main')


@login_required
def logout():
    user = User.query.filter(User.email == current_user.email).one_or_none()
    if user.session_id:
        user.add_session()
    logout_user()
    return redirect('/')


@login_required
def main():
    return render_template('index.html')
