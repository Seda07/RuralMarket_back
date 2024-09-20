from cloudinary.models import CloudinaryField
from django.db import models
from rest_framework.exceptions import ValidationError
from category.models import Category
from users.models import CustomUser
class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = CloudinaryField('image', null=True, blank=True)
    seller = models.ForeignKey(CustomUser, related_name="product", on_delete=models.CASCADE)

    def clean(self):
        if self.stock < 0:
            raise ValidationError('El stock no puede ser negativo')

    def __str__(self):
        return self.name


