from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError("Credenciales incorrectas")

        # Generar el token JWT
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        return {
            'access_token': access_token,
            'is_superuser': user.is_superuser 
        }



from django.contrib.auth import get_user_model
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password', 'password2']

    def validate(self, data):
        # Validación de contraseñas
        password = data.get('password')
        password2 = data.get('password2')

        if password != password2:
            raise serializers.ValidationError("Las contraseñas no coinciden")

        return data

    def create(self, validated_data):
        # Elimina el campo 'password2' antes de crear el usuario
        validated_data.pop('password2', None)
        
        # Crear usuario con 'is_admin' en False
        user = get_user_model().objects.create_user(**validated_data)
        return user

