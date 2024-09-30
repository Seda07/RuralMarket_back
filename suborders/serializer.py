from rest_framework import serializers
from .models import  CustomUser
from .models import Suborder


class SuborderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Suborder
        fields = '__all__'
        read_only_fields = ['seller']


