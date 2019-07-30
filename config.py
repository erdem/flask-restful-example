import os


class BaseConfig:
    DEBUG=False
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % (os.path.join(PROJECT_ROOT, "db.sqlite3"))
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(BaseConfig):
    ENV='development'
    DEBUG = True
    DOMAIN = 'http://localhost:5000'
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/1'


class TestingConfig(BaseConfig):
    ENV='testing'
    TESTING = True
    DOMAIN = 'http://testserver'

    # Use memory for DB files
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

