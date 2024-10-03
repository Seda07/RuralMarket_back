from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializer import ProductSerializer

class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]  # Permite lectura pública, escritura solo a usuarios autenticados

    def perform_create(self, serializer):
        user = self.request.user

        # Verificar si el usuario es vendedor y está autenticado
        if user.is_anonymous or user.user_type != 'seller':
            return Response({'detail': 'Solo los vendedores pueden agregar productos.'},
                            status=status.HTTP_403_FORBIDDEN)

        # Obtener los datos del producto del serializer
        name = serializer.validated_data.get('name')
        category = serializer.validated_data.get('category')
        stock = serializer.validated_data.get('stock')

        # Verificar si el producto ya existe para el mismo vendedor y categoría
        product_exists = Product.objects.filter(name=name, category=category, seller=user).exists()
        if product_exists:
            return Response({'detail': f"El producto '{name}' ya está registrado por este vendedor."},
                            status=status.HTTP_400_BAD_REQUEST)

        # Verificar que el stock sea mayor a 0
        if stock <= 0:
            return Response({'detail': 'El stock debe ser mayor a 0 para crear el producto.'},
                            status=status.HTTP_400_BAD_REQUEST)

        # Si pasa todas las validaciones, se guarda el producto asignando el vendedor
        serializer.save(seller=user)

    # Opcionalmente puedes personalizar el método de actualización si quieres aplicar las mismas validaciones
    def perform_update(self, serializer):
        user = self.request.user

        # Verificar si el usuario es vendedor y está autenticado
        if user.is_anonymous or user.user_type != 'seller':
            return Response({'detail': 'Solo los vendedores pueden actualizar productos.'},
                            status=status.HTTP_403_FORBIDDEN)

        # Obtener los datos del producto del serializer
        stock = serializer.validated_data.get('stock')

        # Verificar que el stock sea mayor a 0
        if stock <= 0:
            return Response({'detail': 'El stock debe ser mayor a 0 para actualizar el producto.'},
                            status=status.HTTP_400_BAD_REQUEST)

        # Si pasa todas las validaciones, actualiza el producto
        serializer.save()
