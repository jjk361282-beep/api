import uuid
from ..exts import db

class Post(db.Model):
    id=db.Column(db.Uuid,primary_key=True,default=uuid.uuid4)
    title=db.Column(db.String)
    description=db.Column(db.String)
    author_id = db.Column(db.Uuid, db.ForeignKey('user.id'), nullable=False)
    # author = db.relationship('User', back_populates='user')
