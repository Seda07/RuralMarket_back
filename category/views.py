from rest_framework import viewsets, serializers
from .serializer import CategorySerializer
from .models import Category


class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def perform_create(self, serializer):
        name = serializer.validated_data.get('name').strip()

        if Category.objects.filter(name__iexact=name).exists():
            raise serializers.ValidationError({"name": "Este nombre de categoría ya existe."})

        serializer.save()

    def perform_update(self, serializer):
        name = serializer.validated_data.get('name').strip()
        if Category.objects.filter(name__iexact=name).exists():
            raise serializers.ValidationError({"name": "Este nombre de categoría ya existe."})
        serializer.save()

