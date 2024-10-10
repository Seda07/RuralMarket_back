from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializer import SuborderSerializer
from .models import Suborder


class SuborderView(viewsets.ModelViewSet):
    serializer_class = SuborderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Suborder.objects.filter(seller=self.request.user)

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        suborders_with_product_quantities = []
        for suborder, suborder_data in zip(queryset, serializer.data):
            suborder_info = {
                'id': suborder_data['id'],
                'order': suborder_data['order'],
                'subtotal': suborder_data['subtotal'],
                'seller': suborder_data['seller'],
                'status': suborder_data['status'],
                'order_username': suborder_data['order_username'],
                'order_email': suborder_data['order_email'],
                'products': []
            }

            for item in suborder.suborder_product.all():
                product_info = {
                    'product_id': item.product.id,
                    'product_name': item.product.name,
                    'quantity': item.quantity,
                }
                suborder_info['products'].append(product_info)

            suborders_with_product_quantities.append(suborder_info)

        return Response(suborders_with_product_quantities)
