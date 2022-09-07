from rest_framework import serializers
from .models import User, Watchlist, Stock


class StockSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Stock
        fields = ('id', 'ticker', 'watchlist',)


class WatchlistSerializer(serializers.HyperlinkedModelSerializer):
    stocks = StockSerializer(

        many=True,
        read_only=True
    )

    class Meta:
        model = Watchlist
        fields = ('id', 'name', 'stocks',)


class UserSerializer(serializers.ModelSerializer):
    watchlists = WatchlistSerializer(

        many=True,
        read_only=True
    )

    class Meta:
        model = User
        fields = ('id', 'name', 'watchlists', 'email', 'password',)
