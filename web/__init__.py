from flask import Blueprint

web_bp = Blueprint('web', __name__, template_folder='templates', static_folder='static', static_url_path='')


from .views.home import home, logout, main
web_bp.add_url_rule('/', view_func=home, methods=['GET', 'POST'])
web_bp.add_url_rule('/logout', view_func=logout, methods=['GET'])
web_bp.add_url_rule('/main', view_func=main, methods=['GET', 'POST'])
