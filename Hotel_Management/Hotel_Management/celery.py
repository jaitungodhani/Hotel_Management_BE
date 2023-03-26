import os

from celery import Celery
from django.core.mail import EmailMessage
from django.conf import settings
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Hotel_Management.settings')

app = Celery('Hotel_Management')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def send_mail(self, subject, body, recipient, content_subtype="plain"):
    mail = EmailMessage(
        subject,
        body,
        settings.DEFAULT_SERVER_EMAIL,
        [recipient],
    )
    mail.content_subtype = content_subtype
    mail.send(fail_silently=False)