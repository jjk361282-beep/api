from apiflask import APIFlask
from .exts import db, migrate
from .routes.user_routes import userBlueprint
from .routes.post_routes import postBp


def create_app():
    app=APIFlask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///test.db"


    db.init_app(app)
    migrate.init_app(app,db)

    # add of endpionts
    app.register_blueprint(userBlueprint)
    app.register_blueprint(postBp)

    return app