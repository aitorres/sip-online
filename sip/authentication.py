# encoding=utf-8

"""
Módulo con funciones para complementar el manejo de sesiones
de Django.
"""

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class EmailBackend(ModelBackend):
    """
    Implementa un manejador de autenticación que permite iniciar
    sesión con correo electrónico en vez de nombre de usuario.
    """

    def authenticate(self, username=None, password=None, **kwargs):
        """
        Verifica si existe un usuario con el correo electrónico PASADO
        COMO 'username', en cuyo caso intenta iniciar sesión.
        """

        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None
