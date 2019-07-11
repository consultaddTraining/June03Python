from django.db import models


# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class E(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class WorkHours(models.Model):
    name = models.ForeignKey("Employee", on_delete=models.PROTECT)
    days = models.DateField()
    hours = models.IntegerField()


    def __int__(self):
        return self.days


class Salary(models.Model):
    days = models.ForeignKey("WorkHours", on_delete=models.PROTECT)
    credited_salary = models.IntegerField()


class Login(models.Model):
    name = models.CharField(max_length=50, unique=False)
    email = models.EmailField()
    # password = models.CharField(max_length=50, unique=False)
