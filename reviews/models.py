from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from suborders_product.models import SuborderProduct
from users.models import CustomUser


class Review(models.Model):
    comment = models.CharField(max_length=300)
    suborders_product = models.ForeignKey(SuborderProduct, related_name='reviews_products', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, related_name='reviews_products', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=False)

    def __str__(self):
        return f'{self.CustomUser.username}'
