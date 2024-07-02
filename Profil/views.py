from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
class ApplicationListCreateAPIView(generics.ListAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = Application.objects.all()
        lang = self.kwargs.get("lang", None)
        if lang:
            queryset = queryset.filter(language=lang)
        return queryset
class DiscountListCreateAPIView(generics.ListAPIView):
    serializer_class = DiscountSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = Discount.objects.all()
        lang = self.kwargs.get("lang", None)
        if lang:
            # Example of filtering based on related model field
            queryset = queryset.filter(application__language=lang)
        return queryset
class ProgramListCreateAPIView(generics.ListAPIView):
    serializer_class = ProgramSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Program.objects.all()
        lang = self.kwargs.get("lang", None)
        if lang:
            queryset = queryset.filter(language=lang)
        return queryset