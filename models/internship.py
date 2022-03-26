from models import dbc


class Internship(dbc.Model):

    __tablename__ = 'internships'
    __table_args__ = {'schema': 'info'}

    id = dbc.Column(dbc.BigInteger, primary_key=True, autoincrement=True, unique=True)
    name = dbc.Column(dbc.String(256))
    title = dbc.Column(dbc.String(256))

    @classmethod
    def create(cls, name, title):
        i = cls()
        i.name = name
        i.title = title
        cls.query.session.add(i)
        cls.query.session.commit()
        return i
