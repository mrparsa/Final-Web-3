from django.urls import path
from .views import *

urlpatterns = [
    path('list_stock/', StockView.as_view(), name='liststock'),
]