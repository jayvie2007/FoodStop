from django.shortcuts import render
from .serializers import FoodSerializer, FoodData, FoodUpdate, DrinkSerializer, DrinkData, SideSerializer, SideData
from .models import FoodList, DrinkList, SideList

from rest_framework.views import APIView
from rest_framework.response import Response

from constant.status_code import *

import uuid


# Create your views here.

class GetFood(APIView):
    def get(self, request):
        foods =  FoodList.objects.all()
        serializers = FoodSerializer(foods, many=True)
        return Response({"Foods Registered": serializers.data})

class AddFood(APIView):
    def post(self, request):
        food = request.data['name']
        serialiazers = FoodSerializer(data = request.data)
        uid = generate_uuid()
        request.data._mutable = True
        request.data['uid'] = uid
        request.data._mutable = False
        if serialiazers.is_valid():
            message = (f"{food} is currently in the food list")
            try:
                foodname = FoodList.objects.get(
                    name = food, 
                )
                return Response(data = {"status": error, "message":message})
            except:
                    serialiazers.save()
                    message = (f"{food} has been added")
                    return Response(data={"status": ok, 'message': message})
        return Response(serialiazers.errors, status=error)

class ListFood(APIView):
    def post(self, request):     
        foodInput = request.data['name']
        serialiazers = FoodData(data=request.data)
        if serialiazers.is_valid():
            message = ("Food Data Successfully gotten")
            try:
                foods = FoodList.objects.get(
                    name = foodInput,
                )
                return Response(data = {"status": ok, 'message': message, 'foods' : serialiazers.data})
            except:
                return Response(data = {"status": not_found, 'message': no_info})
        return Response(serialiazers.errors, status=error)
    
    def put(self, request, uid):
        try:
            foodlist = FoodList.objects.get(uid = uid)
            foodInput = request.data['name']
            priceInput = int(request.data['price'])
        except FoodList.DoesNotExist:
            return Response(status=not_found)

        serializers = FoodUpdate(foodlist, data=request.data)
       
        if (priceInput != foodlist.price) and (foodInput != foodlist.name):
            message = (f"{foodlist.name} has been updated to {foodInput} and its price from {foodlist.price} into {priceInput}")
        elif priceInput != foodlist.price:
            message = (f"The price has been updated to {priceInput} from {foodlist.price}")
        elif foodInput != foodlist.name:
            message = (f"The food name has been changed to {foodInput} from {foodlist.name}")
        else:
            message = ("Nothing has been changed")
        if serializers.is_valid():
            serializers.save()
            return Response(data = {"message": message , 'status': ok})
        return Response(serializers.errors, status=error)

    def delete(self, request, uid):
            try:
                foodlist = FoodList.objects.get(uid = uid)
            except FoodList.DoesNotExist:
                return Response(status=not_found)
            foodlist.delete()
            return Response(status = no_data)

class GetDrink(APIView):
    def get(self, request):
        foods =  DrinkList.objects.all()
        serializers = DrinkSerializer(foods, many=True)
        return Response({"Drinks Registered": serializers.data})
        
class AddDrink(APIView):
    def post(self, request):
        drink = request.data['name']
        serializers = DrinkSerializer(data = request.data)
        uid = generate_uuid()
        request.data._mutable = True
        request.data['uid'] = uid
        request.data._mutable = True
        if serializers.is_valid():
            message = (f"{drink} is currently in the drink lists")
            try:
                drinkname = DrinkList.objects.get(
                    name = drink
                )
                return Response(data = {"status": error, "message": message})
            except:    
                serializers.save()
                message = (f"{drink} has been added to the drink lists")
                return Response(data = {"status":created, 'message': message})
        return Response(serializers.errors, status=error)

class ListDrink(APIView):
    def post(self, request):
        side = request.data['name']
        serializers = SideData(data = request.data)
        if serializers.is_valid():
            message = ("The side dish has successfully been gotten")
            try:
                sidelist = SideList.objects.get(
                    name = side
                )
                return Response(data = {"status": ok, "message": message ["sides" :serializers.data]})
            except:
                return Response(data={"message": no_info})
            
    def put(self, request, uid):
        try:
            sidelist = SideList.objects.get(uid = uid)
            side = request.data['name']
            price = int(request.data['price'])
        except SideList.DoesNotExist:
            return Response(status=not_found)
        #serializers = side        

    def delete(self, request, uid):
        try:
            sidelist = SideList.objects.get(uid = uid)
        except SideList.DoesNotExist:
            return Response(status=not_found)
        sidelist.delete()
        return Response(status = no_data)

class AddSide(APIView):
    def post(self, request):
        side = request.data['name']
        serializers = SideSerializer(data = request.data)
        uid = generate_uuid()
        request.data._mutable = True
        request.data['uid'] = uid
        request.data._mutable = False
        sides = request.data['name']
        if serializers.is_valid():
            message = (f"{sides} is currently in the side list")
            try:
                sidelist = SideList.objects.get(
                    name = side
                )
                return Response(data = {"status": error, "message": message})
            except:
                message = (f"{sides} has been added to the Sides list")
                serializers.save()
                return Response(data = {"status": created, "message":message})
        return Response(serializers.errors, status=error)

class GetSide(APIView):
    def get(self, request):
        foods =  SideList.objects.all()
        serializers = SideSerializer(foods, many=True)
        return Response({"Sides Registered": serializers.data})
    
class ListSide(APIView):
    def post(self, request):
        sideInput = ['name']
        serializers = SideData(data = request.data)

def generate_uuid():
    uid = uuid.uuid4().hex[-8:]
    return uid