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


@pytest.fixture(scope='session')
def temp_db_instance_helper(db):
    def temp_db_instance_manager(instance):
        with db.session.begin():
            db.session.add(instance)

        yield instance

        mapper = instance.__class__.__mapper__
        assert len(mapper.primary_key) == 1
        instance.__class__.query\
            .filter(mapper.primary_key[0] == mapper.primary_key_from_instance(instance)[0])\
            .delete()

    return temp_db_instance_manager
