from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializer import CartSerializer, CartItemSerializer
from .models import Cart, CartItem


class CartItemView(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()


class CartView(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(comprador=self.request.user)






