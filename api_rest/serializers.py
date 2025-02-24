from rest_framework import serializers
from django.contrib.auth.models import User 

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'username', 
            'first_name',  
            'email',  
            'password', 
        ]
        extra_kwargs = {
            'password': {'write_only': True},  
        }

    def create(self, validated_data):
        # Cria o usuário corretamente, garantindo que a senha seja hasheada
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            password=validated_data['password']  # O Django automaticamente faz o hash
        )
        return user

    def update(self, instance, validated_data):
        # Atualiza os dados do usuário garantindo que a senha seja hasheada corretamente
        password = validated_data.pop('password', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)  # O Django cuida do hash da senha

        instance.save()
        return instance
