from flask_sqlalchemy import SQLAlchemy

dbc = SQLAlchemy()

from .users import User, Role
from .internship import Internship
from .captures import Captures
from .clients import Clients
