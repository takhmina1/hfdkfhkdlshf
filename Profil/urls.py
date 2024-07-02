from django.urls import path
from .views import *
urlpatterns = [
    path('api/applications/', ApplicationListCreateAPIView.as_view(), name='application-list-create'),
    path('api/discounts/', DiscountListCreateAPIView.as_view(), name='discount-list-create'),
    path('programs/list/<str:lang>', ProgramListCreateAPIView.as_view(), name='program-list-create'),

]