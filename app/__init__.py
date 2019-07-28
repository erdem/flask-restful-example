import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.contacts.views import contacts_api

CONFIG_NAME_MAPPER = {
    'development': 'config.DevelopmentConfig',
    'testing': 'config.TestingConfig',
}

def create_app(config_name=None, **kwargs):
    """
    Entry point to the Flask RESTful Server application.
    """

    app = Flask(__name__, **kwargs)
    app.register_blueprint(contacts_api, url_prefix='/api/contacts/')

    flask_config_name = os.getenv('FLASK_CONFIG', 'development')
    if config_name is not None:
        flask_config_name = config_name

    try:
        app.config.from_object(CONFIG_NAME_MAPPER[flask_config_name])
    except ImportError:
        raise Exception('Invalid Config')

    db = SQLAlchemy(app)
    db.create_all()
    return app
