import datetime

from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()


class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    person = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    final_cost = models.PositiveIntegerField()

    def calculate_final_cost(self, birthdate):
        today = datetime.datetime.now().date()
        if birthdate and birthdate.month == today.month and birthdate.day == today.day:
            discount = 0.1
        else:
            discount = 0.0
        return self.product.price * (1 - discount)
