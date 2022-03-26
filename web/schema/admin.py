from marshmallow import fields as f, Schema, pre_load


class BaseAdminSchema(Schema):
    pass


class InternshipRq(BaseAdminSchema):

    name = f.Str()
    title = f.Str()


class CapturesRq(InternshipRq):
    pass


class Sections(InternshipRq):

    sec_name = f.Str()


class Answers(Schema):

    right_answer = f.Str()
    wrong_answer1 = f.Str()
    wrong_answer2 = f.Str()


class Questions(BaseAdminSchema):

    name = f.Str()
    question = f.Str()
    answers = f.Nested(Answers)

    @pre_load
    def _remake(self, data, **kwargs):
        print(data)
        data = {'question': data['question'],
                'name': data['name'],
                'answers': {'right_answer': data['right_answer'],
                            'wrong_answer1': data['wrong_answer1'],
                            'wrong_answer2': data['wrong_answer2']}}
        return data
