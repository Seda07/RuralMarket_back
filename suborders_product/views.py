from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializer import SuborderProductSerializer
from .models import SuborderProduct


class SuborderProduct(viewsets.ModelViewSet):
    serializer_class = SuborderProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return SuborderProduct.objects.filter(user=self.request.user)
