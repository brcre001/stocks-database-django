from rest_framework import serializers
from .models import Stock, Cryptocurrency

class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stock
        # If you want to return everything
        # this is a shortcut
        # fields = '__all__'
        # do not do the above comment if you have sensitive data
        fields = '__all__'

        # If you want only some of the data:
        # fields = ('ticker', 'volume')

class CryptocurrencySerializer(serializers.ModelSerializer):

    class Meta:
        model = Cryptocurrency
        fields = '__all__'