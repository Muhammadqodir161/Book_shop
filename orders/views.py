from rest_framework import generics, permissions, viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Order
from .serializers import OrderSerializer
from notifications.models import Notification

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

class OrderListCreateView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        order = serializer.save(user=self.request.user)
        Notification.objects.create(
            user=self.request.user,
            message=f"Buyurtma #{order.id} muvaffaqiyatli yaratildi."
        )

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['user__email', 'status'] 
