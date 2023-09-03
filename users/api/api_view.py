from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework.decorators import api_view
from rest_framework import status
from users.models import User
from users.api.serializers import UserSerializer, UserListSerializer
from django.shortcuts import get_object_or_404

# class UserAPIView(APIView):
#     def get(self, request):
#         users = User.objects.all()
#         users_serializers = UserSerializer(users, many=True)
#         return Response(users_serializers.data)
    
@api_view(['GET'])
def userList_api_view(request):
    if request.method == 'GET':
        users = User.objects.all().values('id','name','username','email','password') #se deben obtener los valores si el serializador, tiene el metodo to_representation()
        users_serializers = UserListSerializer(users, many=True)
        return Response(users_serializers.data)
    
@api_view(['POST'])
def userCreate_api_view(request):
    if request.method == 'POST':
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(user_serializer.errors)
        
@api_view(['GET','PUT','DELETE'])
def getUser_api_view(request, id):

    user = get_object_or_404(User, id=id)

    if user:
        if request.method == 'GET':
            userDetail_serializer = UserSerializer(user)
            return Response(userDetail_serializer.data)

        elif request.method == 'PUT':
            editUser_serializer = UserSerializer(user, data=request.data)
            if editUser_serializer.is_valid():
                editUser_serializer.save()
                return Response(editUser_serializer.data)
            else: 
                return Response(editUser_serializer.errors)
        
        elif request.method == 'DELETE':
            user.delete()
            return Response('Eliminado')
        
    else:
        return Response({'message':'No se ha encontrado el usuario'}, status=status.HTTP_400_BAD_REQUEST)
        
