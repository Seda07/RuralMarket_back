from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializer import ProductSerializer
from .models import Product


class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]  # Asegúrate de que el usuario esté autenticado

    def perform_create(self, serializer):
        user = self.request.user

        # Impresión de depuración para ver el tipo de usuario
        print(f"Tipo de usuario: {user.user_type}")  # Verifica el tipo de usuario
        print(f"Usuario que intenta crear el producto: {user.username}")  # Muestra el nombre del usuario

        # Verificar que el usuario sea un vendedor
        if user.user_type != 'seller':
            print("Acceso denegado: solo los vendedores pueden agregar productos.")
            return Response({'detail': 'Solo los vendedores pueden agregar productos.'},
                            status=status.HTTP_403_FORBIDDEN)

        # Guardar el producto y asignar el vendedor
        serializer.save(seller=user)
