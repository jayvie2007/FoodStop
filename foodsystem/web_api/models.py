from django.db import models

# Create your models here.
class FoodList(models.Model):
    uid = models.CharField(max_length=8)
    name = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return self.name + " " + self.price
    
class DrinkList(models.Model):
    uid = models.CharField(max_length=8)
    name = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return self.name + " " + self.price

class Sidelist(models.Model):
    uid = models.CharField(max_length=8)
    name = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return self.name + " " + self.price