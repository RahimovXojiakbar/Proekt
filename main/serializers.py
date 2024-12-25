from rest_framework.serializers import  ModelSerializer
from . import models


class PresidentSerializer(ModelSerializer):
    class Meta:
        model = models.President
        fields = '__all__'

class StateSerializer(ModelSerializer):
    class Meta:
        model = models.State
        fields = '__all__'


class GovernorRegionSerializer(ModelSerializer):
    class Meta:
        model = models.Governor_Region
        fields = '__all__'


class RegionSerializer(ModelSerializer):
    class Meta:
        model = models.Region
        fields = '__all__'


class GovernorDistrictSerializer(ModelSerializer):
    class Meta:
        model = models.Governor_District
        fields = '__all__'


class DistrictSerializer(ModelSerializer):
    class Meta:
        model = models.District
        fields = '__all__'


class ChairmanSerializer(ModelSerializer):
    class Meta:
        model = models.Chairman
        fields = '__all__'



class MFYSerializer(ModelSerializer):
    class Meta:
        model = models.MFY  
        fields = '__all__'


class NeighborhoodSerializer(ModelSerializer):
    class Meta:
        model = models.Neighborhood
        fields = '__all__'



class HouseSerializer(ModelSerializer):
    class Meta:
        model = models.House
        fields = '__all__'



class HumanSerializer(ModelSerializer):
    class Meta:
        model = models.Human
        fields = '__all__'