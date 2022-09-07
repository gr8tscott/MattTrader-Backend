
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('watchlists', views.WatchlistView)
router.register('stocks', views.StockView)
router.register('user', views.UserView)
urlpatterns = [
    path('', include(router.urls))
    #     path('user/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    #     path('watchlists', views.WatchlistList.as_view(), name='watchlist_list'),
    #     path('watchlists/<int:pk>', views.WatchlistDetail.as_view(),
    #          name='watchlist_detail'),
    #     path('stocks', views.StockList.as_view(), name='stock_research'),
    #     path('stocks/<int:pk>',
    #          views.StockDetail.as_view(), name='stock_detail')
]
