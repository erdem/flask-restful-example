from app import celery


@celery.task
def send_async_email(msg):
    print(msg)


def send_email(to, subject, template, **kwargs):
    send_async_email.delay(to)