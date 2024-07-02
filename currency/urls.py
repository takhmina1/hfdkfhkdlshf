# urls.py
from django.urls import path
from .views import CoinDataAPIView, FiatCurrencyListView

urlpatterns = [
    path('api/coins/', CoinDataAPIView.as_view(), name='coin_data_api'),
    path('api/fiat-currencies/', FiatCurrencyListView.as_view(), name='fiat_currency_list_api'),
]
