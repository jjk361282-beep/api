from flask_app.exts import db
from flask_app.models.post import Post

class PostControllers:
    @staticmethod
    def get_all_post()->list[Post]:
        return Post.query.all()
    
    @staticmethod
    def create_post(data):
        post=Post(
            title=data.get('title'),
            description=data.get('description'),
            author_id=data.get('author_id'),
        )
        db.session.add(post)
        db.session.commit()
        return post