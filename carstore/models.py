from django.db import models


class Brand(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=3, blank=True, null=True)

    def __str__(self):
        return self.name


class Warehouse(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Record(models.Model):
    carmodel = models.ForeignKey('CarModel', models.CASCADE, blank=True, null=True)
    warehouse = models.ForeignKey('Warehouse', models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.carmodel.name




