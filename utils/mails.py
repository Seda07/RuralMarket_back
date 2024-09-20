from django.core.mail import send_mail
from django.conf import settings

def send_welcome_email(user):
    subject = 'Bienvenido a nuestro marketplace'
    message = f'Hola {user.username}, gracias por registrarte.'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user.email]
    send_mail(subject, message, from_email, recipient_list)

def send_order_confirmation_email(order):
    subject = 'Confirmación de pedido'
    message = f'Tu pedido {order.id} ha sido creado exitosamente.'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [order.buyer.email]
    send_mail(subject, message, from_email, recipient_list)

def send_seller_order_notification(order):
    subject = 'Nuevo pedido recibido'
    message = f'Has recibido un nuevo pedido {order.id}.'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [order.seller.email]
    send_mail(subject, message, from_email, recipient_list)
