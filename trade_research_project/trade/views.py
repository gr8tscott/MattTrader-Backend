from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer, WatchlistSerializer, StockSerializer
from .models import User, Watchlist, Stock

# Create your views here.


# class UserList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class WatchlistView(viewsets.ModelViewSet):
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer


# class WatchlistDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Watchlist.objects.all()
#     serializer_class = WatchlistSerializer


class StockView(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


# class StockDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Stock.objects.all()
#     serializer_class = StockSerializer
