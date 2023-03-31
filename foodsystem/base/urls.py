"""base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from web_api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/food/', views.GetFood.as_view(), name = "GetFood"),
    path('api/food/addfood/', views.AddFood.as_view(), name = "AddFood"),
    path('api/food/listfood/', views.ListFood.as_view(), name = "ListFood"),
    path('api/food/updatefood/', views.UpdateFood.as_view(), name = "UpdateFood"),
    path('api/drink/', views.GetDrink.as_view(), name = "GetDrink"),
    path('api/drink/adddrink/', views.AddDrink.as_view(), name = "AddDrink"),
    path('api/drink/listdrink/', views.ListDrink.as_view(), name = "ListDrink"),
    path('api/side/', views.GetSide.as_view(), name = "GetSide"),
    path('api/side/addside/', views.AddSide.as_view(), name = "AddSide"),
    path('api/side/listside/', views.ListSide.as_view(), name = "ListSide"),

    
]
