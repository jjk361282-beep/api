from apiflask import APIFlask,abort
from schema import UserIn,UserOut
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app=APIFlask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///dev.db"
db=SQLAlchemy()
db.init_app(app)
migrate=Migrate(app,db)

from models import User
@app.get('/')
def hello():
    return "hello api"

@app.get('/user/')
@app.output(UserOut)
def set_user_all():
    return User.query.all()

@app.get('/user/<int:id>')
@app.output(UserOut)
def get_user_id(id):
    user= User.query.get(id)
    if user:
        return user
    abort(404)

@app.put("/user/<int:id>")
@app.input(UserIn)
@app.output(UserOut)
def update_user(id,json_data):
    user1=User.query.get(id)
    if user1:
        user1.name=json_data.get('name')
        user1.email=json_data.get('email')
        
        db.session.commit()
        return user1
    abort(401)

@app.post('/user/')
@app.input(UserIn)
@app.output(UserOut)
def create_user(json_data):
    user= User(name=json_data.get('name'),email=json_data.get('email'))
    db.session.add(user)
    db.session.commit()
    return user




@app.delete("/user/<int:id>")
@app.output(UserOut)
def delete(id):
    user=User.query.get(id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return user
    abort(404)

@app.delete('/user/')
def delete_all_user():
    User.query.delete()
    db.session.commit()
    return {'message':"ok"}