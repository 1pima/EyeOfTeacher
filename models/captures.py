from models import dbc
from sqlalchemy import JSON


class Captures(dbc.Model):

    __tablename__ = 'captures'
    __table_args__ = {'schema': 'info'}

    id = dbc.Column(dbc.BigInteger, primary_key=True, autoincrement=True, unique=True)
    name = dbc.Column(dbc.String(256))
    title = dbc.Column(dbc.String(256))
    sections = dbc.Column(JSON, nullable=False)
    questions = dbc.Column(JSON, nullable=False)

    @classmethod
    def create(cls, name, title):
        c = cls()
        c.name = name
        c.title = title
        c.sections = {}
        c.questions = {}
        cls.query.session.add(c)
        cls.query.session.commit()
        return c

    def add_questions(self, questions=None):
        q = self.questions
        q.update(questions or {})
        self.query.session.commit()

    def add_sections(self, sections=None):
        q = self.sections
        q.update(sections or {})
        self.query.session.commit()
