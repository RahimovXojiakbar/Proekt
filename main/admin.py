from django.contrib import admin
from unfold.admin import ModelAdmin
from main import models


@admin.register(models.President)
class PresidentAdmin(ModelAdmin):
    list_display = ['uuid', 'name']
    search_fields = ['name']
    list_filter = ['information']
    
# =======================================================================================================

@admin.register(models.State)
class StateAdmin(ModelAdmin):
    list_display = ['uuid', 'title']
    search_fields = ['title']
    list_filter = ['president']

# =======================================================================================================

@admin.register(models.Governor_Region)
class GovernorRegionAdmin(ModelAdmin):
    list_display = ['uuid', 'name']
    search_fields = ['name']
    list_filter = ['information']

# =======================================================================================================

@admin.register(models.Region)
class RegionAdmin(ModelAdmin):
    list_display = ['uuid', 'title']
    search_fields = ['title']
    list_filter = ['state', 'governor']

# =======================================================================================================

@admin.register(models.Governor_District)
class GovernorDistrictAdmin(ModelAdmin):
    list_display = ['uuid', 'name']
    search_fields = ['name']
    list_filter = ['information']

# =======================================================================================================

@admin.register(models.District)
class DistrictAdmin(ModelAdmin):
    list_display = ['uuid', 'title']
    search_fields = ['title']
    list_filter = ['region', 'governor']  

# =======================================================================================================

@admin.register(models.Chairman)
class ChairmanAdmin(ModelAdmin):
    list_display = ['uuid', 'name']
    search_fields = ['name']
    list_filter = ['information']

# =======================================================================================================

@admin.register(models.MFY)
class MFYAdmin(ModelAdmin):
    list_display = ['uuid', 'title']
    search_fields = ['title']
    list_filter = [ 'district','chairman']

# =======================================================================================================

@admin.register(models.Neighborhood)
class NeighborhoodAdmin(ModelAdmin):
    list_display = ['uuid', 'title']
    search_fields = ['title']
    list_filter = ['MFY']

# =======================================================================================================

@admin.register(models.House)
class HouseAdmin(ModelAdmin):
    list_display = ['uuid', 'house_number', 'a_b']
    search_fields = ['house_number']
    list_filter = ['a_b', 'neighborhood', 'status']

# =======================================================================================================

@admin.register(models.Human)
class HumanAdmin(ModelAdmin):
    list_display = ['uuid', 'name']
    search_fields = ['fullname']
    list_filter = ['status', 'information', 'house']

    
