from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Coin, FiatCurrency
from .serializers import CoinSerializer, FiatCurrencySerializer
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from django.http import JsonResponse



class CoinDataAPIView(APIView):
    def get(self, request, *args, **kwargs):
        coins = Coin.objects.all()
        serializer = CoinSerializer(coins, many=True)
        data = {
            'success': 1,
            'data': serializer.data
        }
        return Response(data)



class FiatCurrencyListView(APIView):
    def get(self, request):
        fiat_currencies = FiatCurrency.objects.all()
        serializer = FiatCurrencySerializer(fiat_currencies, many=True)
        data = {
            "code": "000000",
            "message": None,
            "messageDetail": None,
            "data": {
                "fiatList": serializer.data
            }
        }
        return Response(data)





