from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(required=False)  # Puede cambiarse a FileField si necesario
    category_name = serializers.CharField(source='category.name', read_only=True)
    seller_first_name = serializers.CharField(source='seller.first_name', read_only=True)  # Nombre del vendedor

    class Meta:
        model = Product
        fields = ['name', 'category', 'category_name', 'description', 'price', 'stock', 'photo', 'seller',
                  'seller_first_name']

    # Validación del stock para no aceptar valores negativos
    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError("El stock no puede ser negativo.")
        return value
