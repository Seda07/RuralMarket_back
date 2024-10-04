import pytest
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from .models import Product, Category

User = get_user_model()


@pytest.mark.django_db
def test_create_product_as_seller():
    """
    Feature: Crear productos como vendedor

    Scenario: Un vendedor autenticado crea un nuevo producto en el sistema
        Given que existe una categoría llamada "Electrónica"
        And que existe un usuario con el tipo de usuario "vendedor"
        And el vendedor está autenticado
        When el vendedor envía una solicitud para crear un producto con los datos proporcionados
        Then el producto es creado exitosamente
        And el sistema retorna los detalles del producto creado, incluyendo el nombre, categoría, descripción, precio, stock, y vendedor
    """

    # Given que existe una categoría llamada "Electrónica"
    category = Category.objects.create(name='Electrónica')

    # Given que existe un usuario con el tipo de usuario "vendedor"
    seller = User.objects.create_user(
        username='vendedor',
        password='contraseña123',
        user_type='seller',  # Suponiendo que el modelo de usuario tiene un campo "user_type"
        first_name='Vendedor',
        last_name='Prueba'
    )

    # And el vendedor está autenticado
    client = APIClient()
    client.force_authenticate(user=seller)

    # When el vendedor envía una solicitud para crear un producto con los datos proporcionados
    product_data = {
        "name": "Teléfono Móvil",
        "category": category.id,
        "description": "Teléfono móvil de última generación",
        "price": "699.99",
        "stock": 5,
        "seller": seller.id  # Asegúrate de incluir el vendedor aquí
    }

    response = client.post('/api/product/', product_data, format='json')

    # Then el producto es creado exitosamente
    assert response.status_code == status.HTTP_201_CREATED, f"Error en la creación del producto: {response.content}"

    # And el sistema retorna los detalles del producto creado, incluyendo el nombre, categoría, descripción, precio, stock, y vendedor
    assert response.data['name'] == product_data['name']
    assert response.data['category'] == product_data['category']
    assert response.data['description'] == product_data['description']
    assert response.data['price'] == product_data['price']
    assert response.data['stock'] == product_data['stock']
    assert response.data['seller'] == seller.id  # Verificar que el vendedor esté asignado
