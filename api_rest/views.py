from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import check_password

from django.contrib.auth.models import User

from .serializers import UserSerializer

# 📌 Endpoint de Registro de Usuário
@api_view(['POST'])
def register_user(request):
    # Pegando apenas os campos necessários
    required_fields = ['username', 'email', 'first_name', 'password']
    data = {field: request.data.get(field, '').strip() for field in required_fields}

    # Verificar se todos os campos foram preenchidos
    if not all(data.values()):
        return Response({"error": "Todos os campos são obrigatórios."}, status=status.HTTP_400_BAD_REQUEST)

    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        user = serializer.save()

        # Criar um Token para o usuário recém-criado
        token, created = Token.objects.get_or_create(user=user)

        return Response({'username': user.username, 'token': token.key}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
# 📌 Endpoint de Login do Usuário
@api_view(['POST'])
def login_user(request):
    email = request.data.get('email')  
    password = request.data.get('password')  

    if not email or not password:
        return Response({'error': 'Email e senha são obrigatórios.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(email=email)  # Busca pelo email em vez do username
    except User.DoesNotExist:
        return Response({'error': 'Usuário não encontrado.'}, status=status.HTTP_404_NOT_FOUND)
      
    # Verifica a senha corretamente
    if not check_password(password, user.password):
        return Response({'error': 'Credenciais inválidas.'}, status=status.HTTP_401_UNAUTHORIZED)

    # Pega ou cria um token para o usuário
    token, created = Token.objects.get_or_create(user=user)

    return Response({'token': token.key}, status=status.HTTP_200_OK)

# 📌 Endpoint protegido que lista os usuários (somente autenticados)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
