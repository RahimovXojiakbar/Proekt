from rest_framework.serializers import  ModelSerializer, SlugRelatedField
from . import models


class PresidentSerializer(ModelSerializer):
    class Meta:
        model = models.President
        fields = '__all__'

# =======================================================================================================

class StateSerializer(ModelSerializer):
    president = SlugRelatedField(slug_field = 'name', read_only = True )
    class Meta:
        model = models.State
        fields = '__all__'

# =======================================================================================================

class GovernorRegionSerializer(ModelSerializer):
    class Meta:
        model = models.Governor_Region
        fields = '__all__'

# =======================================================================================================

class RegionSerializer(ModelSerializer):
    state = SlugRelatedField(slug_field = 'title', read_only = True )
    governor = SlugRelatedField(slug_field = 'name', read_only = True )
    class Meta:
        model = models.Region
        fields = '__all__'

# =======================================================================================================

class GovernorDistrictSerializer(ModelSerializer):
    class Meta:
        model = models.Governor_District
        fields = '__all__'

# =======================================================================================================

class DistrictSerializer(ModelSerializer):
    region = SlugRelatedField(slug_field = 'title', read_only = True )
    governor = SlugRelatedField(slug_field = 'name', read_only = True )
    class Meta:
        model = models.District
        fields = '__all__'

# =======================================================================================================

class ChairmanSerializer(ModelSerializer):
    class Meta:
        model = models.Chairman
        fields = '__all__'

# =======================================================================================================

class MFYSerializer(ModelSerializer):
    district = SlugRelatedField(slug_field = 'title', read_only = True )
    chairman = SlugRelatedField(slug_field = 'name', read_only = True )
    class Meta:
        model = models.MFY  
        fields = '__all__'

# =======================================================================================================

class NeighborhoodSerializer(ModelSerializer):
    MFY = SlugRelatedField(slug_field = 'title', read_only = True )
    class Meta:
        model = models.Neighborhood
        fields = '__all__'

# =======================================================================================================

class HouseSerializer(ModelSerializer):
    neighborhood = SlugRelatedField(slug_field = 'title', read_only = True )
    class Meta:
        model = models.House
        fields = '__all__'

# =======================================================================================================

class HumanSerializer(ModelSerializer):
    house = SlugRelatedField(slug_field = 'house_number', read_only = True )
    class Meta:
        model = models.Human
        fields = '__all__'