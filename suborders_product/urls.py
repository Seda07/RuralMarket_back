from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SuborderProduct

router = DefaultRouter()
router.register(r'', SuborderProduct, basename='suborderProduct')


urlpatterns = [
    path('', include(router.urls)),
    ]