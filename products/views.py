from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import ValidationError
from .models import Product
from .serializer import ProductSerializer
from rest_framework.exceptions import PermissionDenied


class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        user = self.request.user

        if user.is_anonymous or user.user_type != 'seller':
            raise ValidationError({'detail': 'Solo los vendedores pueden agregar productos.'})

        name = serializer.validated_data.get('name').strip()
        category = serializer.validated_data.get('category')
        stock = serializer.validated_data.get('stock')

        if Product.objects.filter(name__iexact=name, category=category, seller=user).exists():
            raise ValidationError({'detail': f"El producto '{name}' ya está registrado por este vendedor."})

        if stock <= 0:
            raise ValidationError({'detail': 'El stock debe ser mayor a 0 para crear el producto.'})

        serializer.save(seller=user)

    def perform_update(self, serializer):
        user = self.request.user

        if user.is_anonymous or user.user_type != 'seller':
            raise ValidationError({'detail': 'Solo los vendedores pueden actualizar productos.'})

        product = self.get_object()

        name = serializer.validated_data.get('name', product.name).strip()
        category = serializer.validated_data.get('category', product.category)

        if Product.objects.filter(name__iexact=name, category=category).exclude(id=product.id).exists():
            raise ValidationError({'detail': f"El producto '{name}' ya está registrado por otro vendedor."})

        stock = serializer.validated_data.get('stock', product.stock)

        if stock < 0:
            raise ValidationError({'detail': 'El stock debe ser mayor o igual a 0 para actualizar el producto.'})

        serializer.save()

    def perform_destroy(self, instance):
        user = self.request.user

        if user.is_anonymous or user.user_type != 'seller':
            raise PermissionDenied({'detail': 'Solo los vendedores pueden eliminar productos.'})

        if instance.seller != user:
            raise PermissionDenied({'detail': 'No tienes permiso para eliminar este producto.'})

        instance.delete()

