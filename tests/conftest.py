import os
import pytest

from app import create_app


os.environ["FLASK_CONFIG"] = 'testing'


@pytest.yield_fixture(scope='session')
def app():
    app = create_app(config_name='testing')
    from app.database import db as db_instance

    with app.app_context():
        yield app
        db_instance.drop_all()


@pytest.fixture
def app_context(app):
    with app.app_context() as ctx:
        yield ctx


@pytest.fixture
def test_client(app, app_context):
    return app.test_client()


@pytest.yield_fixture(scope='session')
def db(app):
    from app.database import db as db_instance
    yield db_instance
    db_instance.drop_all()
