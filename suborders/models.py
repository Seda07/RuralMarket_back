from django.db import models
from users.models import CustomUser
from orders.models import Order


class Suborder(models.Model):
    order = models.ForeignKey(Order, related_name="suborders", on_delete=models.CASCADE, null=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    seller = models.ForeignKey(CustomUser, related_name="seller_suborder", on_delete=models.CASCADE)
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
        return f'Orden de {self.seller.username} número {self.order.id}'

