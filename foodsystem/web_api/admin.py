from django.contrib import admin
from .models import FoodList, DrinkList, SideList

# Register your models here.
admin.site.register(FoodList)
admin.site.register(DrinkList)
admin.site.register(SideList)

admin.site.site_header = ("Food Database")