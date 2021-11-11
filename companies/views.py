from django.shortcuts import get_object_or_404
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cryptocurrency, Stock
from .seralizers import CryptocurrencySerializer, StockSerializer

# Create your views here.

# Class based views:

# Lists all stocks or create a new one
# Example URL: stocks/FB/
class StockList(APIView):

    def get(self, request):
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data)
    
    def post(self):
        pass


class CryptocurrencyList(APIView):

    def get(self, request):
        crypto = Cryptocurrency.objects.all()
        serializer = CryptocurrencySerializer(crypto, many=True)
        return Response(serializer.data)

    def post(self):
        pass