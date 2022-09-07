from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Watchlist(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='watchlists')
    name = models.CharField(max_length=100, default='Name your watchlist')

    def __str__(self):
        return self.name


class Stock(models.Model):
    watchlist = models.ForeignKey(
        Watchlist, on_delete=models.CASCADE, related_name='stocks')
    ticker = models.CharField(max_length=10)

    def __str__(self):
        return self.ticker
