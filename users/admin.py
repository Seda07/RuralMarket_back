from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Registrar el modelo CustomUser con la configuración de UserAdmin
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Si quieres personalizar los campos visibles en la vista de admin:
    search_fields = ('username', 'email')

