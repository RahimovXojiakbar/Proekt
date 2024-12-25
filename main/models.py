from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from shortuuid.django_fields import ShortUUIDField


class MyShortUuid(models.Model):
    uuid = ShortUUIDField(
        primary_key=True,
        editable=False,
        max_length=12,
        alphabet = 'abcdefghijklmnopqrstuvwxz123456789',
    )
    
    class Meta:
        abstract  = True

# -------------------------------------------------------------------------------------------

class President(MyShortUuid):
    name = models.CharField(max_length=200)
    information =  models.CharField(max_length=200, choices={'MIDDLE':'MIDDLE', 'HIGH':'HIGH'})
    party = models.CharField(max_length=200)
    BIO = CKEditor5Field(config_name='extends')
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-uuid']

# -------------------------------------------------------------------------------------------

class State(MyShortUuid):
    title = models.CharField(max_length=200)
    president = models.ForeignKey(President, on_delete=models.SET_NULL, null=True, related_name='state')
    about = CKEditor5Field(config_name='extends')
    flag = models.ImageField(blank=True, upload_to='images')
    anthem = models.TextField()
    emblem = models.ImageField(upload_to='images', blank=True)
    area_km_kv = models.DecimalField(decimal_places=2, max_digits=10)
    regions = models.PositiveIntegerField()
    people = models.PositiveIntegerField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-uuid']

# -------------------------------------------------------------------------------------------

class Governor_Region(MyShortUuid):
    name = models.CharField(max_length=200)
    information =  models.CharField(max_length=200, choices={'MIDDLE':'MIDDLE', 'HIGH':'HIGH'})
    BIO = CKEditor5Field(config_name='extends')
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-uuid']

# -------------------------------------------------------------------------------------------

class Region(MyShortUuid):
    title = models.CharField(max_length=200)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, related_name='region')
    governor = models.ForeignKey(Governor_Region, on_delete=models.SET_NULL, null=True, related_name='region')
    about = CKEditor5Field(config_name='extends')
    area_km_kv = models.DecimalField(decimal_places=2, max_digits=10)
    districts = models.PositiveIntegerField()
    people = models.PositiveIntegerField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-uuid']

# -------------------------------------------------------------------------------------------

class Governor_District(MyShortUuid):
    name = models.CharField(max_length=200)
    information =  models.CharField(max_length=200, choices={'MIDDLE':'MIDDLE', 'HIGH':'HIGH'})
    BIO = CKEditor5Field(config_name='extends')
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-uuid']

# -------------------------------------------------------------------------------------------

class District(MyShortUuid):
    title = models.CharField(max_length=200)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, related_name='district')
    governor = models.ForeignKey(Governor_District, on_delete=models.SET_NULL, null=True, related_name='district')
    about = CKEditor5Field(config_name='extends')
    area_km_kv = models.DecimalField(decimal_places=2, max_digits=10)
    MFY = models.PositiveIntegerField()
    people = models.PositiveIntegerField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-uuid']


# -------------------------------------------------------------------------------------------

class Chairman(MyShortUuid):
    name = models.CharField(max_length=200)
    BIO = CKEditor5Field(config_name='extends')
    information =  models.CharField(max_length=200, choices={'MIDDLE':'MIDDLE', 'HIGH':'HIGH'})
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-uuid']

# -------------------------------------------------------------------------------------------


class MFY(MyShortUuid):
    title = models.CharField(max_length=200)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, related_name='d_MFY')
    chairman = models.ForeignKey(Chairman, on_delete=models.SET_NULL, null=True, related_name='C_MFY')
    area_km_kv = models.DecimalField(decimal_places=2, max_digits=10)
    neighborhoods = models.PositiveIntegerField()
    people = models.PositiveIntegerField()
    created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-uuid']

# -------------------------------------------------------------------------------------------


class Neighborhood(MyShortUuid):   
    title = models.CharField(max_length=200)
    elder = models.CharField(max_length=250)
    MFY = models.ForeignKey(MFY, on_delete=models.SET_NULL, null=True)
    area_km_kv = models.DecimalField(decimal_places=2, max_digits=15)
    houses = models.PositiveIntegerField()
    people = models.PositiveIntegerField()
    created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['-uuid']

# -------------------------------------------------------------------------------------------


class House(MyShortUuid):
    house_boss = models.CharField(max_length=200)
    house_number= models.PositiveIntegerField()
    a_b = models.CharField(max_length=200, choices={ 'A':'A', 'B':'B'})
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.SET_NULL, null=True, related_name='house')
    status = models.CharField(max_length=200, choices={'POORER':'POORER', 'MIDDLE':'MIDDLE','RICH':'RICH'})
    people = models.PositiveIntegerField(blank=True)
    area_kv_m = models.DecimalField(decimal_places=2, max_digits=15)
    created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.house_number} {self.a_b}"

    class Meta:
        ordering = ['house_number', 'a_b']

      
# -------------------------------------------------------------------------------------------


class Human(MyShortUuid):
    name = models.CharField(max_length=200)
    BIO = CKEditor5Field(config_name='extends')
    status = models.CharField(max_length=200, choices={'Kindergarten':'Kindergarten', 'Schoolboy':'Schoolboy', 'Student':'Student', 'Worker':'Worker'})
    information = models.CharField(max_length=200, choices={'NO':'NO', 'MIDDLE':'MIDDLE','HIGH':'HIGH'}, default='NO')
    house = models.ForeignKey(House, on_delete=models.SET_NULL, null=True, related_name='human')
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

# -------------------------------------------------------------------------------------------
