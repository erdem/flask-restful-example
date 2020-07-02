Flask Example
=============

This repository contains the example code for a contact API project, using SQLAlchemy, PyTest, Celery with Flask.


### Tasks
- Model a Contact with username, email, first name and surname.
- Create a Restful API that returns a list of all contacts.
- Returns a contact by username.
- Saves a Contact.
- Updates a Contact
- Deletes a Contact
- Allow a contact to have multiple email addresses.  Adjust GET, POST, PUT, DEL methods to the new sub entity.
- Extend the GET to also accept the email address for contact retrieval.
- Implement a celery task to create a random contact with two email addresses every 15 seconds. Any older entries then 1 min should be cleaned up and deleted.


Setup
-----

1. Clone this repository.
2. Create a virtualenv and activate.
3. Install requirement packages. 
4. Make sure `redis-server` running on background.
5. Set `FLASK_ENV` environment variable as `development`. (`export FLASK_ENV=development`)
6. Open a second terminal and start celery: `celery worker -A celery_worker.celery --loglevel=info`.
7. Open a third terminal and start celery-beat: `celery -A celery_worker:celery beat --loglevel=INFO`.
8. Start the Flask application on your original terminal window: `flask run`.
9. Go to `http://localhost:5000/api/contacts/` and enjoy!

> You can run the tests with `pytest tests` command.

Some example usage for Contact API
----------------------------------

##### Creating a contact entity 

```bash
curl -X POST \
  http://localhost:5000/api/contacts/ \
  -H 'Content-Type: application/json' \
  -d '{
	"username": "admin",
	"first_name": "Armin",
	"last_name": "Ronacher",
	"emails": [
		{"email": "arminronacher@mail.com"}
	]
}'
```

##### Updating a contact entity 

```bash
curl -X PATCH \
  http://localhost:5000/api/contacts/admin/ \
  -H 'Content-Type: application/json' \
  -d '{
	"emails": [
		{"email": "admin@mail.com"}
	]
}'
```

##### Get list of contacts by username

```bash
curl -X GET http://localhost:5000/api/contacts/admin/
```
