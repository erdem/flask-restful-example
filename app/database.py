from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def init_db(app):
    with app.app_context():
        db.init_app(app)
        db.create_all()
