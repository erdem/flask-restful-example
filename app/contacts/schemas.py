from marshmallow import Schema, fields, post_load, validates, ValidationError, pre_dump

from app import db
from app.utils import get_config
from app.contacts.models import Contact, ContactEmail


class ContactEmailSchema(Schema):
    email = fields.Email(required=True)
    created_at = fields.DateTime(dump_only=True)


class ContactSchema(Schema):
    id = fields.Integer(dump_only=True)
    username = fields.Str(required=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    emails = fields.Nested(ContactEmailSchema, many=True, required=True)
    created_at = fields.DateTime(dump_only=True)
    uri = fields.Method("get_item_uri")

    def get_item_uri(self, obj):
        config = get_config()
        return '{config.DOMAIN}/api/contacts/{obj.username}/'.format(
            obj=obj,
            config=config
        )

    @validates('username')
    def validate_username(self, username, **kwargs):
        if bool(Contact.query.filter_by(username=username).first()):
            raise ValidationError(
                '"{username}" username already exists, '
                'please use a different username.'.format(username=username)
            )

    @post_load
    def create_contact(self, data):
        email_list = data.pop('emails', list())
        contact = Contact(**data)
        contact_emails = [ContactEmail(email=d.get('email')) for d in email_list]
        contact.emails.extend(contact_emails)
        db.session.add(contact)
        db.session.add_all(contact_emails)
        db.session.commit()
        self.instance = contact

    def update_contact(self, contact, data):
        contact.username = data.get('username', contact.username)
        contact.first_name = data.get('first_name', contact.first_name)
        contact.last_name = data.get('last_name', contact.last_name)
        emails = data.get('emails')
        if emails:
            ContactEmail.query.filter_by(contact_id=contact.id).delete()
            db.session.commit()
            new_contact_emails = [ContactEmail(email=d.get('email')) for d in emails]
            contact.emails.extend(new_contact_emails)
            db.session.add_all(new_contact_emails)
        db.session.commit()
