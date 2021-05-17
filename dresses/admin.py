from django.contrib import admin

from .models import Dress, Color, DressType, LeaseType, ImagesDress

admin.site.register(Dress)
admin.site.register(Color)
admin.site.register(ImagesDress)
admin.site.register(DressType)
admin.site.register(LeaseType)
