from rest_framework import serializers
from products.models import Product
from .models import Cart, CartItem
from products.serializer import ProductSerializer


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True, source='product')

    class Meta:
        model = CartItem
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    buyer = serializers.StringRelatedField()

    class Meta:
        model = Cart
        fields = '__all__'


