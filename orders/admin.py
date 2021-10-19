from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from orders.models import Employee, Order, OrderDetail, Firm


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'employee'


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline,)


class OrderInline(admin.TabularInline):
    model = OrderDetail


class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderInline,
    ]
    list_display = ("id", "employee", "firm", "created_at", "updated_at", "total_price",)


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(Firm)
admin.site.register(User, UserAdmin)
admin.site.register(Order, OrderAdmin)
