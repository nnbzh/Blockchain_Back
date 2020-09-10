from django.db import models


class CurrencyRecord(models.Model):
    name = models.CharField(max_length=300)
    symbol = models.CharField(max_length=300)
    price = models.FloatField()