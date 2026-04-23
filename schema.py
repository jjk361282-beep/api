from apiflask import Schema
from apiflask.fields import String,Integer,UUID

class UserIn(Schema):
    name=String()
    email=String()

class UserOut(Schema):
    id=UUID()
    name=String()
    email=String()