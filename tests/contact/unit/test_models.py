from app.contacts.models import Contact, ContactEmail


def test_contact_email_count():
    contact = Contact(
        username='admin',
        first_name='Guido',
        last_name='van Rossum'
    )
    contact_emails = [
        ContactEmail(email='newadmin@mail.com'),
        ContactEmail(email='adminnew@mail.com')
    ]
    contact.emails.extend(contact_emails)
    assert len(contact.emails) == 2


def test_append_contact_email():
    contact = Contact(
        username='admin',
        first_name='Guido',
        last_name='van Rossum',
        emails= [
            ContactEmail(email='newadmin@mail.com'),
        ]
    )
    contact.emails.append(ContactEmail(email='adminnew@mail.com'))
    assert len(contact.emails) == 2
