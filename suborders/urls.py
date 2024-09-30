from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SuborderView

router = DefaultRouter()
router.register(r'', SuborderView, basename='suborder')


urlpatterns = [
    path('', include(router.urls)),
    ]