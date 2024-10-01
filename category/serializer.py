from rest_framework import serializers
from .models import Category
from .validations import validate_category_name


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def validate_name(self, value):
        return validate_category_name(value)

