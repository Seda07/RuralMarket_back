from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from .serializer import CartSerializer, CartItemSerializer
from .models import Cart, CartItem
from products.models import Product
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class CartItemView(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        cart = Cart.objects.get(user=self.request.user)
        return CartItem.objects.filter(cart=cart)

    def create(self, request, *args, **kwargs):
        cart, created = Cart.objects.get_or_create(user=request.user)

        product_id = request.data.get('product_id')
        quantity = int(request.data.get('quantity', 1))

        product = get_object_or_404(Product, id=product_id)

        if quantity < 1:
            return Response({"error": "La cantidad debe ser al menos 1"}, status=status.HTTP_400_BAD_REQUEST)
        if quantity > product.stock:
            return Response({
                "error": f"Sólo hay {product.stock} unidades disponibles de {product.name}."
            }, status=status.HTTP_400_BAD_REQUEST)

        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product, defaults={'quantity': quantity})
        if not created:
            cart_item.quantity += quantity
            cart_item.save()

        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        cart_item = self.get_object()
        quantity = int(request.data.get('quantity'))

        if quantity < 1:
            return Response({"error": "La cantidad debe ser al menos 1"}, status=status.HTTP_400_BAD_REQUEST)
        if quantity > cart_item.product.stock:
            return Response({
                "error": f"Sólo hay {cart_item.product.stock} unidades disponibles de {cart_item.product.name}."
            }, status=status.HTTP_400_BAD_REQUEST)

        cart_item.quantity = quantity
        cart_item.save()

        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        cart_item = self.get_object()
        cart_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CartView(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return Cart.objects.filter(id=cart.id)

    def retrieve_cart_summary(self, request):
        cart = Cart.objects.get(user=request.user)

        total_quantity = sum(item.quantity for item in cart.cart_items.all())
        total_price = sum(item.quantity * item.product.price for item in cart.cart_items.all())

        return Response({
            "total_quantity": total_quantity,
            "total_price": total_price
        }, status=status.HTTP_200_OK)
