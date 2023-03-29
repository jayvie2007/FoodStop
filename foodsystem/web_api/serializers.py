from .models import FoodList, DrinkList, SideList
from rest_framework import serializers

##################FOODS############################
class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        models = FoodList
        fields = '__all__'

class FoodData(serializers.ModelSerializer):
    class Meta:
        models = FoodList
        fields = ['name']


##################DRINKS############################
class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        models = DrinkList
        fields = '__all__'

class DrinkData(serializers.ModelSerializer):
    class Meta:
        models = DrinkList
        fields = ['name']

##################SIDES############################
class SideSerializer(serializers.ModelSerializer):
    class Meta:
        models = SideList
        fields = '__all__'

class SideData(serializers.ModelSerializer):
    class Meta:
        models = SideList
        fields = ['name']
        