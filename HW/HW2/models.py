from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    date_registered = models.DateField(auto_now_add=True)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    date = models.DateField(auto_now_add=True)


class Order(models.Model):


    — связь
    с
    моделью «Клиент», указывает
    на
    клиента, сделавшего
    заказ
    — связь
    с
    моделью «Товар», указывает
    на
    товары, входящие
    в
    заказ
    — общая
    сумма
    заказа
    — дата
    оформления
    заказа