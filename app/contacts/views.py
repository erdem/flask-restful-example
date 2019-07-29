from flask import Blueprint, jsonify
from flask import request


contacts_api = Blueprint('contacts_api', __name__)


@contacts_api.route('/', methods=["GET"])
@contacts_api.route('/<int:contact_id>/', methods=["GET"])
def retrieve_contacts(contact_id=None):
    from app.contacts.models import Contact
    from app.contacts.schemas import ContactSchema

    if contact_id:
        return str(contact_id)
    contacts = Contact.query.all()
    schema = ContactSchema(many=True).dump(contacts)
    return jsonify(schema.data)


@contacts_api.route('/', methods=["POST"])
def create_contact():
    from app.contacts.schemas import ContactSchema

    data = request.get_json()
    schema = ContactSchema().load(data)

    if schema.errors:
        return jsonify(schema.errors)
    return jsonify(schema.data)
