from rest_framework import serializers
from .models import  CustomUser
from .models import Suborder


class SuborderSerializer(serializers.ModelSerializer):
    order_username = serializers.CharField(source='order.user.username', read_only=True)
    order_email = serializers.EmailField(source='order.user.email', read_only=True)

    class Meta:
        model = Suborder
        fields = ['id', 'order', 'subtotal', 'seller', 'status', 'order_username', 'order_email']


