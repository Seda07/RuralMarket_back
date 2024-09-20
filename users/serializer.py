from .models import CustomUser
from rest_framework import serializers
from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    photo = serializers.ImageField(required=False, allow_null=True)
    user_description = serializers.CharField(required=False, allow_blank=True, max_length=2500)
    province = serializers.CharField(required=False, allow_blank=True, max_length=50)
    zip_code = serializers.CharField(required=False, allow_blank=True, max_length=20)

    class Meta:
        model = CustomUser
        fields = [
            'username', 'email', 'password', 'user_type', 'phone',
            'address', 'photo', 'user_description', 'province',
            'zip_code', 'register_date'
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'register_date': {'read_only': True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser.objects.create_user(
            **validated_data,
            password=password
        )
        return user

