from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SuborderProductView

router = DefaultRouter()
router.register(r'', SuborderProductView, basename='suborderProduct')


urlpatterns = [
    path('', include(router.urls)),
    ]