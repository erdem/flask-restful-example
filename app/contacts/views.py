from flask import Blueprint, jsonify
from flask import request


contacts_api = Blueprint('contacts_api', __name__)


@contacts_api.route('/', methods=["GET"])
@contacts_api.route('/<string:username>/', methods=["GET"])
def retrieve_contacts(username=None):
    from app.contacts.models import Contact
    from app.contacts.schemas import ContactSchema

    if username:
        contact = Contact.query.filter_by(username=username).first_or_404()
        schema = ContactSchema().dump(contact)
        return jsonify(schema.data), 200

    contacts = Contact.query.all()
    schema = ContactSchema(many=True).dump(contacts)
    return jsonify(schema.data), 200


@contacts_api.route('/', methods=["POST"])
def create_contact():
    from app.contacts.schemas import ContactSchema

    data = request.get_json()
    schema = ContactSchema().load(data)

    if schema.errors:
        return jsonify(schema.errors), 400
    return jsonify(schema.data), 201


@contacts_api.route('/<string:username>/', methods=["PUT"])
def update_contact(username):
    from app.contacts.schemas import ContactSchema
    from app.contacts.models import Contact

    contact = Contact.query.filter_by(username=username).first_or_404()

    data = request.get_json()

    schema = ContactSchema()
    schema.update_only = True
    errors = schema.validate(data, partial=True)

    if errors:
        return jsonify(errors), 400

    schema.update_contact(contact, data)
    updated_contact = Contact.query.filter_by(username=username).first()
    return jsonify(ContactSchema().dump(updated_contact)), 202
