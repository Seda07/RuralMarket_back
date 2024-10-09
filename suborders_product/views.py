from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializer import SuborderProductSerializer
from .models import SuborderProduct


class SuborderProductView(viewsets.ModelViewSet):
    serializer_class = SuborderProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return SuborderProduct.objects.filter(suborder__seller=self.request.user)
