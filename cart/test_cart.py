import pytest
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from .models import CustomUser, Cart

@pytest.mark.django_db
def test_create_cart():
    client = APIClient()
    user = CustomUser.objects.create_user(username='testuser', password='testpassword')
    client.force_authenticate(user=user)

    response = client.post(reverse('cart-list-create'), {})
    assert response.status_code == status.HTTP_201_CREATED
    assert 'id' in response.data  # Asegúrate de que se devuelve un ID
