from django.db import models

class Stock(models.Model):
    name = models.CharField(max_length=50)
    code_name = models.CharField(max_length=50)
    price = models.IntegerField()
    total_shares = models.IntegerField()
    state = models.BooleanField(default=False)


class Market(models.Model):
    name = models.CharField(max_length=50)
    index = models.IntegerField()


class Trade(models.Model):
    stock = models.OneToOneField(Stock, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    datetime = models.DateTimeField()
    # buyer = models.OneToOneField(User, on_delete=models.CASCADE)
    # seller = models.OneToOneField(User, on_delete=models.CASCADE)
