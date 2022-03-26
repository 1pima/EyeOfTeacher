import pyotp
from flask_security import UserMixin, RoleMixin
from models import dbc


roles_users = dbc.Table('roles_users',
                        dbc.Column('user_id', dbc.Integer(), dbc.ForeignKey('admin.user.id')),
                        dbc.Column('role_id', dbc.Integer(), dbc.ForeignKey('admin.role.id')),
                        schema='admin')


class User(dbc.Model, UserMixin):

    __tablename__ = 'user'
    __table_args__ = {'schema': 'admin'}

    id = dbc.Column(dbc.BigInteger, primary_key=True, autoincrement=True, unique=True)
    email = dbc.Column(dbc.String(90), unique=True)
    password = dbc.Column(dbc.String(256))
    active = dbc.Column(dbc.Boolean())
    roles = dbc.relationship('Role', secondary=roles_users, backref=dbc.backref('users', lazy='dynamic'))
    secret_base32 = dbc.Column(dbc.String(256))
    session_id = dbc.Column(dbc.String(256))

    def __str__(self):
        return self.email

    @classmethod
    def create(cls, email, password):
        u = cls()
        u.email = email
        u.password = password
        u.active = True
        u.secret_base32 = pyotp.random_base32()  # для otp
        u.session_id = ''
        cls.query.session.add(u)
        cls.query.session.commit()
        return u


class Role(dbc.Model, RoleMixin):

    __tablename__ = 'role'
    __table_args__ = {'schema': 'admin'}

    id = dbc.Column(dbc.Integer(), primary_key=True)
    name = dbc.Column(dbc.String)
    access = dbc.Column(dbc.String(100))
    id_access = dbc.Column(dbc.Integer())

    def __str__(self):
        return self.name
