from django.contrib import admin

from .models import Basket, Dress, Order

admin.site.register(Dress)
admin.site.register(Order)
admin.site.register(Basket)
