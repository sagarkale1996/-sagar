from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name=models.ForeignKey(User,on_delete=models.CASCADE)


class Order(models.Model):
    Ord=models.OneToOneField(Product,on_delete=models.CASCADE)

class Placed(models.Model):
    name=models.ManyToManyField(Order,)
    placed=models.CharField(max_length=120)