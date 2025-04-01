from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import CustomUser
from .serializers import UserSerializer


@api_view(["POST"])
def register_user(request):
    required_fields = [
        "login",
        "nome",
        "email",
        "password",
        "telefone",
        "status",
        "perfil",
    ]
    data = {field: request.data.get(field, "").strip() for field in required_fields}

    if not all(data.values()):
        return Response(
            {"error": "Todos os campos são obrigatórios."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {"login": user.login, "token": token.key},
            status=status.HTTP_201_CREATED,
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def login_user(request):
    email = request.data.get("email")
    password = request.data.get("password")

    if not email or not password:
        return Response(
            {"error": "email e senha são obrigatórios."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        user = CustomUser.objects.get(email=email)
    except CustomUser.DoesNotExist:
        return Response(
            {"error": "Usuário não encontrado."}, status=status.HTTP_404_NOT_FOUND
        )

    if not user.check_password(password):
        return Response(
            {"error": "Credenciais inválidas."}, status=status.HTTP_401_UNAUTHORIZED
        )

    token, created = Token.objects.get_or_create(user=user)
    return Response({"token": token.key}, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_users(request):
    users = CustomUser.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
