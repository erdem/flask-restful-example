from app.contacts.models import Contact
from app.contacts.tasks import generate_random_contact, clean_contacts


def test_generate_random_emails(session):
    assert Contact.query.count() == 0
    generate_random_contact()
    assert Contact.query.count() == 1


def test_clean_contacts(session, contact_item, contact_with_multiple_emails):
    assert Contact.query.count() == 2
    clean_contacts()
    assert Contact.query.count() == 0

