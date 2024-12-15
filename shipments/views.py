from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Order, OrderItem
from .serializers import OrderSerializer
from access.models import User

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]  # Solo usuarios autenticados pueden acceder

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            # Si es superusuario, devuelve todas las órdenes con los usuarios
            User.objects.all()
            return Order.objects.select_related('user').all()
        else:
            # Si es usuario normal, devuelve solo las órdenes del usuario autenticado
            return Order.objects.filter(user=user)

    @action(detail=False, methods=['get'])
    def user_orders(self, request):
        user = self.request.user
        if user.is_authenticated:
            orders = Order.objects.filter(user=user)
            serializer = self.get_serializer(orders, many=True)
            return Response(serializer.data)
        return Response({'detail': 'No autorizado'}, status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=False, methods=['get'])
    def all_orders(self, request):
        user = self.request.user
        if user.is_superuser:
            orders = Order.objects.all()
            serializer = self.get_serializer(orders, many=True)
            return Response(serializer.data)
        return Response({'detail': 'No autorizado'}, status=status.HTTP_401_UNAUTHORIZED)
