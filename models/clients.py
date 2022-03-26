from models import dbc


class Clients(dbc.Model):

    __tablename__ = 'clients'
    __table_args__ = {'schema': 'info'}

    id = dbc.Column(dbc.BigInteger, primary_key=True, autoincrement=True, unique=True)
    username = dbc.Column(dbc.String(256))
    password = dbc.Column(dbc.String(256))

    @classmethod
    def create(cls, username, password):
        c = cls()
        c.username = username
        c.password = password
        cls.query.session.add(c)
        cls.query.session.commit()
        return c
