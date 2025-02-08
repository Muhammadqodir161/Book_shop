from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """
    Foydalanuvchi ma'lumotlarini qaytarish uchun serializer.
    """
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'is_verified']

class RegisterSerializer(serializers.ModelSerializer):
    """
    Ro'yxatdan o'tish uchun serializer.
    """
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def create(self, validated_data):
        """
        Yangi foydalanuvchini yaratish.
        """
        return User.objects.create_user(**validated_data)

class LoginSerializer(TokenObtainPairSerializer):
    """
    JWT token olish uchun serializer.
    """
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        return token

class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

class PasswordResetSerializer(serializers.Serializer):
    token = serializers.CharField()
    new_password = serializers.CharField(write_only=True, min_length=6)
