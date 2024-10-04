import pytest
from django.contrib.auth import get_user_model
from django.db import IntegrityError

# Importamos el modelo CustomUser
CustomUser = get_user_model()

@pytest.mark.django_db
class TestCustomUser:
    """
    Feature: Registro de usuario

      Scenario: Un nuevo usuario se registra correctamente
        Given un usuario no registrado
        When el usuario se registra con nombre "Juan", email "juan@example.com", y tipo de usuario "buyer"
        Then el usuario debe ser creado en el sistema con el tipo "buyer"
        And el usuario debe tener un número de teléfono, dirección y descripción vacíos
    """
    def test_user_creation(self):
        # Given: Un usuario no registrado
        # When: Se registra el usuario
        user = CustomUser.objects.create_user(
            username='juan',
            email='juan@example.com',
            password='password123',
            user_type='buyer'
        )

        # Then: El usuario debe estar creado correctamente
        assert user.username == 'juan'
        assert user.email == 'juan@example.com'
        assert user.user_type == 'buyer'
        assert user.phone is None
        assert user.address is None
        assert user.user_description is None

    """
    Feature: Actualización del perfil de usuario

      Scenario: Un usuario actualiza su perfil con nueva información
        Given un usuario registrado con nombre "Juan"
        When el usuario actualiza su teléfono a "123456789", su dirección a "Calle Falsa 123", y su descripción a "Soy un vendedor"
        Then los datos del perfil del usuario deben actualizarse correctamente en el sistema
    """
    def test_update_user_profile(self):
        # Given: Un usuario registrado
        user = CustomUser.objects.create_user(
            username='juan',
            email='juan@example.com',
            password='password123',
            user_type='seller'
        )

        # When: El usuario actualiza su perfil
        user.phone = '123456789'
        user.address = 'Calle Falsa 123'
        user.user_description = 'Soy un vendedor'
        user.save()

        # Then: Los datos deben actualizarse correctamente
        assert user.phone == '123456789'
        assert user.address == 'Calle Falsa 123'
        assert user.user_description == 'Soy un vendedor'

    """
    Feature: Eliminación de usuario

      Scenario: Un usuario elimina su cuenta
        Given un usuario registrado con nombre "Juan"
        When el usuario solicita eliminar su cuenta
        Then el usuario debe ser eliminado del sistema
    """
    def test_user_deletion(self):
        # Given: Un usuario registrado
        user = CustomUser.objects.create_user(
            username='juan',
            email='juan@example.com',
            password='password123'
        )

        # When: Se elimina el usuario
        user_id = user.id
        user.delete()

        # Then: El usuario debe eliminarse correctamente
        with pytest.raises(CustomUser.DoesNotExist):
            CustomUser.objects.get(id=user_id)



