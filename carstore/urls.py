from django.urls import path
from .views import BrandListView, CarModelListView, WarehouseListView, RecordListView, \
    SearchBrandsListView, SearchCarModelsListView, \
    BrandList, BrandDetail, CarModelList, CarModelDetail, WarehouseList, WarehouseDetail, RecordList, RecordDetail, \
    SearchRecordsListView

urlpatterns = [
    path('brands/', BrandListView.as_view(), name='brands'),
    path('car_models/', CarModelListView.as_view(), name='car_models'),
    path('records/', RecordListView.as_view(), name='records'),
    path('warehouses/', WarehouseListView.as_view(), name='warehouses'),
    path('search_brands/', SearchBrandsListView.as_view(), name='brand_search_results'),
    path('search_car_models/', SearchCarModelsListView.as_view(), name='car_model_search_results'),
    path('search_records/', SearchRecordsListView.as_view(), name='record_search_results'),

    path('brandsapi/<int:pk>/', BrandDetail.as_view()),
    path('brandsapi/', BrandList.as_view()),
    path('carmodelsapi/<int:pk>', CarModelDetail.as_view()),
    path('carmodelsapi/', CarModelList.as_view()),
    path('recordsapi/<int:pk>', RecordDetail.as_view()),
    path('recordsapi/', RecordList.as_view()),
    path('warehousesapi/<int:pk>', WarehouseDetail.as_view()),
    path('warehousesapi/', WarehouseList.as_view()),
]
