from django.db import models


class Product(models.Model):
    symbol = models.CharField(max_length=60)
    description = models.TextField(blank=True)
    unit = models.CharField(max_length=10)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.symbol
