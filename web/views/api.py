from flask_login import logout_user
from flask_security import login_required, current_user
from flask import redirect, render_template, request, g, jsonify, abort
from models import Clients, Internship, Captures
from middlewares.utilits import parse_params
from web.schema import api as sh


@parse_params(sh.RegisterRq())
def register():
    rq = g.rq
    c = Clients.query.filter(Clients.username == rq['username']).one()
    if c:
        return jsonify({'success': False, 'info': 'user already exists'})
    client = Clients.create(username=rq['username'],
                            password=rq['password'])
    if client:
        return jsonify({'success': True})
    return jsonify({'success': False})


@parse_params(sh.AuthRq())
def auth():
    rq = g.rq
    client = Clients.query.filter(Clients.username == rq['username']).one()
    if not client or client.password != rq['password']:
        return jsonify({'success': False})
    return jsonify({'success': True})


@parse_params(sh.InternshipsRq())
def all_internships():
    rq = g.rq
    client = Clients.query.filter(Clients.username == rq['username']).one()
    if not client or client.password != rq['password']:
        abort(403)
    return jsonify([{'title': i.name, 'description': i.title} for i in Internship.query.all()])


@parse_params(sh.InternshipsRq())
def all_captures():
    rq = g.rq
    client = Clients.query.filter(Clients.username == rq['username']).one()
    if not client or client.password != rq['password']:
        abort(403)
    return jsonify([{'title': i.name, 'description': i.title, 'id': i.id} for i in Captures.query.all()])


@parse_params(sh.InternshipsRq())
def all_captures():
    rq = g.rq
    client = Clients.query.filter(Clients.username == rq['username']).one()
    if not client or client.password != rq['password']:
        abort(403)
    return jsonify([{'title': i.name, 'description': i.title, 'id': i.id} for i in Captures.query.all()])


@parse_params(sh.InternshipsRq())
def all_captures():
    rq = g.rq
    client = Clients.query.filter(Clients.username == rq['username']).one()
    if not client or client.password != rq['password']:
        abort(403)
    return jsonify([{'title': i.name, 'description': i.title, 'id': i.id} for i in Captures.query.all()])


@parse_params(sh.InternshipsRq())
def all_sections(capture_id):
    rq = g.rq
    client = Clients.query.filter(Clients.username == rq['username']).one()
    if not client or client.password != rq['password']:
        abort(403)
    capture = Captures.query.filter(Captures.id == capture_id).one()
    if not capture:
        abort(404)
    return jsonify([{'title': k, 'description': v} for k, v in capture.sections.items()])


@parse_params(sh.InternshipsRq())
def all_questions(capture_id):
    rq = g.rq
    client = Clients.query.filter(Clients.username == rq['username']).one()
    if not client or client.password != rq['password']:
        abort(403)
    capture = Captures.query.filter(Captures.id == capture_id).one()
    if not capture:
        abort(404)
    return jsonify([{'question': k, 'right_answer': v} for k, v in capture.questions.items()])
