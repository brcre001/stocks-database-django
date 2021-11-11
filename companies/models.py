from django.db import models
from django.db.models.fields import NullBooleanField

# This is to import user class from Django
# from django.contrib.auth.models import User

# Create your models here.

class Stock(models.Model):
    ticker = models.CharField(max_length=10)
    open = models.FloatField()
    close = models.FloatField()
    volume = models.IntegerField()

    def __str__(self):
        return self.ticker

class Cryptocurrency(models.Model):
    name = models.CharField(max_length=75)
    symbol = models.CharField(max_length=10)
    current_price = models.FloatField(null=True, default=0)

    def __str__(self):
        return self.name