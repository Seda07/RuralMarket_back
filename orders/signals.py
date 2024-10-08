from django.db.models.signals import post_save
from django.dispatch import receiver
from orders.models import Order
from utils.mails import send_seller_order_notification

@receiver(post_save, sender=Order)
def order_created(sender, instance, created, **kwargs):
    if created:
        sellers = {suborder.seller for suborder in instance.suborders.all()}
        for seller in sellers:
            send_seller_order_notification(instance, seller)
