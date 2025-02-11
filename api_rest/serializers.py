from rest_framework import serializers

from .models import User
# classe para serializar todos os campos
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'