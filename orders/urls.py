from django.urls import path, include
from .views import OrderListCreateView, OrderDetailView, OrderViewSet

urlpatterns = [
    path('', OrderListCreateView.as_view(), name='order-list'),
    path('<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
]
router = DefaultRouter()
router.register(r'orders', OrderViewSet)


urlpatterns = [
    path('', include(router.urls)),
]