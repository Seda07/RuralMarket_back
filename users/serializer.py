from .models import CustomUser
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    photo = serializers.ImageField(required=False, allow_null=True)
    user_description = serializers.CharField(required=False, allow_blank=True, max_length=2500)
    province = serializers.CharField(required=False, allow_blank=True, max_length=50)
    zip_code = serializers.CharField(required=False, allow_blank=True, max_length=20)
    first_name = serializers.CharField(required=True, max_length=30)

    class Meta:
        model = CustomUser
        fields = [
            'first_name','username', 'email', 'password', 'user_type', 'phone',
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


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.photo and hasattr(instance.photo, 'url'):
            representation['photo'] = instance.photo.url
        else:
            representation['photo'] = None
        return representation


class UserUpdateSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(write_only=True, required=False)
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)
    photo = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = CustomUser
        fields = "__all__"

    def validate(self, data):
        if 'password' in data:
            if 'confirm_password' not in data:
                raise serializers.ValidationError({"confirm_password": "Debes confirmar la nueva contraseña."})
            if data['password'] != data['confirm_password']:
                raise serializers.ValidationError({"password": "Las contraseñas deben coincidir."})
        return data

    def update(self, instance, validated_data):

        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.address = validated_data.get('address', instance.address)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.user_description = validated_data.get('user_description', instance.user_description)
        instance.province = validated_data.get('province', instance.province)
        instance.zip_code = validated_data.get('zip_code', instance.zip_code)



        if 'photo' in validated_data:
            instance.photo = validated_data.get('photo', instance.photo)

        password = validated_data.get('password')
        if password:
            instance.set_password(password)

        instance.save()
        return instance

