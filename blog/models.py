from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name=models.ForeignKey(User,on_delete=models.CASCADE)

class sagar(models.Model):
    pass

class tina():
    pass

class tiny():
    pass
class appaji():
    pass
class corona():
    pass

class Mehfil():
    pass




