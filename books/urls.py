from django.urls import path
from .views import BookListCreateView, BookDetailView

urlpatterns = [
    path('', BookListCreateView.as_view(), name='book-list'),
    path('<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books', BookListCreateView)

urlpatterns = [
    path('', include(router.urls)),
]