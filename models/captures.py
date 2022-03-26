from models import dbc
from sqlalchemy import JSON


class Captures(dbc.Model):

    __tablename__ = 'captures'
    __table_args__ = {'schema': 'info'}

    id = dbc.Column(dbc.BigInteger, primary_key=True, autoincrement=True, unique=True)
    name = dbc.Column(dbc.String(256), unique=True)
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

    def add_questions(self, questions: dict):
        questions.update(self.questions)
        self.questions = questions
        self.query.session.commit()

    def add_sections(self, sections: dict):
        sections.update(self.sections)
        self.sections = sections
        self.query.session.commit()
