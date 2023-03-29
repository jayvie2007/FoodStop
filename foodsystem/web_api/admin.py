from django.contrib import admin
from .models import FoodList, DrinkList, Sidelist

# Register your models here.
admin.site.register(FoodList)
admin.site.register(DrinkList)
admin.site.register(Sidelist)

admin.site.site_header = ("Food Database")