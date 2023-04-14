from .models import FoodList, DrinkList, SideList
from rest_framework import serializers

##################FOODS############################
class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodList
        fields = '__all__'
  
class FoodData(serializers.ModelSerializer):
    class Meta:
        model = FoodList
        fields = ['name']

class FoodUpdate(serializers.ModelSerializer):
    class Meta:
        model = FoodList
        fields = ['name', 'price']


##################DRINKS############################
class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrinkList
        fields = '__all__'

class DrinkData(serializers.ModelSerializer):
    class Meta:
        model = DrinkList
        fields = ['name']

class DrinkUpdate(serializers.ModelSerializer):
    class Meta:
        model = DrinkList
        fields = ['name', 'price']

##################SIDES############################
class SideSerializer(serializers.ModelSerializer):
    class Meta:
        model = SideList
        fields = '__all__'

class SideData(serializers.ModelSerializer):
    class Meta:
        model = SideList
        fields = ['name']
        
class SideUpdate(serializers.ModelSerializer):
    class Meta:
        model = SideList
        fields = ['name', 'price']