from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from orders.models import Order
from cart.models import CartItem
from suborders.models import Suborder
from suborders_product.models import SuborderProduct
from orders.serializer import OrderSerializer
from decimal import Decimal
from utils.mails import send_order_confirmation_email, send_seller_order_notification


class CreateOrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        missing_fields = []

        if not user.first_name:
            missing_fields.append("first_name")
        if not user.address:
            missing_fields.append("address")
        if not user.phone:
            missing_fields.append("phone")

        if missing_fields:
            raise ValidationError({
                "missing_fields": missing_fields,
                "message": "Por favor completa tu información antes de realizar la compra."
            })

        order = serializer.save(user=user)

        cart_items = CartItem.objects.filter(cart__user=user)
        if not cart_items.exists():
            raise ValidationError({"message": "No tienes productos en tu carrito."})

        suborders_data = {}
        products_detail = []

        for cart_item in cart_items:
            product = cart_item.product
            seller = product.seller
            quantity = cart_item.quantity

            if seller not in suborders_data:
                suborder = Suborder.objects.create(
                    order=order,
                    seller=seller,
                    subtotal=Decimal('0.00'),
                    status='pending'
                )
                suborders_data[seller] = suborder
            else:
                suborder = suborders_data[seller]

            SuborderProduct.objects.create(
                suborder=suborder,
                product=product,
                quantity=quantity,
                sold_price=product.price
            )

            suborder.subtotal += product.price * quantity
            suborder.save()

            products_detail.append({
                'product_name': product.name,
                'quantity': quantity,
                'price': product.price,
                'total_price': product.price * quantity,
            })

        cart_items.delete()

        send_order_confirmation_email(order, products_detail)

        for seller in suborders_data.keys():
            send_seller_order_notification(order, seller)


class OrderSellerView(viewsets.ReadOnlyModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


