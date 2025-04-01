from django.urls import path

from .views import get_users, login_user, register_user

urlpatterns = [
    path("register/", register_user, name="register_user"),  # Cadastro geração de token
    path("login/", login_user, name="login_user"),  # Autenticação
    path(
        "users/", get_users, name="get_all_users"
    ),  # Lista de usuários (Protegido por Token)
]
