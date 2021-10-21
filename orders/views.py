from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from rest_framework import generics
from rest_framework_bulk import ListBulkCreateUpdateDestroyAPIView

from carstore.models import CarModel
from .models import Order, OrderDetail, Employee, Firm
from .serializers import OrderSerializer, FirmSerializer, OrderDetailSerializer


def _get_user(request):
    user = User.objects.get(username=request.user.username)
    return user


@login_required
def order_list(request):
    user = _get_user(request)
    try:
        employee = Employee.objects.get(user__username=user)
        orders = Order.objects.filter(employee=employee)
    except Employee.DoesNotExist:
        if user.is_superuser:
            orders = Order.objects.all()
        else:
            orders = []
    context = {
        'orders': orders,
    }
    return render(request, 'orders/order_list.html', context)


@login_required
def order_detail_list(request, order):
    order_details = OrderDetail.objects.filter(order=order)
    context = {
        'order_details': order_details,
        'order': order,
    }
    return render(request, 'orders/order_detail.html', context)


@login_required
def add_order(request, car_model_id):
    employee = Employee.objects.get(user__username=_get_user(request))
    car_model = CarModel.objects.get(id=car_model_id)
    print(employee, car_model)
    try:
        order_id = request.POST.get('order_id')
        print(order_id)
        order = Order.objects.get(id=order_id)
        print(order)
    except Order.DoesNotExist:
        firm_name = request.POST.get('firm_name')
        print(firm_name)
        firm = Firm.objects.get(id=firm_name)
        order = Order.objects.create(employee=employee, firm=firm)
    quantity = request.POST.get('quantity')
    OrderDetail.objects.create(order=order, car_model=car_model, quantity=quantity)
    return redirect('orders')


class FirmListAPIView(ListBulkCreateUpdateDestroyAPIView):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer


class OrderListAPIView(ListBulkCreateUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailListAPIView(ListBulkCreateUpdateDestroyAPIView):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer


class OrderDetailDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer
