from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from .serializers import StockSerializer
from home.models import Stock
from rest_framework.authentication import TokenAuthentication,RemoteUserAuthentication, SessionAuthentication

class StockView(ListCreateAPIView):
    serializer_class = StockSerializer
    queryset = Stock.objects.all()
    authentication_classes = (TokenAuthentication, )