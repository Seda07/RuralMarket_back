import pytest
from decimal import Decimal
from rest_framework.exceptions import ValidationError  # Cambiamos a ValidationError de DRF
from users.models import CustomUser
from category.models import Category
from .models import Product


# Test para la creación de un producto válido
@pytest.mark.django_db
def test_given_seller_when_creates_valid_product_then_product_created_successfully():
    """
    Escenario: Crear un producto válido exitosamente

    Dado que existe un vendedor con el nombre de usuario "seller1"
    Y existe una categoría "Electrónica"
    Cuando el vendedor crea un producto con el nombre "Laptop", precio "1500.00" y stock "10"
    Entonces el producto debería crearse exitosamente
    """
    # Given (Dado)
    seller = CustomUser.objects.create(username="seller1", user_type="seller")
    category = Category.objects.create(name="Electrónica")

    # When (Cuando)
    product = Product.objects.create(
        name="Laptop",
        category=category,
        description="Una laptop de gaming de alta gama",
        price=Decimal('1500.00'),
        stock=10,
        seller=seller
    )

    # Then (Entonces)
    assert product.name == "Laptop"
    assert product.category == category
    assert product.price == Decimal('1500.00')
    assert product.stock == 10


# Test para stock negativo
@pytest.mark.django_db
def test_given_seller_when_creates_product_with_negative_stock_then_error_raised():
    """
    Escenario: Crear un producto con stock negativo

    Dado que existe un vendedor con el nombre de usuario "seller1"
    Y existe una categoría "Electrónica"
    Cuando el vendedor intenta crear un producto con el nombre "Laptop", precio "1500.00" y stock "-5"
    Entonces debería lanzarse un error que diga "El stock no puede ser negativo"
    """
    # Given (Dado)
    seller = CustomUser.objects.create(username="seller1", user_type="seller")
    category = Category.objects.create(name="Electrónica")

    # When (Cuando)
    product = Product(
        name="Laptop",
        category=category,
        description="Una laptop de gaming de alta gama",
        price=Decimal('1500.00'),
        stock=-5,
        seller=seller
    )

    # Then (Entonces)
    with pytest.raises(ValidationError, match="El stock no puede ser negativo"):
        product.clean()


# Test para validar que solo los vendedores pueden crear productos
@pytest.mark.django_db
def test_given_buyer_when_tries_to_create_product_then_error_raised():
    """
    Escenario: Crear un producto por un usuario que no es vendedor

    Dado que existe un comprador con el nombre de usuario "buyer1"
    Y existe una categoría "Electrónica"
    Cuando el comprador intenta crear un producto con el nombre "Laptop", precio "1500.00" y stock "10"
    Entonces debería lanzarse un error que diga "Solo los vendedores pueden agregar productos"
    """
    # Given (Dado)
    buyer = CustomUser.objects.create(username="buyer1", user_type="buyer")
    category = Category.objects.create(name="Electrónica")

    # When (Cuando)
    product = Product(
        name="Laptop",
        category=category,
        description="Una laptop de gaming de alta gama",
        price=Decimal('1500.00'),
        stock=10,
        seller=buyer
    )

    # Then (Entonces)
    with pytest.raises(ValidationError, match="Solo los vendedores pueden agregar productos"):
        product.clean()


# Test para validar que el precio debe ser mayor que cero
@pytest.mark.django_db
def test_given_seller_when_creates_product_with_zero_price_then_error_raised():
    """
    Escenario: Crear un producto con precio igual a cero o negativo

    Dado que existe un vendedor con el nombre de usuario "seller1"
    Y existe una categoría "Electrónica"
    Cuando el vendedor intenta crear un producto con el nombre "Laptop", precio "0.00" y stock "10"
    Entonces debería lanzarse un error que diga "El precio debe ser mayor a cero"
    """
    # Given (Dado)
    seller = CustomUser.objects.create(username="seller1", user_type="seller")
    category = Category.objects.create(name="Electrónica")

    # When (Cuando)
    product = Product(
        name="Laptop",
        category=category,
        description="Una laptop de gaming de alta gama",
        price=Decimal('0.00'),
        stock=10,
        seller=seller
    )

    # Then (Entonces)
    with pytest.raises(ValidationError, match="El precio debe ser mayor a cero"):
        product.clean()
