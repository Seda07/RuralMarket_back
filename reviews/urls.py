from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReviewProduct


router = DefaultRouter()
router.register(r'', ReviewProduct, basename='review')

urlpatterns = [
    path('', include(router.urls)),
]