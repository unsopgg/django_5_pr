from django.contrib import admin

from applications.car.models import Car, Brand, Model

admin.site.register(Model)
admin.site.register(Brand)
admin.site.register(Car)

