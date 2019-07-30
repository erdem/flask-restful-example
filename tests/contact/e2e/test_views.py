import json
from http import HTTPStatus

import pytest


def test_retrieve_contact_view(
    session,
    test_client,
    contact_item,
    contact_with_multiple_emails
):
    response = test_client.get('/api/contacts/')
    response_data = response.get_json()
    assert len(response_data) == 2
    assert response_data[0]['username'] == contact_item.username
    assert response_data[1]['username'] == contact_with_multiple_emails.username
    assert response.status_code == HTTPStatus.OK


def test_create_contact_view_validations(test_client):
    response = test_client.post(
        '/api/contacts/',
        data=json.dumps(dict()),
        content_type='application/json'
    )
    errors = response.get_json()
    assert len(errors.keys()) == 4
    assert 'username' in errors.keys()
    assert 'emails' in errors.keys()
    assert 'first_name' in errors.keys()
    assert 'last_name' in errors.keys()

    response = test_client.post(
        '/api/contacts/',
        data=json.dumps({
            'username': 'admin'
        }),
        content_type='application/json'
    )
    errors = response.get_json()
    assert len(errors.keys()) == 3


def test_create_contact_view(test_client, linus_contact_data):
    response = test_client.post(
        '/api/contacts/',
        data=json.dumps(linus_contact_data),
        content_type='application/json'
    )
    response_data = response.get_json()
    assert response.status_code == HTTPStatus.CREATED
    assert 'id' in response_data
    assert response_data['username'] == linus_contact_data['username']


def test_put_update_contact_view(session, test_client, contact_item, knuth_contact_data, guido_contact_data):
    response = test_client.put(
        '/api/contacts/{0}/'.format(contact_item.username),
        data=json.dumps(guido_contact_data),
        content_type='application/json'
    )
    response_data = response.get_json()
    assert response.status_code == HTTPStatus.ACCEPTED
    assert response_data['id'] == contact_item.id
    assert response_data['username'] == guido_contact_data['username']

    # Try to update the contact item with an exists in email
    knuth_contact_data['emails'] = guido_contact_data['emails']
    knuth_contact_data['username'] = 'siteadmin'
    response = test_client.put(
        '/api/contacts/{0}/'.format(contact_item.username),
        data=json.dumps(knuth_contact_data),
        content_type='application/json'
    )
    response_data = response.get_json()
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert 'emails' in response_data


@pytest.mark.parametrize('new_email', ('siteadmin@mail.com', ))
def test_partial_update_view(new_email, session, test_client, contact_item):
    response = test_client.patch(
        '/api/contacts/{0}/'.format(contact_item.username),
        data=json.dumps(
            {
                'emails': [{
                    'email': new_email
                }]
            }
        ),
        content_type='application/json'
    )
    response_data = response.get_json()
    assert response.status_code == HTTPStatus.ACCEPTED
    assert response_data['emails'][0]['email'] == new_email


@pytest.mark.parametrize('new_username', ('newadmin', ))
def test_partial_update_view(new_username, session, test_client, contact_item):
    response = test_client.patch(
        '/api/contacts/{0}/'.format(contact_item.username),
        data=json.dumps(
            {
                'username': new_username
            }
        ),
        content_type='application/json'
    )
    response_data = response.get_json()
    assert response.status_code == HTTPStatus.ACCEPTED
    assert response_data['id'] == contact_item.id

    # Get contact item by new API URI
    item_uri = response_data.get('uri')
    response = test_client.get(item_uri)
    response_data = response.get_json()
    assert response.status_code == HTTPStatus.OK
    assert response_data['username'] == new_username
