from django.db.models.signals import post_save
from django.dispatch import receiver
from utils.mails import send_welcome_email
from .models import CustomUser

@receiver(post_save, sender=CustomUser)
def handle_user_created(sender, instance, created, **kwargs):
    if created:
        send_welcome_email(instance)
