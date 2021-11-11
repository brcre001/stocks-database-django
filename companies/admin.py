from django.contrib import admin
from .models import Cryptocurrency, Stock

# Register your models here.

admin.site.register(Stock)
admin.site.register(Cryptocurrency)