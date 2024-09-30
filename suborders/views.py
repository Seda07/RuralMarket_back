from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializer import SuborderSerializer
from .models import Suborder


class SuborderView(viewsets.ModelViewSet):
    serializer_class = SuborderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Suborder.objects.filter(seller=self.request.user)

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)
