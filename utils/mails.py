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
    recipient_list = [order.user.email]
    send_mail(subject, message, from_email, recipient_list)

def send_seller_order_notification(order, seller):
    subject = 'Nuevo pedido recibido'
    message = f'Has recibido un nuevo pedido {order.id}.\n\nDetalles del pedido:\n'

    # Obtener productos relacionados con el pedido y el vendedor
    suborders = order.suborder_set.filter(seller=seller)

    for suborder in suborders:
        for product in suborder.suborderproduct_set.all():
            message += f"- {product.product.name}: {product.quantity} x ${product.sold_price} = ${product.sold_price * product.quantity}\n"

    message += "\n¡Gracias por vender en nuestro marketplace!"

    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [seller.email]  # Asegúrate de que el vendedor tenga un campo email
    send_mail(subject, message, from_email, recipient_list)
