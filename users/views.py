from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from rest_framework.permissions import AllowAny
from .models import CustomUser
from .serializers import RegisterSerializer, UserSerializer, UserProfileSerializer, PasswordResetSerializer, PasswordResetConfirmSerializer
from rest_framework import status

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

class PasswordResetView(APIView):
    def post(self, request):
        serializer = PasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            try:
                user = User.objects.get(email=email)
                uid = urlsafe_base64_encode(str(user.pk).encode())
                token = default_token_generator.make_token(user)
                reset_url = f'http://example.com/reset-password-confirm/?uid={uid}&token={token}'
                send_mail(
                    'Password Reset',
                    f'Click the link to reset your password: {reset_url}',
                    'no-reply@example.com',
                    [email],
                )
                return Response({'message': 'Password reset email sent successfully.'}, status=200)
            except User.DoesNotExist:
                return Response({'error': 'User not found'}, status=404)
        return Response(serializer.errors, status=400)

class PasswordResetConfirmView(APIView):
    def post(self, request):
        serializer = PasswordResetConfirmSerializer(data=request.data)
        if serializer.is_valid():
            uid = serializer.validated_data.get('uid')
            token = serializer.validated_data.get('token')
            password = serializer.validated_data.get('password')
            try:
                uid = urlsafe_base64_decode(uid).decode()
                user = User.objects.get(pk=uid)
                if default_token_generator.check_token(user, token):
                    user.set_password(password)
                    user.save()
                    return Response({'message': 'Password successfully reset.'}, status=200)
                else:
                    return Response({'error': 'Invalid token.'}, status=400)
            except User.DoesNotExist:
                return Response({'error': 'Invalid user.'}, status=404)
        return Response(serializer.errors, status=400)

class UserProfileUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        serializer = UserProfileSerializer(request.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)