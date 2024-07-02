from django.db import models
from django.contrib.auth.models import User


class ExchangeOperation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    from_currency = models.CharField(max_length=100)
    to_curren