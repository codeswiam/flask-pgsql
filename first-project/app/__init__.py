from flask import Flask
from app.modules import hello, goodbye
from app.config import Config
from flask_migrate import Migrate
from app.database import db

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY="1234"
    )

    app.config.from_object(Config)

    # Database related part
    db.init_app(app)
    from app.models.user import User
    from app.models.car import Car
    migrate = Migrate(app, db)

    app.register_blueprint(hello.blueprint)
    app.register_blueprint(goodbye.blueprint)

    return app