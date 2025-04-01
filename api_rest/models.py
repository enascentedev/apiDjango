from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, login, email, nome, password=None, **extra_fields):
        if not login:
            raise ValueError("O campo 'login' é obrigatório.")
        if not email:
            raise ValueError("O campo 'email' é obrigatório.")
        email = self.normalize_email(email)
        user = self.model(login=login, email=email, nome=nome, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, login, email, nome, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(login, email, nome, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    nome = models.CharField(max_length=150)
    login = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=20, default="ativo")
    perfil = models.CharField(max_length=20, default="admin")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "login"
    REQUIRED_FIELDS = ["email", "nome"]

    objects = CustomUserManager()

    def __str__(self):
        return self.login
