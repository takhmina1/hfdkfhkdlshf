from django.urls import path
from .views import *

urlpatterns = [
    path('<str:lang>/combined/', AllDataView.as_view(), name='combined-view'),
    path('reviews/', ReviewListCreate.as_view(), name='review-list-create'),
]
