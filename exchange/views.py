from rest_framework.views import APIView
from rest_framework.response import response
from rest_framework import status
from .serializers import ConversionSerializer, CurrencyListSerializer
from .services import perform_conversion, get_suppored_cryptocurrecies, get_supported_fiat_currencies


class ConverCurrencyView(APIView):
    def post(self,request,*args,**kwargs):
        serializer = ConversionSerializer(data=request.data)
        if serializer.is_valid():
            amount = serializer.validated_data['amount']
            from_currency = serializer.validated['from_currency']
            to_currency = serializer.validated_data['to_currency']

            try:
                converted_amount = perform_conversion(amount,from_currency,to_currency)
                return Response({'converted_amount': converted_amount},status=status.HTTP_200_OK)
            except ValueError as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        