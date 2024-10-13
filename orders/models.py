from django.db import models
from users.models import CustomUser
from cart.models import Cart


class Order(models.Model):
    cart = models.ForeignKey(Cart, related_name="order", on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
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
    user = models.ForeignKey(CustomUser, related_name="order", on_delete=models.CASCADE)

    def __str__(self):
        return f'Orden de {self.user.username} número {self.id} creada en {self.order_date}'

