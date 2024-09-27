from django.db import models
from users.models import CustomUser
from orders.models import Order


class Suborder(models.Model):
    order_id = models.ForeignKey(Order, related_name="suborder", on_delete=models.CASCADE)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    seller = models.ForeignKey(CustomUser, related_name="suborder", on_delete=models.CASCADE)
    STATUS_TYPE_CHOICES = [
        ('pending', 'Pendiente'),
        ('completed', 'Finalizada'),
        ('cancelled', 'Cancelada'),
    ]
    status = models.CharField(
        max_length=10,
        choices=STATUS_TYPE_CHOICES,
        default='pending'
    )


    def __str__(self):
        return f'Orden de {self.Order.username} número {self.orden_id}'

