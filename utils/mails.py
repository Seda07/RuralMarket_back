from django.core.mail import send_mail
from django.conf import settings


def send_welcome_email(user):
    subject = 'Bienvenido a nuestro marketplace'
    message = f'Hola {user.username}, gracias por registrarte en RuralMarket.'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user.email]
    send_mail(subject, message, from_email, recipient_list)


def send_order_confirmation_email(order):
    subject = f'Pedido {order.id} creado exitosamente.'
    message = f'Hola {order.user.first_name} tu pedido {order.id} ha sido creado exitosamente.\n'

    total_order_value = 0

    for suborder in order.suborders.all():
        message += f'Vendedor: {suborder.seller.username}\n'

        for suborder_product in suborder.suborder_product.all():
            message += f' - Producto: {suborder_product.product.name}, Cantidad: {suborder_product.quantity}, Precio: {suborder_product.sold_price}\n'
            total_order_value += suborder_product.sold_price * suborder_product.quantity
        message += f'Subtotal: {suborder.subtotal}\n\n'

    message += f'Total del pedido: {total_order_value}\n'

    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [order.user.email]
    send_mail(subject, message, from_email, recipient_list)


def send_seller_order_notification(order, seller):
    subject = 'Nuevo pedido recibido'
    message = f'Has recibido un nuevo pedido {order.id}.\n\nDetalles del pedido:\n'

    message += f'Datos del comprador:\n'
    message += f' - Nombre: {order.user.first_name} {order.user.last_name}\n'
    message += f' - Username: {order.user.username}\n'
    message += f' - Email: {order.user.email}\n'
    message += f' - Teléfono: {order.user.phone}\n'
    message += f' - Dirección: {order.user.address}\n\n'

    for suborder in order.suborders.filter(seller=seller):
        message += f'Suborden para el vendedor: {suborder.seller.username}\n'

        for suborder_product in suborder.suborder_product.all():
            message += f' - Producto: {suborder_product.product.name}, Cantidad: {suborder_product.quantity}, Precio: {suborder_product.sold_price}\n'

        message += f'Subtotal de la suborden: {suborder.subtotal}\n\n'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [seller.email]
    send_mail(subject, message, from_email, recipient_list)
