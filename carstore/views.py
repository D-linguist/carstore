from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import ListView
from rest_framework import generics
from rest_framework_bulk import ListBulkCreateUpdateDestroyAPIView

from .models import Brand, Warehouse, CarModel, Record
from .serializers import BrandSerializer, CarModelSerializer, WarehouseSerializer, RecordSerializer


class BrandListView(LoginRequiredMixin, ListView):
    model = Brand
    context_object_name = 'brands'
    template_name = 'carstore/brand_list.html'
    login_url = 'account_login'


class WarehouseListView(LoginRequiredMixin, ListView):
    model = Warehouse
    context_object_name = 'warehouses'
    template_name = 'carstore/warehouse_list.html'
    login_url = 'account_login'


class CarModelListView(LoginRequiredMixin, ListView):
    model = CarModel
    context_object_name = 'car_models'
    template_name = 'carstore/car_model_list.html'
    login_url = 'account_login'


class RecordListView(LoginRequiredMixin, ListView):
    model = Record
    context_object_name = 'records'
    template_name = 'carstore/record_list.html'
    login_url = 'account_login'


class SearchBrandsListView(LoginRequiredMixin, ListView):
    model = Brand
    context_object_name = 'brands'
    template_name = 'carstore/brand_search_results.html'
    login_url = 'account_login'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Brand.objects.filter(
            Q(name__icontains=query) | Q(country__icontains=query)
        )


class SearchCarModelsListView(LoginRequiredMixin, ListView):
    model = CarModel
    context_object_name = 'car_models'
    template_name = 'carstore/car_model_search_results.html'
    login_url = 'account_login'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return CarModel.objects.filter(
            Q(name__icontains=query) | Q(brand__name__icontains=query)
        )


class SearchRecordsListView(LoginRequiredMixin, ListView):
    model = Warehouse
    context_object_name = 'records'
    template_name = 'carstore/record_search_results.html'
    login_url = 'account_login'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Record.objects.filter(
            Q(carmodel__name__icontains=query) | Q(warehouse__name__icontains=query)
        )


class BrandList(ListBulkCreateUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class CarModelList(ListBulkCreateUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer


class CarModelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer


class RecordList(ListBulkCreateUpdateDestroyAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


class RecordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


class WarehouseList(ListBulkCreateUpdateDestroyAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


class WarehouseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
