from rest_framework import serializers
from rest_framework_bulk import (
    BulkListSerializer,
    BulkSerializerMixin,
)
from .models import Brand, Warehouse, CarModel, Record


class BrandSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'name', 'country',)
        list_serializer_class = BulkListSerializer


class WarehouseSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ('id', 'name',)
        list_serializer_class = BulkListSerializer


class CarModelSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'name', 'brand', 'price',)
        list_serializer_class = BulkListSerializer


class RecordSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ('id', 'warehouse', 'carmodel', 'quantity',)
        list_serializer_class = BulkListSerializer
