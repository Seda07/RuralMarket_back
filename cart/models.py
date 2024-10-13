from django.db import models
from users.models import CustomUser
from products.models import Product


class Cart(models.Model):
    user = models.ForeignKey(CustomUser, related_name="cart", on_delete=models.CASCADE, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Carrito de {self.user.username} creado en {self.date_created}'


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name="cart_items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="product", on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.quantity} x {self.product.name} en carrito {self.cart.id}'





