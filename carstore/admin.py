from django.contrib import admin
from .models import Brand, CarModel, Record, Warehouse


class CarModelInline(admin.TabularInline):
    model = CarModel


class BrandAdmin(admin.ModelAdmin):
    inlines = [
        CarModelInline,
    ]
    list_display = ("name", "country",)


class RecordInline(admin.TabularInline):
    model = Record


class CarModelAdmin(admin.ModelAdmin):
    inlines = [
        RecordInline,
    ]
    list_display = ("name", "brand",)


admin.site.register(Warehouse)
admin.site.register(Brand, BrandAdmin)
admin.site.register(CarModel, CarModelAdmin)
