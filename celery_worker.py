from app import celery, create_app

app = create_app(config_name='development')
app.app_context().push()
