from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField


class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = [
        ('buyer', 'Comprador'),
        ('seller', 'Vendedor'),
        ('admin', 'Administrador'),
    ]

    user_type = models.CharField(
        max_length=10,
        choices=USER_TYPE_CHOICES,
        default='buyer'
    )
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    photo = CloudinaryField('photo', null=True, blank=True)
    user_description = models.CharField(max_length=2500, null=True, blank=True)
    province = models.CharField(max_length=50, null=True, blank=True)
    zip_code = models.CharField(max_length=20, null=True, blank=True)
    register_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '__all__'
