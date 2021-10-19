from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView

from carstore.models import CarModel
from .models import Order, OrderDetail, Employee, Firm

"""
def add_order(request, car_model_id):
    car_model = CarModel.objects.get(id=car_model_id)
    try:
        order = Order.objects.get(id)
    except Order.DoesNotExist:
        order = Order.objects.create(
            id=_order_id(request)
        )
    order.save()
    order_detail_exists = OrderDetail.objects.filter(car_model=car_model, order=order).exists()
    if order_detail_exists:
        detail = OrderDetail.objects.get(car_model=car_model)
        detail.quantity += 1
        detail.save()
    else:
        detail = OrderDetail.objects.create(car_model=car_model, quantity=1, order=order)
        detail.save()
    return redirect('order_detail')
"""


"""
class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    context_object_name = 'orders'
    template_name = 'orders/order_list.html'
    login_url = 'account_login'
"""

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

