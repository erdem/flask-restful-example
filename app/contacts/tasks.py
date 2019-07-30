from datetime import datetime, timedelta

from app import celery
from app.database import db
from app.contacts.models import Contact, ContactEmail
from app.utils import get_random_name, generate_random_emails


@celery.task
def generate_random_contacts():
    contact_data = {
        'username': get_random_name(),
        'first_name': get_random_name(),
        'last_name': get_random_name(),
    }
    emails = generate_random_emails(2)
    contact = Contact(**contact_data)
    contact_emails = [ContactEmail(email=email) for email in emails]
    contact.emails.extend(contact_emails)
    db.session.add(contact)
    db.session.add_all(contact_emails)
    db.session.commit()


@celery.task
def clean_contacts():
    now = datetime.now()
    Contact.query.filter(
        Contact.created_at >= now-timedelta(minutes=1)
    ).delete()
    db.session.commit()
