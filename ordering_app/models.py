from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os
import secrets

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"


def save_img(instance, filename):
    random_hex = secrets.token_hex(8)
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (random_hex, ext)
    return os.path.join('food', filename)


class Food(models.Model):
    cat_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="food_cat")
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to=save_img, null=True)
    toppings_no = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.cat_id.name}-{self.name}"


class Topping(models.Model):
    cat_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="topping_cat")
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.cat_id} - {self.name}"


class Price(models.Model):
    food_id = models.ForeignKey(Food, on_delete=models.CASCADE, related_name="price_food_id")
    name_selection = (
        ('O', 'One Size'),
        ('S', 'Small'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=1, choices=name_selection)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.get_name_display()}: {self.price}"


class Order(models.Model):
    cust_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="customer_id")
    status_selection = (
        ('NP', 'Not Placed'),
        ('PL', 'Placed'),
        ('IN', 'In Progress'),
        ('CO', 'Completed'),
    )
    status = models.CharField(max_length=2, choices=status_selection)

    def __str__(self):
        return f"order no: {self.id}"


class OrderItem(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_id")
    food_id = models.ForeignKey(Food, on_delete=models.CASCADE, related_name="order_food_id")
    food_price = models.ForeignKey(Price, on_delete=models.CASCADE, related_name="order_price_id")
    food_topping1 = models.ForeignKey(Topping, blank=True, null=True, on_delete=models.CASCADE, related_name="order_topping1_id")
    food_topping2 = models.ForeignKey(Topping, blank=True, null=True, on_delete=models.CASCADE, related_name="order_topping2_id")
    food_topping3 = models.ForeignKey(Topping, blank=True, null=True, on_delete=models.CASCADE, related_name="order_topping3_id")
    food_topping4 = models.ForeignKey(Topping, blank=True, null=True, on_delete=models.CASCADE, related_name="order_topping4_id")
    food_topping5 = models.ForeignKey(Topping, blank=True, null=True, on_delete=models.CASCADE, related_name="order_topping5_id")

    # def __str__(self):
    #     return f"order no: {self.order_id} items: {self.food_id}"