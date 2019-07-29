from marshmallow import Schema, fields, post_load, validates, ValidationError

from app import db
from app.contacts.models import Contact


class ContactSchema(Schema):
    id = fields.Integer(dump_only=True)
    username = fields.Str(required=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    email = fields.Email(required=True)
    created_at = fields.DateTime(dump_only=True)

    @validates('username')
    def validate_username(self, username):
        if bool(Contact.query.filter_by(username=username).first()):
            raise ValidationError(
                '"{username}" username already exists, '
                'please use a different username.'.format(username=username)
            )

    @post_load
    def create_contact(self, data):
        contact = Contact(**data)
        db.session.add(contact)
        db.session.commit()
