from rest_framework import serializers
from .models import Order, OrderItem
from access.models import User

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'name', 'description', 'quantity', 'price', 'weight']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'order_date', 'delivery_date', 'items', 'user']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if self.context['request'].user.is_superuser:
            representation['user'] = instance.user.username  # Agregar nombre de usuario para superusuario
        return representation
