import os
import random
import string

from werkzeug.utils import import_string

CONFIG_NAME_MAPPER = {
    'development': 'config.DevelopmentConfig',
    'testing': 'config.TestingConfig',
}


def get_config(config_name=None):
    flask_config_name = os.getenv('FLASK_CONFIG', 'development')
    if config_name is not None:
        flask_config_name = config_name
    return import_string(CONFIG_NAME_MAPPER[flask_config_name])


DOMAINS = ('hotmail.com', 'gmail.com', 'aol.com', 'mail.com', 'mail.kz', 'yahoo.com')


def get_random_domain(domains):
    return random.choice(domains)


def get_random_name():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(random.randint(5, 20)))


def generate_random_emails(number):
    random_emails = []
    for i in range(number):
        random_name = get_random_name()
        random_domain = get_random_domain(DOMAINS)
        random_email = random_name + '@' + random_domain
        random_emails.append(random_email)
    return random_emails
