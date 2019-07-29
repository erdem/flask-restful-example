from app import get_config


def test_utils():
    config = get_config()
    assert config.ENV == 'testing'

    config = get_config(config_name='development')
    assert config.ENV == 'development'