Flask Example
=============

This repository contains the example code for a flask project, using SQLAlchemy, PyTest, Celery with Flask.


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
9. Go to `http://localhost:5000/` and enjoy!
