from main import db
import uuid

class User(db.Model):
    id=db.Column(db.Uuid,primary_key=True,default=uuid.uuid4)
    name=db.Column(db.String)
    email=db.Column(db.String)

    posts = db.relationship('Post', back_populates='author', lazy='dynamic')

    def __repr__(self):
        return f"< User id:{self.id}>"

class Post(db.Model):
    id=db.Column(db.Uuid,primary_key=True,default=uuid.uuid4)
    title=db.Column(db.String)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    author = db.relationship('User', back_populates='articles')
