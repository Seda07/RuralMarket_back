from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(required=False)

    class Meta:
        model = Product
        fields = ['name', 'category', 'description', 'price', 'stock', 'photo', 'seller']

    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError("El stock no puede ser negativo.")
        return value



