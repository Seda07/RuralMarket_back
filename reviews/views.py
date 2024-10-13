from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializer import ReviewSerializer
from .models import Review


class ReviewProduct(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)