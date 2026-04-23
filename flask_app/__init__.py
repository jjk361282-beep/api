from apiflask import APIFlask
from exts import db, migrate
def create_app():
    app=APIFlask(__name__)
    app.config['SQLACHEMY_DATABASE_URI']="sqlite:///test.db"

    db.init_app(app)
    migrate.init_app(app,db)
    return app