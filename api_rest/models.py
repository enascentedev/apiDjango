from django.db import models
from django.contrib.auth.hashers import make_password

class User(models.Model):  # DELETE ESTE MODELO
    user_nickname = models.CharField(primary_key=True, max_length=100, default='')
    user_name = models.CharField(max_length=150, default='')
    user_email = models.EmailField(default='')
    user_age = models.IntegerField(default=0)
    user_password = models.CharField(max_length=128, default='')  # NOVO CAMPO

    def __str__(self):
        return f'Nickname: {self.user_nickname} | E-mail: {self.user_email}'

    # Método para hash da senha
    def set_password(self, raw_password):
        self.user_password = make_password(raw_password)
