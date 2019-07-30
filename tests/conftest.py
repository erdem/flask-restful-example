import os
import pytest

from app import create_app
from app.database import db as db_instance


os.environ["FLASK_CONFIG"] = 'testing'


@pytest.yield_fixture(scope='session')
def app():
    app = create_app(config_name='testing')

    with app.app_context():
        yield app


@pytest.fixture
def app_context(app):
    with app.app_context() as ctx:
        yield ctx


@pytest.fixture
def test_client(app, app_context):
    return app.test_client()


@pytest.yield_fixture(scope='session')
def db(app):
    with app.app_context():
        db_instance.drop_all()
        db_instance.create_all()
        yield db_instance



@pytest.yield_fixture(scope="class", autouse=True)
def session(app, db, request):
    """
    Returns function-scoped session.
    """
    with app.app_context():
        conn = db_instance.engine.connect()
        txn = conn.begin()

        options = dict(bind=conn, binds={})
        sess = db_instance.create_scoped_session(options=options)

        db_instance.session = sess
        yield sess

        sess.remove()
        # This instruction rollsback any commit that were executed in the tests.
        txn.rollback()