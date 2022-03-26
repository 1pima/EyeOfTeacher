from flask import Flask
from flask_security import Security, SQLAlchemyUserDatastore


def create_app():

    app = Flask(__name__)

    from configuration import default
    app.config.from_object(default)

    with app.app_context():

        from models import dbc
        dbc.init_app(app)

        from web import web_bp
        app.register_blueprint(web_bp,
                               url_prefix='',
                               template_folder='templates',
                               static_folder='static',
                               static_url_path='')

        from models import User, Role
        user_datastore = SQLAlchemyUserDatastore(dbc, User, Role)
        Security(app, user_datastore)

    return app
