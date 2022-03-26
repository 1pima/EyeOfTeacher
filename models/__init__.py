from flask_sqlalchemy import SQLAlchemy

dbc = SQLAlchemy()

from .users import User, Role
