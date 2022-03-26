from marshmallow import fields as f, Schema


class RegisterRq(Schema):

    username = f.Str()
    password = f.Str()


class AuthRq(RegisterRq):
    pass


class InternshipsRq(RegisterRq):
    pass


class CapturesRq(RegisterRq):
    pass
