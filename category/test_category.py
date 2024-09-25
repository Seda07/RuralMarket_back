import pytest
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from .models import Category


# Test para la creación de una categoría válida
@pytest.mark.django_db
def test_given_category_when_creates_valid_category_then_category_created_successfully():
    """
    Escenario: Crear una categoría válida exitosamente

    Dado que no existe una categoría con el nombre "Electrónica"
    Cuando se crea una categoría con el nombre "Electrónica" y descripción "Categoría de productos electrónicos"
    Entonces la categoría debería crearse exitosamente
    """
    # Given (Dado)
    category_name = "Electrónica"
    description = "Categoría de productos electrónicos"

    # When (Cuando)
    category = Category.objects.create(name=category_name, description=description)

    # Then (Entonces)
    assert category.name == category_name
    assert category.description == description


# Test para la creación de una categoría sin nombre
@pytest.mark.django_db
def test_given_no_name_when_creates_category_then_error_raised():
    """
    Escenario: Crear una categoría sin nombre

    Dado que no existe una categoría con el nombre ""
    Cuando se intenta crear una categoría con el nombre "" y descripción "Descripción de prueba"
    Entonces debería lanzarse un error de validación de Django
    """
    # Given (Dado)
    description = "Descripción de prueba"

    # When (Cuando)
    category = Category(name="", description=description)

    # Then (Entonces)
    with pytest.raises(ValidationError):
        category.full_clean()  # Utilizamos full_clean() para validar el objeto antes de guardar


