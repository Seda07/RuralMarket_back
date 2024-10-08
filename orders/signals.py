from django.db.models.signals import post_save
from django.dispatch import receiver
from orders.models import Order
from utils.mails import send_order_confirmation_email, send_seller_order_notification

@receiver(post_save, sender=Order)
def order_created(sender, instance, created, **kwargs):
    if created:
        # Enviar correo al comprador
        send_order_confirmation_email(instance)

        # Enviar correo a cada vendedor involucrado en el pedido
        sellers = {suborder.seller for suborder in instance.suborders.all()}  # Conjunto de vendedores
        for seller in sellers:
            send_seller_order_notification(instance, seller)
