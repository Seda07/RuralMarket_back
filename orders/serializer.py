from rest_framework import serializers
from .models import Order, CustomUser

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['user', 'order_date']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user

        return Order.objects.create(**validated_data)

    def validate(self, data):
        user = self.context['request'].user
        missing_fields = []

        if not isinstance(user, CustomUser):
            raise serializers.ValidationError({"message": "Usuario no válido."})

        if not user.first_name:
            missing_fields.append("first_name")
        if not user.address:
            missing_fields.append("address")
        if not user.phone:
            missing_fields.append("phone")

        if missing_fields:

            raise serializers.ValidationError({
                "missing_fields": missing_fields,
                "message": "Por favor completa tu información antes de realizar la compra."
            })

        return data
