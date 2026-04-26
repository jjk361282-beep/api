from apiflask import Schema
from apiflask.fields import UUID,String
# from apiflask.validators import Length

class PostIn(Schema):
    title=String()
    description=String()
    author_id=UUID()


class PostOut(Schema):
    id=UUID()
    title=String()
    description=String()
    author_id=UUID()
