from flask import Blueprint

web_bp = Blueprint('web', __name__, template_folder='templates', static_folder='static', static_url_path='')


from .views import admin
web_bp.add_url_rule('/', view_func=admin.home, methods=['GET', 'POST'])
web_bp.add_url_rule('/logout', view_func=admin.logout, methods=['GET'])
web_bp.add_url_rule('/main', view_func=admin.main, methods=['GET', 'POST'])
web_bp.add_url_rule('/captures', view_func=admin.captures, methods=['GET', 'POST'])
web_bp.add_url_rule('/sections', view_func=admin.sections, methods=['GET', 'POST'])
web_bp.add_url_rule('/questions', view_func=admin.questions, methods=['GET', 'POST'])
