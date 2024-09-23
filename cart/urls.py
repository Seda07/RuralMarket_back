from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CartView, CartItemView

router = DefaultRouter()
router.register(r'', CartView, basename='cart')
router.register(r'', CartItemView, basename='cartitem')

urlpatterns = [
    path('', include(router.urls)),
]