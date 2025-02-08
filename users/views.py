from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import (
    UserSerializer, RegisterSerializer, LoginSerializer, 
    PasswordResetRequestSerializer, PasswordResetSerializer
)

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    """
    Ro‘yxatdan o‘tish uchun API.
    """
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class LoginView(TokenObtainPairView):
    """
    JWT login uchun API.
    """
    serializer_class = LoginSerializer

class UserProfileView(generics.RetrieveUpdateAPIView):
    """
    Foydalanuvchi profilini ko‘rish va yangilash uchun API.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

class PasswordResetRequestView(APIView):
    """
    Parolni tiklash uchun email orqali so‘rov jo‘natish.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'message': 'Reset link sent to email'}, status=status.HTTP_200_OK)

class PasswordResetView(APIView):
    """
    Parolni qayta tiklash uchun API.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = PasswordResetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'message': 'Password successfully reset'}, status=status.HTTP_200_OK)
