from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from shortuuid.django_fields import ShortUUIDField
from django.contrib.auth.models import User



class MyShortUuid(models.Model):
    uuid = ShortUUIDField(
        primary_key=True,
        editable=False,
        max_length=12,
        alphabet = 'abcdefghijklmnopqrstuvwxz123456789',
    )
    
    class Meta:
        abstract  = True

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class BaseModel(MyShortUuid):
    created = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class InformationLevel(models.TextChoices):
    HIGH = 'HIGH'
    MIDDLE = 'MIDDLE'
    NO = 'NO'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class President(BaseModel):
    name = models.CharField(max_length=200)
    information =  models.CharField(max_length=200, choices=InformationLevel.choices)
    party = models.CharField(max_length=200)
    BIO = CKEditor5Field(config_name='extends', default = '<p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque at ligula purus. Praesent aliquet ipsum risus, nec interdum nunc tempus quis. Proin ultricies mauris urna, vel sagittis libero fermentum in. Sed eleifend varius nisl eu ullamcorper. Vestibulum condimentum cursus pretium. Aenean sed nibh ac dui pulvinar porttitor ut id neque. Sed consequat sapien sed magna venenatis lacinia. Praesent ullamcorper dignissim viverra. Curabitur ac odio et ante volutpat condimentum. Pellentesque eu faucibus ipsum. Sed est ante, accumsan id tortor vitae, vestibulum auctor magna. Vivamus in neque neque. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam non leo sit amet nunc maximus bibendum vitae fringilla ex. </p>')

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-uuid']

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class State(BaseModel):
    title = models.CharField(max_length=200)
    president = models.OneToOneField(President, on_delete=models.SET_NULL, null=True, related_name='state')
    about = CKEditor5Field(config_name='extends', default = '<p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque at ligula purus. Praesent aliquet ipsum risus, nec interdum nunc tempus quis. Proin ultricies mauris urna, vel sagittis libero fermentum in. Sed eleifend varius nisl eu ullamcorper. Vestibulum condimentum cursus pretium. Aenean sed nibh ac dui pulvinar porttitor ut id neque. Sed consequat sapien sed magna venenatis lacinia. Praesent ullamcorper dignissim viverra. Curabitur ac odio et ante volutpat condimentum. Pellentesque eu faucibus ipsum. Sed est ante, accumsan id tortor vitae, vestibulum auctor magna. Vivamus in neque neque. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam non leo sit amet nunc maximus bibendum vitae fringilla ex. </p>')
    flag = models.ImageField(blank=True, upload_to='images')
    anthem = models.TextField(default = '<p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque at ligula purus. Praesent aliquet ipsum risus, nec interdum nunc tempus quis. Proin ultricies mauris urna, vel sagittis libero fermentum in. Sed eleifend varius nisl eu ullamcorper. Vestibulum condimentum cursus pretium. Aenean sed nibh ac dui pulvinar porttitor ut id neque. Sed consequat sapien sed magna venenatis lacinia. Praesent ullamcorper dignissim viverra. Curabitur ac odio et ante volutpat condimentum. Pellentesque eu faucibus ipsum. Sed est ante, accumsan id tortor vitae, vestibulum auctor magna. Vivamus in neque neque. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam non leo sit amet nunc maximus bibendum vitae fringilla ex. </p>')
    emblem = models.ImageField(upload_to='images', blank=True)
    language = models.CharField(max_length=200)
    area_km_kv = models.DecimalField(decimal_places=2, max_digits=10, default=450.54)
    regions = models.PositiveIntegerField(default=13)
    people = models.PositiveIntegerField(default=40000000)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-uuid']

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class GovernorRegion(BaseModel):
    name = models.CharField(max_length=200)
    information =  models.CharField(max_length=200, choices=InformationLevel.choices)
    BIO = CKEditor5Field(config_name='extends', default = '<p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque at ligula purus. Praesent aliquet ipsum risus, nec interdum nunc tempus quis. Proin ultricies mauris urna, vel sagittis libero fermentum in. Sed eleifend varius nisl eu ullamcorper. Vestibulum condimentum cursus pretium. Aenean sed nibh ac dui pulvinar porttitor ut id neque. Sed consequat sapien sed magna venenatis lacinia. Praesent ullamcorper dignissim viverra. Curabitur ac odio et ante volutpat condimentum. Pellentesque eu faucibus ipsum. Sed est ante, accumsan id tortor vitae, vestibulum auctor magna. Vivamus in neque neque. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam non leo sit amet nunc maximus bibendum vitae fringilla ex. </p>')

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-uuid']

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Region(BaseModel):
    title = models.CharField(max_length=200)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, related_name='region')
    governor = models.OneToOneField(GovernorRegion, on_delete=models.SET_NULL, null=True, related_name='region')
    about = CKEditor5Field(config_name='extends', default = '<p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque at ligula purus. Praesent aliquet ipsum risus, nec interdum nunc tempus quis. Proin ultricies mauris urna, vel sagittis libero fermentum in. Sed eleifend varius nisl eu ullamcorper. Vestibulum condimentum cursus pretium. Aenean sed nibh ac dui pulvinar porttitor ut id neque. Sed consequat sapien sed magna venenatis lacinia. Praesent ullamcorper dignissim viverra. Curabitur ac odio et ante volutpat condimentum. Pellentesque eu faucibus ipsum. Sed est ante, accumsan id tortor vitae, vestibulum auctor magna. Vivamus in neque neque. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam non leo sit amet nunc maximus bibendum vitae fringilla ex. </p>')
    area_km_kv = models.DecimalField(decimal_places=2, max_digits=10, default=83.95)
    districts = models.PositiveIntegerField(default=8)
    people = models.PositiveIntegerField(default=2500000)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-uuid']

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class GovernorDistrict(BaseModel):
    name = models.CharField(max_length=200)
    information =  models.CharField(max_length=200, choices=InformationLevel.choices)
    BIO = CKEditor5Field(config_name='extends', default = '<p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque at ligula purus. Praesent aliquet ipsum risus, nec interdum nunc tempus quis. Proin ultricies mauris urna, vel sagittis libero fermentum in. Sed eleifend varius nisl eu ullamcorper. Vestibulum condimentum cursus pretium. Aenean sed nibh ac dui pulvinar porttitor ut id neque. Sed consequat sapien sed magna venenatis lacinia. Praesent ullamcorper dignissim viverra. Curabitur ac odio et ante volutpat condimentum. Pellentesque eu faucibus ipsum. Sed est ante, accumsan id tortor vitae, vestibulum auctor magna. Vivamus in neque neque. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam non leo sit amet nunc maximus bibendum vitae fringilla ex. </p>')

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-uuid']

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class District(BaseModel):
    title = models.CharField(max_length=200)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, related_name='district')
    governor = models.OneToOneField(GovernorDistrict, on_delete=models.SET_NULL, null=True, related_name='district')
    about = CKEditor5Field(config_name='extends', default = '<p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque at ligula purus. Praesent aliquet ipsum risus, nec interdum nunc tempus quis. Proin ultricies mauris urna, vel sagittis libero fermentum in. Sed eleifend varius nisl eu ullamcorper. Vestibulum condimentum cursus pretium. Aenean sed nibh ac dui pulvinar porttitor ut id neque. Sed consequat sapien sed magna venenatis lacinia. Praesent ullamcorper dignissim viverra. Curabitur ac odio et ante volutpat condimentum. Pellentesque eu faucibus ipsum. Sed est ante, accumsan id tortor vitae, vestibulum auctor magna. Vivamus in neque neque. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam non leo sit amet nunc maximus bibendum vitae fringilla ex. </p>')
    area_km_kv = models.DecimalField(decimal_places=2, max_digits=10, default=45.58)
    MFYs = models.PositiveIntegerField(default=45)
    people = models.PositiveIntegerField(default=25000)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-uuid']

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Chairman(BaseModel):
    name = models.CharField(max_length=200)
    BIO = CKEditor5Field(config_name='extends', default = '<p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque at ligula purus. Praesent aliquet ipsum risus, nec interdum nunc tempus quis. Proin ultricies mauris urna, vel sagittis libero fermentum in. Sed eleifend varius nisl eu ullamcorper. Vestibulum condimentum cursus pretium. Aenean sed nibh ac dui pulvinar porttitor ut id neque. Sed consequat sapien sed magna venenatis lacinia. Praesent ullamcorper dignissim viverra. Curabitur ac odio et ante volutpat condimentum. Pellentesque eu faucibus ipsum. Sed est ante, accumsan id tortor vitae, vestibulum auctor magna. Vivamus in neque neque. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam non leo sit amet nunc maximus bibendum vitae fringilla ex. </p>')
    information =  models.CharField(max_length=200, choices=InformationLevel.choices)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-uuid']

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class MFY(BaseModel):
    title = models.CharField(max_length=200)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, related_name='d_MFY')
    chairman = models.OneToOneField(Chairman, on_delete=models.SET_NULL, null=True, related_name='C_MFY')
    area_km_kv = models.DecimalField(decimal_places=2, max_digits=10, default=15.75)
    neighborhoods = models.PositiveIntegerField(default=8)
    people = models.PositiveIntegerField(default=8500)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-uuid']

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Neighborhood(BaseModel):   
    title = models.CharField(max_length=200)
    elder = models.CharField(max_length=250, default='Jhon Doe')
    MFY = models.ForeignKey(MFY, on_delete=models.SET_NULL, null=True)
    area_km_kv = models.DecimalField(decimal_places=2, max_digits=15, default=4.65)
    houses = models.PositiveIntegerField(default=85)
    people = models.PositiveIntegerField(default=530)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['-uuid']

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class House(BaseModel):
    house_boss = models.CharField(max_length=200)
    house_number= models.PositiveIntegerField()
    a_b = models.CharField(max_length=200, choices={ 'A':'A', 'B':'B'})
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.SET_NULL, null=True, related_name='house')
    status = models.CharField(max_length=200, choices={'POORER':'POORER', 'MIDDLE':'MIDDLE','RICH':'RICH'})
    people = models.PositiveIntegerField(blank=True, default=5)
    area_kv_m = models.DecimalField(decimal_places=2, max_digits=15, default=415.5)

    def __str__(self) -> str:
        return f"{self.house_number} {self.a_b}"

    class Meta:
        ordering = ['house_number', 'a_b']
  
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Status(models.TextChoices):
    KINDERGARTEN = 'Kindergarten'
    SCHOOLBOY = 'Schoolboy'
    STUDENT = 'Student'
    WORKER = 'Worker'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Human(BaseModel):
    name = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField(default='example@mail.ru')
    BIO = CKEditor5Field(config_name='extends', default = '<p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque at ligula purus. Praesent aliquet ipsum risus, nec interdum nunc tempus quis. Proin ultricies mauris urna, vel sagittis libero fermentum in. Sed eleifend varius nisl eu ullamcorper. Vestibulum condimentum cursus pretium. Aenean sed nibh ac dui pulvinar porttitor ut id neque. Sed consequat sapien sed magna venenatis lacinia. Praesent ullamcorper dignissim viverra. Curabitur ac odio et ante volutpat condimentum. Pellentesque eu faucibus ipsum. Sed est ante, accumsan id tortor vitae, vestibulum auctor magna. Vivamus in neque neque. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam non leo sit amet nunc maximus bibendum vitae fringilla ex. </p>')
    status = models.CharField(max_length=200, choices=Status.choices)
    information = models.CharField(max_length=200, choices=InformationLevel.choices, default=InformationLevel.NO)
    house = models.ForeignKey(House, on_delete=models.SET_NULL, null=True, related_name='human')

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-uuid']

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    BIO = models.TextField(default = '<p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque at ligula purus. Praesent aliquet ipsum risus, nec interdum nunc tempus quis. Proin ultricies mauris urna, vel sagittis libero fermentum in. Sed eleifend varius nisl eu ullamcorper. Vestibulum condimentum cursus pretium. Aenean sed nibh ac dui pulvinar porttitor ut id neque. Sed consequat sapien sed magna venenatis lacinia. Praesent ullamcorper dignissim viverra. Curabitur ac odio et ante volutpat condimentum. Pellentesque eu faucibus ipsum. Sed est ante, accumsan id tortor vitae, vestibulum auctor magna. Vivamus in neque neque. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam non leo sit amet nunc maximus bibendum vitae fringilla ex. </p>')
    date_of_birth = models.DateField(null=True, blank=True)
