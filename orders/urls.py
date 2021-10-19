from django.urls import path

from .views import order_detail_list, order_list, add_order

urlpatterns = [
    path('', order_list, name='orders'),
    path('<int:order>/', order_detail_list, name='order_detail'),
    path('add_order/<int:car_model_id>', add_order, name='add_order'),
]
