from marshmallow.validate import Email

from app import get_config
from app.utils import DOMAINS, get_random_domain, generate_random_emails


def test_get_config():
    config = get_config()
    assert config.ENV == 'testing'

    config = get_config(config_name='development')
    assert config.ENV == 'development'


def test_get_random_domain():
    domain = get_random_domain(DOMAINS)
    assert domain in DOMAINS


def test_generate_random_emails():
    emails = generate_random_emails(2)
    assert len(emails) == 2
    assert Email()(emails[0]) == emails[0]
