from django.urls import path
from .views import ConvertCurrencyView

urlpatters = [
    path('convert/',ConvertCurrencyView.as_view(), name='convert-currency')
]
