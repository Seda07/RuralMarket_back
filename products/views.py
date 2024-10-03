from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .serializer import ProductSerializer
from .models import Product


class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = self.request.user

        print(f"Tipo de usuario: {user.user_type}")
        print(f"Usuario que intenta crear el producto: {user.username}")

        if user.user_type != 'seller':
            print("Acceso denegado: solo los vendedores pueden agregar productos.")
            return Response({'detail': 'Solo los vendedores pueden agregar productos.'},
                            status=status.HTTP_403_FORBIDDEN)

        serializer.save(seller=user)
