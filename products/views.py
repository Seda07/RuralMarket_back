from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializer import ProductSerializer

class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user

        if user.user_type != 'seller':
            return Response({'detail': 'Solo los vendedores pueden agregar productos.'},
                            status=status.HTTP_403_FORBIDDEN)

        name = serializer.validated_data.get('name')
        category = serializer.validated_data.get('category')
        stock = serializer.validated_data.get('stock')


        product_exists = Product.objects.filter(name=name, category=category, seller=user).exists()
        if product_exists:
            return Response({'detail': f"El producto '{name}' ya está registrado por este vendedor."},
                            status=status.HTTP_400_BAD_REQUEST)


        if stock <= 0:
            return Response({'detail': 'El stock debe ser mayor a 0 para crear el producto.'},
                            status=status.HTTP_400_BAD_REQUEST)


        serializer.save(seller=user)

