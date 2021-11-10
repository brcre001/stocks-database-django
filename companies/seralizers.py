from rest_framework import serializers
from .models import Stock

class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stock
        # If you want to return everything
        # this is a shortcut
        # fields = '__all__'
        # do not do the above comment if you have sensitive data
        fields = ('ticker', 'volume')
