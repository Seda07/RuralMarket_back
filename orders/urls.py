from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CreateOrderView, OrderSellerView

router = DefaultRouter()
router.register(r'order', CreateOrderView, basename='order')


urlpatterns = [
    path('', include(router.urls)),
    path('create/', CreateOrderView.as_view({'post': 'create'}), name='create-order'),
    path('seller/', OrderSellerView.as_view({'get': 'list'}), name='order-seller'),
]

