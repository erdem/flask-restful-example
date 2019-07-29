from datetime import datetime

from app import db


class Contact(db.Model):
    __tablename__ = 'contact'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(length=20), unique=True, index=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String(120))
    created_at = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return (
            '<{class_name}('
            'contact_id={self.id}, '
            'username="{self.username}")>'.format(
                class_name=self.__class__.__name__,
                self=self
            )
        )
