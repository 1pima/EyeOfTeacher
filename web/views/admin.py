from flask_login import logout_user
from flask_security import login_required, current_user
from flask import redirect, render_template, request, g
from models import User, Internship, Captures
from middlewares.utilits import parse_params
from web.schema import admin as sh


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
@parse_params(sh.InternshipRq())
def main():
    if request.method != 'GET':
        rq = g.rq
        Internship.create(name=rq['name'], title=rq['title'])
    return render_template('internship.html')


@login_required
@parse_params(sh.CapturesRq())
def captures():
    if request.method != 'GET':
        rq = g.rq
        Captures.create(name=rq['name'], title=rq['title'])
    return render_template('captures.html')


@login_required
@parse_params(sh.Sections())
def sections():
    if request.method != 'GET':
        rq = g.rq
        cap = Captures.query.filter(Captures.name == rq['name']).one()
        cap.add_sections({rq['sec_name']: rq['title']})
    return render_template('sections.html', captures=Captures.query.all())


@login_required
@parse_params(sh.Questions())
def questions():
    if request.method != 'GET':
        rq = g.rq
        cap = Captures.query.filter(Captures.name == rq['name']).one()
        cap.add_questions({rq['question']: rq['answers']})
    return render_template('questions.html', captures=Captures.query.all())
