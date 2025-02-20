from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

import json

@api_view(['GET'])
def get_users(request):
		if request.method == 'GET':
				users = User.objects.all()
				serializer = UserSerializer(users, many=True)
				return Response(serializer.data)
		return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
def get_by_nick(request, nick):
		try:
				user = User.objects.get(pk=nick)
		except User.DoesNotExist:
				return Response(status=status.HTTP_404_NOT_FOUND)
		
		if request.method =='GET':
				serializer = UserSerializer(user)
				return Response(serializer.data)
  
		if request.method =='PUT':
				serializer = UserSerializer(user,data=request.data)
				
				if serializer.is_valid():
					serializer.save()
					return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
   
				return Response(status=status.HTTP_400_BAD_REQUEST)
  
# CRUD
@api_view(['GET','POST','PUT','DELETE'])
def user_manager(request):
		if request.method == 'GET':
				try:
						if request.GET['user']:                         # verifica se existe um parametro chamado 'user' 
								user_nickname = request.GET['user']         # pega parametro
								try:
										user = User.objects.get(pk=user_nickname)   # pega o objeto no database
								except:
										return Response(status=status.HTTP_404_NOT_FOUND)
								serializer = UserSerializer(user)           # Serialize para um objeto json
								return Response(serializer.data)            # Return os dados serializados
						else:
								return Response(status=status.HTTP_400_BAD_REQUEST)
				except:
						return Response(status=status.HTTP_400_BAD_REQUEST)
# CRIAR DADOS
		if request.method == 'POST':
				new_user = request.data
				serializer = UserSerializer(data=new_user)
				if serializer.is_valid():
						serializer.save()
						return Response(serializer.data, status=status.HTTP_201_CREATED)
				return Response(status=status.HTTP_400_BAD_REQUEST)
  
# EDITAR DADOS
		if request.method == 'PUT':
				nickname = request.data['user_nickname']
				try:
						updated_user = User.objects.get(pk=nickname)
				except:
						return Response(status=status.HTTP_404_NOT_FOUND)
				serializer = UserSerializer(updated_user, data=request.data)
    
				if serializer.is_valid():
						serializer.save()
						return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
				return Response(status=status.HTTP_400_BAD_REQUEST)

# DELETAR DADOS 
		if request.method == 'DELETE':
				try:
						user_to_delete = User.objects.get(pk=request.data['user_nickname'])
						user_to_delete.delete()
						return Response(status=status.HTTP_202_ACCEPTED)
				except:
						return Response(status=status.HTTP_400_BAD_REQUEST)


