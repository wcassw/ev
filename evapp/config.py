from urllib.parse import quote
from sqlalchemy.engine import create_engine
import os

class BaseConfig(object):
    TESTING = False
    UPLOAD_FOLDER = 'static/uploads'  # changed to relative path
    TEMPLATE = 'static/template'  # changed to relative path
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    VERSION = ''
    DBNAME = 'template.db'
    SECRET_KEY = os.urandom(32) # "you-will-never-guess"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLAlCHEMY_ECHO = False
    DEBUG = False
    
    os.environ["SQLALCHEMY_TRACK_MODIFICATIONS"] = "False"
    os.environ["MAIL_USE_SSL"] = "True"
    os.environ["DBNAME"] = "template.db"
    os.environ["DEBUG"] = "False"
    os.environ["FLASK_ENV"] = 'development'

class DevelopmentConfig(BaseConfig):
    # DB
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:{CREDS}@localhost:3306/{DBNAME}'.format(quote('s!ldfans'), DBNAME)
    DB_SERVER = 'localhost'
    # DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(BaseConfig.DBNAME)
    DEBUG = True


class TestingConfig(BaseConfig):
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:%s@localhost:3306/flask_new_testing' % quote('s!ldfans')
    DB_SERVER = 'localhost'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}.test'.format(BaseConfig.DBNAME)
    TESTING = True
    WTF_CSRF_ENABLED = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(BaseConfig):
    DB_SERVER = '192.168.1.201'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:%s@localhost:3306/flask_new' % quote('s!ldfans')
    DEBUG = False


config_setting = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}

# https://flask.palletsprojects.com/en/1.1.x/config/
# How the flask app.config.from_object work
