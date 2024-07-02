from rest_framework import serializers 

class ConversionSerializer(serializers.Serializer):
    amount = serializers.FloatField()
    from_currency = serializers.CharField(max_length=250)
    to_currency = serializers.CharField(max_length=240)
    converted_amount = serializers.FloatField(read_only=True)


class CurrencyListSerializer(serializers.Serializer):
    currencies = serializers.ListField(child=serializers.CharField(max_length=240)
    