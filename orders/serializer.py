from rest_framework import serializers
from suborders.serializer import SuborderSerializer
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)
    suborders = SuborderSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['user', 'order_date']

