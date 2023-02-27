from django.db import models
import datetime

from django.contrib.auth.models import User
from django.utils import timezone


class Type(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"Type: {self.name}"


class Item(models.Model):
    type = models.ForeignKey(Type, related_name="items", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=100)
    available = models.BooleanField(default=True)
    item_description = models.TextField(blank=True, null=True, max_length=200)

    def __str__(self):
        return f"Type: {self.name}"


class Client(User):
    CITY_CHOICES = [
        ('WD', 'Windsor'),
        ('TO', 'Toronto'),
        ('CH', 'Chatham'),
        ('WL', 'WATERLOO'), ]
    shipping_address = models.CharField(max_length=300, null=True, blank=True)
    city = models.CharField(max_length=2, choices=CITY_CHOICES, default='CH')
    interested_in = models.ManyToManyField(Type)
    phone_number = models.TextField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f"Type: {self.get_full_name()}"

    class Meta:
        verbose_name = "Client"


# Create your models here.
class OrderItem(models.Model):
    item = models.ForeignKey(Item, related_name="order_items", on_delete=models.CASCADE)
    client = models.ForeignKey(Client, related_name="orders", on_delete=models.CASCADE)
    no_of_items = models.IntegerField(default=1, null=False, blank=False)
    ORDER_STATUS = [
        (0, "Cancelled"),
        (1, "Placed"),
        (2, "Shipped"),
        (3, "Delivered")
    ]
    status = models.IntegerField(choices=ORDER_STATUS, default=1)
    modified_at = models.DateTimeField(default=datetime.datetime.now())

    def total_price(self):
        self.item.price * self.no_of_items

    def __str__(self):
        return f"Type: {self.client.get_full_name()} - {self.item.name} x{self.no_of_items}"


class Description(models.Model):
    title = models.TextField(max_length=100)
    description = models.TextField(max_length=200)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ||| {self.description}"

# class ProjectTitle(models.Model):
#     title = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.title
#
#
# class ProjectDescription(models.Model):
#     desc = models.CharField(max_length=200)
#     modified_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.desc
#
#
# class Description(models.Model):
#     titles = models.ManyToManyField(ProjectTitle)
#     descriptions = models.ManyToManyField(ProjectDescription)
#
#     def __str__(self):
#         return f"Titles: {[o.get('title') for o in (self.titles.values())]} \n Descriptions: {[o.get('desc') for o in self.descriptions.values()]}"
