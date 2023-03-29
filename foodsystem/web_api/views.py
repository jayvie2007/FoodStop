from django.shortcuts import render
from .serializers import FoodSerializer, FoodData, DrinkSerializer, DrinkData, SideSerializer, SideData
from .models import FoodList, DrinkList, SideList

from rest_framework.views import APIView
from rest_framework.response import Response

from constant import status_code



# Create your views here.
class AddFood(APIView):
    def post():
        pass
    
class GetFood(APIView):
    def get(self, request):
        foods =  FoodList.objects.all()
        serializers = FoodSerializer(foods, many=True)
        return Response({"Foods Registered": serializers.data})

class AddDrink(APIView):
    def post():
        pass

class GetDrink(APIView):
    def get(self, request):
        foods =  FoodList.objects.all()
        serializers = FoodSerializer(foods, many=True)
        return Response({"Drinks Registered": serializers.data})

class AddSide(APIView):
    def post():
        pass

class GetSide(APIView):
    def get(self, request):
        foods =  FoodList.objects.all()
        serializers = FoodSerializer(foods, many=True)
        return Response({"Sides Registered": serializers.data})