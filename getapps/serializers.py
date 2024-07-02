from rest_framework import serializers
from rest_framework.authtoken.admin import User
from .models import *
from googletrans import Translator

translator = Translator()


class FAQSerializer(serializers.ModelSerializer):
    language = serializers.CharField()
    class Meta:
        model = FAQ
        fields = '__all__'
class ExchangeRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeRule
        fields = '__all__'


class KYCAMLCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = KYCAMLCheck
        fields = '__all__'


class CurrencyNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyNews
        fields = '__all__'


class OneMomentSerializer(serializers.ModelSerializer):
    class Meta:
        model = OneMoment
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['email', 'website']


class ContestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contest
        fields = '__all__'
    def validate_participants(self, value):
        # Ensure participants is a positive integer
        if value < 0:
            raise serializers.ValidationError("Participants must be a positive integer.")
        return value
    def validate_prize_amount(self, value):
        # Ensure prize_amount is a valid decimal number
        try:
            prize_amount = float(value)
        except ValueError:
            raise serializers.ValidationError("Prize amount must be a valid number.")
        return prize_amount
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']
class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = '__all__'
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

