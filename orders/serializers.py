from rest_framework import serializers
from rest_framework_bulk import (
    BulkListSerializer,
    BulkSerializerMixin,
)

from orders.models import Order, Firm, OrderDetail


class FirmSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Firm
        fields = ('id', 'name',)
        list_serializer_class = BulkListSerializer


class OrderSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'employee', 'firm', 'total_price', 'created_at', 'updated_at',)
        list_serializer_class = BulkListSerializer


class OrderDetailSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = ('id', 'order', 'car_model', 'quantity', 'price', 'is_active',)
        list_serializer_class = BulkListSerializer
