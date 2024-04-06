from django.contrib import admin
from .models import Stock, Market

admin.site.register(Market)
admin.site.register(Stock)