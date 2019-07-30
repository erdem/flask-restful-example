import sqlalchemy
from sqlalchemy.orm import sessionmaker

from app import celery, create_app
from app.utils import get_config



Config = get_config()


def connect():
    """Connects to the database and return a session"""

    uri = Config.SQLALCHEMY_DATABASE_URI

    # The return value of create_engine() is our connection object
    con = sqlalchemy.create_engine(uri)

    # create a Session
    Session = sessionmaker(bind=con)
    session = Session()

    return con, session

con, session = connect()

app = create_app(config_name='development')
app.app_context().push()
