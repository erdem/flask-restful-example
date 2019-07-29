import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.contacts.views import contacts_api

CONFIG_NAME_MAPPER = {
    'development': 'config.DevelopmentConfig',
    'testing': 'config.TestingConfig',
}

db = SQLAlchemy()


def create_app(config_name=None, **kwargs):
    """
    Entry point to the Flask RESTful Server application.
    """

    app = Flask(__name__, **kwargs)

    flask_config_name = os.getenv('FLASK_CONFIG', 'development')
    if config_name is not None:
        flask_config_name = config_name

    try:
        app.config.from_object(CONFIG_NAME_MAPPER[flask_config_name])
    except ImportError:
        raise Exception('Invalid Config')

    app.register_blueprint(contacts_api, url_prefix='/api/contacts/')

    with app.app_context():
        db.init_app(app)
        db.create_all()
    return app

from app.contacts import models