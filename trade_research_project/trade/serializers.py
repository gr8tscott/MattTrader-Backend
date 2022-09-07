from rest_framework import serializers
from .models import User, Watchlist, Stock


class UserSerializer(serializers.HyperlinkedModelSerializer):
    watchlists = serializers.HyperlinkedRelatedField(
        view_name='watchlist_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = User
        fields = ('id', 'name', 'watchlists', 'email', 'password',)


class WatchlistSerializer(serializers.HyperlinkedModelSerializer):
    stocks = serializers.HyperlinkedRelatedField(
        view_name='stock_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Watchlist
        fields = ('id', 'name', 'stocks',)


class StockSerializer(serializers.HyperlinkedModelSerializer):
    watchlist = serializers.HyperlinkedRelatedField(
        view_name='watchlist_detail',
        read_only=True
    )

    class Meta:
        model = Stock
        fields = ('id', 'ticker', 'watchlist',)
