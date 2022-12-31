from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from evapp import config
from flask_cors import CORS
from evapp.models import db

def intial_app(config_name='development'):

    app = Flask(__name__, instance_relative_config=True)

    CORS(app)

    app.config.from_object(config.DevelopmentConfig())  # object-based default configuration
    # app.config.from_pyfile('flask.cfg', silent=True)  # instance-folders configuration

    db.init_app(app)

    from evapp.users.views import users_blueprint # bp_user
    app.register_blueprint(users_blueprint, url_prefix='/user')

    with app.app_context():
        # db.drop_all()
        db.create_all()

    return app
