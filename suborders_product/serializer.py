from rest_framework import serializers
from .models import SuborderProduct


class SuborderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuborderProduct
        fields = '__all__'
        read_only_fields = ['seller', 'order_id']
