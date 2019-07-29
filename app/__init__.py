import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.contacts.views import contacts_api
from app.utils import get_config

db = SQLAlchemy()


def create_app(config_name=None, **kwargs):
    """
    Entry point to the Flask RESTful Server application.
    """

    app = Flask(__name__, **kwargs)

    try:
        app.config.from_object(get_config(config_name))
    except ImportError:
        raise Exception('Invalid Config')

    app.register_blueprint(contacts_api, url_prefix='/api/contacts/')

    with app.app_context():
        db.init_app(app)
        db.create_all()
    return app

from app.contacts import models