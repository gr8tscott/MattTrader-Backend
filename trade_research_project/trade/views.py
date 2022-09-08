from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, WatchlistSerializer, StockSerializer, CreateStockSerializer
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


class CreateStockView(APIView):
    serializer_class = CreateStockSerializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            ticker = serializer.data.get('ticker')
            host = self.request.session.session_key
            queryset = Stock.objects.filter(host=host)
            if queryset.exists():
                stock = queryset[0]
                stock.ticker = ticker
                stock.save(update_fields=['ticker'])
            else:
                stock = Stock(host=host, ticker=ticker)
                stock.save()
            return Response(StockSerializer(stock).data, status=status.HTTP_201)


# class StockDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Stock.objects.all()
#     serializer_class = StockSerializer
