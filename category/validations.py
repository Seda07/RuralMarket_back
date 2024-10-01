from .models import Category
from rest_framework import serializers


def validate_category_name(value):

    if Category.objects.filter(name__iexact=value.strip()).exists():
        raise serializers.ValidationError("Este nombre de categoría ya existe.")
    return value.strip()