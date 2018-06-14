from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    symbol = models.CharField(max_length=60)
    description = models.TextField(blank=True)
    unit = models.CharField(max_length=10)

    def __str__(self):
        return self.symbol


class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders')
    product = models.ForeignKey('store.Product', related_name='orders')
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return '{} {}'.format(self.user.get_full_name(), self.product.symbol)
