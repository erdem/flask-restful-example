from datetime import datetime, timedelta

from app import celery
from app.database import db
from app.contacts.models import Contact, ContactEmail
from app.utils import get_random_name, generate_random_emails


@celery.task
def generate_random_contact():
    contact_data = {
        'username': get_random_name(),
        'first_name': get_random_name(),
        'last_name': get_random_name(),
    }
    emails = generate_random_emails(2)

    contact = Contact(**contact_data)
    contact_emails = [ContactEmail(email=email, contact=contact) for email in emails]
    contact.emails.extend(contact_emails)
    db.session.add_all(contact_emails)
    db.session.add(contact)
    db.session.commit()


@celery.task
def clean_contacts():
    now = datetime.now()
    contacts = Contact.query.filter(
        Contact.created_at >= now-timedelta(minutes=100)
    )
    for contact in contacts:
        print(contact.id)
        db.session.delete(contact)
    db.session.commit()
