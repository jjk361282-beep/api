from ..exts import db
from ..models.user import User
import uuid
from apiflask import abort
from sqlalchemy.exc import NoResultFound, SQLAlchemyError

class UserContreller:

    # get all user

    @staticmethod
    def get_all():
        """
        return all element from database
        """
        return User.query.all()
    # return user with id==id
    @staticmethod
    def get_by_id(user_id:str)->User:

        try:
            user =User.query.get(uuid.UUID(user_id))
        except ValueError :
            abort(401,"valueror") 
        if user:
            return user
        abort(404,'user not found')
    
    
    @staticmethod 
    def create_user(data):
        try:
            user=User(
                name=data.get('name'),
                email=data.get('email'),
            )
            db.session.add(user)
            db.session.commit()
        except SQLAlchemyError:
            abort(300,'input user error')
        return user
    

    @staticmethod
    def update_user(data):
        id=data.get('id')
        name=data.get('name')
        email=data.get('email')
        user =User.query.get(uuid.UUID(id))
        if user :
            user.name=name
            user.email=email
            db.session.commit()
            return user
        abort(404,"user not found")
    
    @staticmethod
    def delete_user(id):
        try:
            user=User.query.get(uuid.UUID(id))
        except ValueError :
            abort(400,'id user by hex value')
        
        if user:
            return user
        abort(404,'user Not Found')
    
    @staticmethod
    def delete():
        User.query.delete()
        db.session.commit()
        return {'message':'db vider'}