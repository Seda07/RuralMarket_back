from django.db import models
from products.models import Product
from suborders.models import Suborder


class SuborderProduct(models.Model):
    suborder = models.ForeignKey(Suborder, related_name="suborder_product", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="suborder_product", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    sold_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Suborden {self.suborder.id} - {self.quantity} x {self.product.name}'

