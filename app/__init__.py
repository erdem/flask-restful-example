from flask import Flask

from app.contacts.views import contacts_api
from app.utils import get_config


def create_app(config_name=None, **kwargs):
    """
    Entry point to the Flask RESTful Server application.
    """
    from app.database import init_db

    app = Flask(__name__, **kwargs)

    try:
        app.config.from_object(get_config(config_name))
    except ImportError:
        raise Exception('Invalid Config')

    app.register_blueprint(contacts_api, url_prefix='/api/contacts/')

    init_db(app)

    return app

from app.contacts import models