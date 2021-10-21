from django.urls import path

from .views import order_detail_list, order_list, add_order, \
    OrderListAPIView, OrderDetailAPIView, FirmListAPIView, OrderDetailListAPIView, OrderDetailDetailAPIView

urlpatterns = [
    path('', order_list, name='orders'),
    path('<int:order>/', order_detail_list, name='order_detail'),
    path('add_order/<int:car_model_id>', add_order, name='add_order'),

    path('api/firms/', FirmListAPIView.as_view()),
    path('api/orders/', OrderListAPIView.as_view()),
    path('api/orders/<int:pk>', OrderDetailAPIView.as_view()),
    path('api/order_details/', OrderDetailListAPIView.as_view()),
    path('api/order_details/<int:pk>', OrderDetailDetailAPIView.as_view()),
]
