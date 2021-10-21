from django.urls import path
from .views import BrandListView, CarModelListView, WarehouseListView, RecordListView, \
    SearchBrandsListView, SearchCarModelsListView, SearchRecordsListView, \
    BrandListAPIView, BrandDetailAPIView, CarModelListAPIView, CarModelDetailAPIView, WarehouseListAPIView, WarehouseDetailAPIView, RecordListAPIView, RecordDetailAPIView, \
    car_model_detail


urlpatterns = [
    path('brands/', BrandListView.as_view(), name='brands'),
    path('car_models/', CarModelListView.as_view(), name='car_models'),
    path('car_models/<int:car_model_id>', car_model_detail, name='car_model_detail'),
    path('records/', RecordListView.as_view(), name='records'),
    path('warehouses/', WarehouseListView.as_view(), name='warehouses'),
    path('search_brands/', SearchBrandsListView.as_view(), name='brand_search_results'),
    path('search_car_models/', SearchCarModelsListView.as_view(), name='car_model_search_results'),
    path('search_records/', SearchRecordsListView.as_view(), name='record_search_results'),

    path('api/brands/<int:pk>', BrandDetailAPIView.as_view()),
    path('api/brands/', BrandListAPIView.as_view()),
    path('api/carmodels/<int:pk>', CarModelDetailAPIView.as_view()),
    path('api/carmodels', CarModelListAPIView.as_view()),
    path('api/records/<int:pk>', RecordDetailAPIView.as_view()),
    path('api/records/', RecordListAPIView.as_view()),
    path('api/warehouses/<int:pk>', WarehouseDetailAPIView.as_view()),
    path('api/warehouses/', WarehouseListAPIView.as_view()),
]
