from celery import Celery
from flask import Flask

from app.utils import get_config


Config = get_config()
celery = Celery(__name__, broker=Config.CELERY_BROKER_URL)


def create_app(config_name=None, **kwargs):
    """
    Entry point to the Flask RESTful Server application.
    """
    from app.database import init_db
    from app.contacts.views import contacts_api

    app = Flask(__name__, **kwargs)

    try:
        app.config.from_object(get_config(config_name))
    except ImportError:
        raise Exception('Invalid Config')

    app.register_blueprint(contacts_api, url_prefix='/api/contacts/')

    init_db(app)
    celery.conf.update(app.config)
    return app

from app.contacts import models