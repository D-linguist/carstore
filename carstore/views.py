from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView
from rest_framework import generics
from rest_framework_bulk import ListBulkCreateUpdateDestroyAPIView

from orders.models import Order, Employee, Firm
from orders.views import _get_user
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


class BrandListAPIView(ListBulkCreateUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class CarModelListAPIView(ListBulkCreateUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer


class CarModelDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer


class RecordListAPIView(ListBulkCreateUpdateDestroyAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


class RecordDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


class WarehouseListAPIView(ListBulkCreateUpdateDestroyAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


class WarehouseDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


def car_model_detail(request, car_model_id):
    try:
        employee = Employee.objects.get(user__username=_get_user(request))
        single_car_model = CarModel.objects.get(id=car_model_id)
        orders = Order.objects.filter(employee=employee)
        orders_count = orders.count()
        firms = Firm.objects.all()
        records = Record.objects.filter(carmodel_id=car_model_id)
        records_quantity = 0
        for r in records:
            field_name = 'quantity'
            quantity = getattr(r, field_name)
            records_quantity += quantity
    except Employee.DoesNotExist:
        return render(request, 'orders/not_employee.html')
    context = {
        'single_car_model': single_car_model,
        'orders': orders,
        'orders_count': orders_count,
        'firms': firms,
        'quantity': records_quantity,
    }
    return render(request, 'carstore/car_model_detail.html', context)
