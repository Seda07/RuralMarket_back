import pytest
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from .models import Product, Category

User = get_user_model()

@pytest.mark.django_db
def test_create_product_as_seller():
    # Crear una categoría
    category = Category.objects.create(name='Electrónica')

    # Crear un usuario vendedor
    seller = User.objects.create_user(
        username='vendedor',
        password='contraseña123',
        user_type='seller',
        first_name='Vendedor',
        last_name='Prueba'
    )

    # Crear una instancia de APIClient y autenticar al vendedor
    client = APIClient()
    client.force_authenticate(user=seller)

    # Definir los datos del nuevo producto, incluyendo el campo 'seller'
    product_data = {
        "name": "Teléfono Móvil",
        "category": category.id,
        "description": "Teléfono móvil de última generación",
        "price": "699.99",
        "stock": 5,
        "seller": seller.id  # Asegúrate de incluir el vendedor aquí
    }

    # Enviar la solicitud POST para crear el producto
    response = client.post('/api/product/', product_data, format='json')

    # Verificar que el producto se ha creado correctamente
    assert response.status_code == status.HTTP_201_CREATED, f"Error en la creación del producto: {response.content}"
    assert response.data['name'] == product_data['name']
    assert response.data['category'] == product_data['category']
    assert response.data['description'] == product_data['description']
    assert response.data['price'] == product_data['price']
    assert response.data['stock'] == product_data['stock']
    assert response.data['seller'] == seller.id  # Verificar que el vendedor esté asignado

