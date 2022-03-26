from flask import Blueprint

web_bp = Blueprint('web', __name__, template_folder='templates', static_folder='static', static_url_path='')


from .views import admin
web_bp.add_url_rule('/', view_func=admin.home, methods=['GET', 'POST'])
web_bp.add_url_rule('/logout', view_func=admin.logout, methods=['GET'])
web_bp.add_url_rule('/main', view_func=admin.main, methods=['GET', 'POST'])
web_bp.add_url_rule('/captures', view_func=admin.captures, methods=['GET', 'POST'])
web_bp.add_url_rule('/sections', view_func=admin.sections, methods=['GET', 'POST'])
web_bp.add_url_rule('/questions', view_func=admin.questions, methods=['GET', 'POST'])

from .views import api
web_bp.add_url_rule('/register', view_func=api.register, methods=['POST'])
web_bp.add_url_rule('/auth', view_func=api.auth, methods=['POST'])
web_bp.add_url_rule('/all_internships', view_func=api.all_internships, methods=['POST'])
web_bp.add_url_rule('/all_captures', view_func=api.all_captures, methods=['POST'])
web_bp.add_url_rule('/all_questions/<capture_id>', view_func=api.all_questions, methods=['POST'])
web_bp.add_url_rule('/all_sections/<capture_id>', view_func=api.all_sections, methods=['POST'])
