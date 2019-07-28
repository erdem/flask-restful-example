from flask import Blueprint

contacts_api = Blueprint('contacts_api', __name__)

@contacts_api.route('/', methods=["GET"])
@contacts_api.route('/<int:contact_id>/', methods=["GET"])
def retrieve_contacts(contact_id=None):
    if contact_id:
        return str(contact_id)
    return 'READ'

# @contacts_api.route('/', methods=["POST"])
# def retrieve_contact():
#     return 'CREATE'
#
# @contacts_api.route('/', methods=["PUT"])
# def retrieve_contact():
#     return 'CREATE'