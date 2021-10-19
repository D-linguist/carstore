from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True, unique=True)
    country = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Warehouse(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.name


class CarModel(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Record(models.Model):
    carmodel = models.ForeignKey('CarModel', models.CASCADE, blank=True, null=True)
    warehouse = models.ForeignKey('Warehouse', models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ["carmodel"]

    def __str__(self):
        return self.carmodel.name
