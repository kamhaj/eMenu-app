from celery import shared_task
from django.core.management import call_command


@shared_task # decorator that lets you create tasks without having any concrete app instance (reusable)
def send_email_report_task():
    call_command("email_report", )  # programmatically calling django-admin commands  (eMenu/management/...)

    
@shared_task
def dummy_task():
    print("I am a dummy task run by Celery!")
    return None