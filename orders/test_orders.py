import pytest
from decimal import Decimal
from users.models import CustomUser
from cart.models import Cart
from orders.models import Order


@pytest.mark.django_db
class TestOrderCreation:
    """
    Feature: Creación de una orden

      Scenario: Un usuario crea una orden correctamente
        Given un usuario registrado y un carrito con productos
        When el usuario crea una orden con un total de 100.00
        Then la orden debe ser creada con estado "pendiente"
        And la orden debe estar asociada al usuario y al carrito
    """

    def test_order_creation(self):
        # Given: Un usuario registrado y un carrito
        user = CustomUser.objects.create_user(username="juan", password="password123")
        cart = Cart.objects.create(user=user)

        # When: Se crea una orden con un total de 100.00
        order = Order.objects.create(
            cart=cart,
            total=Decimal("100.00"),
            user=user
        )

        # Then: La orden debe ser creada con estado "pendiente"
        assert order.status == 'pending'

        # And: La orden debe estar asociada al usuario y al carrito
        assert order.user == user
        assert order.cart == cart
        assert order.total == Decimal("100.00")
@pytest.mark.django_db
class TestOrderStatusUpdate:
    """
    Feature: Actualización del estado de una orden

      Scenario: Un usuario actualiza el estado de una orden
        Given una orden existente con estado "pendiente"
        When el estado de la orden cambia a "finalizada"
        Then el estado de la orden debe ser "finalizada"
    """
    def test_order_status_update(self):
        # Given: Una orden existente con estado "pendiente"
        user = CustomUser.objects.create_user(username="juan", password="password123")
        cart = Cart.objects.create(user=user)
        order = Order.objects.create(
            cart=cart,
            total=Decimal("100.00"),
            user=user
        )
        assert order.status == 'pending'

        # When: El estado de la orden cambia a "finalizada"
        order.status = 'completed'
        order.save()

        # Then: El estado de la orden debe ser "finalizada"
        order.refresh_from_db()
        assert order.status == 'completed'
