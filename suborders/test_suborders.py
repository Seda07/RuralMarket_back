import pytest
from decimal import Decimal
from users.models import CustomUser
from orders.models import Order
from cart.models import Cart
from suborders.models import Suborder

@pytest.mark.django_db
class TestSuborderCreation:
    """
    Feature: Creación de una suborden

      Scenario: Un vendedor recibe una suborden correctamente
        Given una orden existente y un usuario vendedor
        When se crea una suborden con un subtotal de 50.00
        Then la suborden debe ser creada con estado "pendiente"
        And la suborden debe estar asociada a la orden y al vendedor
    """
    def test_suborder_creation(self):
        # Given: Una orden existente y un usuario vendedor
        user = CustomUser.objects.create_user(username="juan", password="password123")
        seller = CustomUser.objects.create_user(username="vendedor", password="password123", user_type="seller")
        cart = Cart.objects.create(user=user)
        order = Order.objects.create(
            cart=cart,
            total=Decimal("100.00"),
            user=user
        )

        # When: Se crea una suborden con un subtotal de 50.00
        suborder = Suborder.objects.create(
            order=order,
            subtotal=Decimal("50.00"),
            seller=seller
        )

        # Then: La suborden debe ser creada con estado "pendiente"
        assert suborder.status == 'pending'

        # And: La suborden debe estar asociada a la orden y al vendedor
        assert suborder.order == order
        assert suborder.seller == seller
        assert suborder.subtotal == Decimal("50.00")

@pytest.mark.django_db
class TestSuborderStatusUpdate:
    """
    Feature: Actualización del estado de una suborden

      Scenario: Un vendedor actualiza el estado de una suborden
        Given una suborden existente con estado "pendiente"
        When el estado de la suborden cambia a "finalizada"
        Then el estado de la suborden debe ser "finalizada"
    """
    def test_suborder_status_update(self):
        # Given: Una suborden existente con estado "pendiente"
        user = CustomUser.objects.create_user(username="juan", password="password123")
        seller = CustomUser.objects.create_user(username="vendedor", password="password123", user_type="seller")
        cart = Cart.objects.create(user=user)
        order = Order.objects.create(
            cart=cart,
            total=Decimal("100.00"),
            user=user
        )
        suborder = Suborder.objects.create(
            order=order,
            subtotal=Decimal("50.00"),
            seller=seller
        )
        assert suborder.status == 'pending'
        # When: El estado de la suborden cambia a "finalizada"
        suborder.status = 'completed'
        suborder.save()

        # Then: El estado de la suborden debe ser "finalizada"
        suborder.refresh_from_db()
        assert suborder.status == 'completed'
