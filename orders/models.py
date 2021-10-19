from django.contrib.auth.models import User
from django.db import models
from carstore.models import CarModel


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.IntegerField

    def __str__(self):
        return self.user.username


class Firm(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.name


class EmployeeFirmsRelation(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE)


class Order(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE)
    total_price = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.car_model.name
