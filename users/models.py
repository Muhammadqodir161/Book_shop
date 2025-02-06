from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.crypto import get_random_string
from rest_framework_simplejwt.tokens import RefreshToken

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_email_verified = models.BooleanField(default=False)
    email_verification_token = models.CharField(max_length=64, blank=True, null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.email
    
    def get_tokens_for_user(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
    
    def generate_email_verification_token(self):
        self.email_verification_token = get_random_string(length=64)
        self.save()
        return self.email_verification_token

