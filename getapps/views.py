from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *

class AllDataView(APIView):
    def get(self, request, *args, **kwargs):
        lang = self.kwargs.get("lang", None)

        def filter_by_language(queryset):
            if lang and hasattr(queryset.model, 'language'):
                return queryset.filter(language=lang)
            return queryset

        faqs = filter_by_language(FAQ.objects.all())
        exchange_rules = filter_by_language(ExchangeRule.objects.all())
        kyc_aml_checks = filter_by_language(KYCAMLCheck.objects.all())
        currency_news = filter_by_language(CurrencyNews.objects.all())
        one_moments = filter_by_language(OneMoment.objects.all())
        contacts = filter_by_language(Contact.objects.all())  # Assuming no language field
        contests =filter_by_language(Contest.objects.all())# Assuming no language field
        footers = filter_by_language(Footer.objects.all())


        data = {
            'faqs': FAQSerializer(faqs, many=True).data,
            'exchange_rules': ExchangeRuleSerializer(exchange_rules, many=True).data,
            'kyc_aml_checks': KYCAMLCheckSerializer(kyc_aml_checks, many=True).data,
            'currency_news': CurrencyNewsSerializer(currency_news, many=True).data,
            'one_moments': OneMomentSerializer(one_moments, many=True).data,
            'contacts': ContactSerializer(contacts, many=True).data,
            'contests': ContestSerializer(contests, many=True).data,
            'footers': FooterSerializer(footers, many=True).data,
        }

        return Response(data)
class ReviewListCreate(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        reviews = Review.objects.all().order_by('-date_posted')
        serializer = ReviewSerializer(reviews, many=True)
        return Response({
            'response': True,
            'data': serializer.data
        })

    def post(self, request, *args, **kwargs):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Получаем последние отзывы после успешного сохранения, чтобы обновить список
            reviews = Review.objects.all().order_by('-date_posted')
            updated_serializer = ReviewSerializer(reviews, many=True)
            return Response({
                'response': True,
                'data': updated_serializer.data,
                'message': 'Отзыв успешно создан.'
            }, status=status.HTTP_201_CREATED)
        return Response({
            'response': False,
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
