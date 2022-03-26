from models import dbc


class Clients(dbc.Model):

    __tablename__ = 'clients'
    __table_args__ = {'schema': 'info'}

    id = dbc.Column(dbc.BigInteger, primary_key=True, autoincrement=True, unique=True)
    username = dbc.Column(dbc.String(256))
    password = dbc.Column(dbc.String(256))
