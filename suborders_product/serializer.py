from rest_framework import serializers
from .models import SuborderProduct


class SuborderProductSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name', read_only=True)
    class Meta:
        model = SuborderProduct
        fields = '__all__'

