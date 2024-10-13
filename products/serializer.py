from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(required=False)
    category_name = serializers.CharField(source='category.name', read_only=True)
    seller_first_name = serializers.CharField(source='seller.first_name', read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'category_name', 'description', 'price', 'stock', 'photo', 'seller',
                  'seller_first_name']

