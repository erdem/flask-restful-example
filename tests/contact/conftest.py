import pytest

from app.contacts.models import ContactEmail, Contact


@pytest.fixture()
def contact_email_1(session):
    return ContactEmail(email='johnwilliam@mail.com')


@pytest.fixture()
def contact_email_2(session):
    return ContactEmail(email='williamjohn@mail.com')


@pytest.yield_fixture()
def contact_with_multiple_emails(session, contact_email_1, contact_email_2):
    contact = Contact(
        username='john',
        first_name='John',
        last_name='William',
    )

    contact_emails = [contact_email_1, contact_email_2]

    contact.emails.extend(contact_emails)
    session.add(contact)
    session.add_all(contact_emails)
    yield contact

    # Cleanup
    Contact.query.filter(Contact.username == contact.username).delete()


@pytest.yield_fixture()
def contact_item(session):
    contact = Contact(
        username='sam',
        first_name='Sam',
        last_name='Henry',
    )

    contact_emails = [
        ContactEmail(email='samhenry@mail.com')
    ]

    contact.emails.extend(contact_emails)
    session.add(contact)
    session.add_all(contact_emails)
    yield contact

    # Cleanup
    Contact.query.filter(Contact.username == contact.username).delete()


@pytest.fixture()
def guido_contact_data():
    return {
        'username': 'guido',
        'first_name': 'Guido',
        'last_name': 'van Rossum',
        'emails': [
            {
                'email': 'guido@mail.com'
            }
        ]
    }

@pytest.fixture()
def knuth_contact_data():
    return {
        'username': 'donald',
        'first_name': 'Donald',
        'last_name': 'Knuth',
        'emails': [
            {
                'email': 'knuth@mail.com',
            },
            {
                'email': 'donald@mail.com'
            }
        ]
    }

@pytest.fixture()
def linus_contact_data():
    return {
        'username': 'linus',
        'first_name': 'Linus',
        'last_name': 'Torvalds',
        'emails': [
            {
                'email': 'linus@mail.com',
            }
        ]
    }