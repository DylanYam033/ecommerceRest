from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    # metodos custom para encriptar contraseña cuando se crea y se edita un usuario
    def create(self, validate_data):
        user = User(**validate_data)
        user.set_password(validate_data['password'])
        user.save()
        return user
    
    def update(self, instance, validated_data):
        updated_user = super().update(instance, validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
    
    # metodo to_representation para indicar como se mostrara la data del modelo o serializer
    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'name': instance['name'],
            'last_name': instance['last_name'],
            'username': instance['username'],
            'email': instance['email'],
            'password': instance['password']
        }
         