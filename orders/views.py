from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializer import OrderSerializer
from .models import Order


class OrderView(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


