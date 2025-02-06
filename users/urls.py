from django.urls import path
from .views import RegisterView, PasswordResetView, PasswordResetConfirmView, UserProfileUpdateView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('reset-password/', PasswordResetView.as_view(), name='reset-password'),
    path('reset-password-confirm/', PasswordResetConfirmView.as_view(), name='reset-password-confirm'),
    path('profile/', UserProfileUpdateView.as_view(), name='profile-update'),
]
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns += [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
