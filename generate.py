import os
import random
import django
from random import choice



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from faker import Faker
from main import models



models.President.objects.all().delete()
models.State.objects.all().delete()
models.Governor_Region.objects.all().delete()
models.Region.objects.all().delete()
models.Governor_District.objects.all().delete()
models.District.objects.all().delete()
models.Chairman.objects.all().delete()
models.MFY.objects.all().delete()
models.Neighborhood.objects.all().delete()
models.House.objects.all().delete()
models.Human.objects.all().delete()


fake = Faker()

for _ in range(3):
    president = models.President.objects.create(
        name = fake.name_male(),
        information = fake.random_element(['MIDDLE', 'HIGH']),
        party = fake.company(),
        BIO = fake.text(max_nb_chars=50),

    )
    president.save()
models.President.objects.all()
print('Add Presidents')

# =======================================================================================================

for _ in range(3):
    state = models.State.objects.create(
        title = fake.word(),
        president = choice(models.President.objects.all()),
        about = fake.text(max_nb_chars=200),
        anthem = fake.text(max_nb_chars=100),
        area_km_kv = round(random.uniform(100, 900), 2),
        regions = round(random.uniform(5 ,30)),
        people = round(random.uniform(1000000, 100000000)),

    )
    state.save()
models.State.objects.all()
print('Add States')

# =======================================================================================================

for _ in range(12):
    governor_region = models.Governor_Region.objects.create(
        name = fake.name(),
        information = fake.random_element(['MIDDLE', 'HIGH']),
        BIO = fake.text(max_nb_chars=50),
        
    )
    governor_region.save()
models.Governor_Region.objects.all()
print('Add Region Governors')

# =======================================================================================================

for _ in range(12):
    regions = models.Region.objects.create(
        title = fake.word(),
        governor = choice(models.Governor_Region.objects.all()),
        about = fake.text(max_nb_chars=200),
        area_km_kv = round(random.uniform(10, 90), 2),
        districts = round(random.uniform(5 ,30)),
        people = round(random.uniform(100000, 10000000)),
    )
    regions.save()
models.Region.objects.all()
print('Add Regions')

# =======================================================================================================

for _ in range(10):
    governor_district = models.Governor_District.objects.create(
        name = fake.name(),
        information = fake.random_element(['MIDDLE', 'HIGH']),
        BIO = fake.text(max_nb_chars=50),
        
    )
    governor_district.save()
models.Governor_District.objects.all()
print('Add District Governors')

# =======================================================================================================

for _ in range(13):
    districts = models.District.objects.create(
        title = fake.word(),
        governor = choice(models.Governor_District.objects.all()),
        about = fake.text(max_nb_chars=200),
        area_km_kv = round(random.uniform(10, 90), 2),
        MFYs = round(random.uniform(5 ,30)),
        people = round(random.uniform(100000, 10000000)),
    )
    districts.save()
models.District.objects.all()
print('Add Districts')

# =======================================================================================================

for _ in range(10):
    chairman = models.Chairman.objects.create(
        name = fake.name_male(),
        BIO = fake.text(),
        information = fake.random_element(['MIDDLE', 'HIGH']),
            
    )
    chairman.save()
models.Chairman.objects.all()
print('Add Chairmans')

# =======================================================================================================

for _ in range(13):
    MFY = models.MFY.objects.create(
        title = fake.word().capitalize(),
        district = choice(models.District.objects.all()),
        chairman = choice(models.Chairman.objects.all()),
        area_km_kv = round(random.uniform(8, 14), 2),
        neighborhoods = round(random.uniform(5, 15)),
        people = round(random.uniform(900, 1400)),
    )
    MFY.save()
models.MFY.objects.all()
print("Add MFY")

# =======================================================================================================

for _ in range(45):
    neighborhoods = models.Neighborhood.objects.create(
        title = fake.word().capitalize(),
        elder = fake.name_male(),
        MFY = choice(models.MFY.objects.all()),
        area_km_kv = round(random.uniform(2, 9), 2),
        houses = round(random.uniform(70, 120)),
        people = round(random.uniform(360, 500)),

    )
    neighborhoods.save()
models.Neighborhood.objects.all()
print('Add Neighborhoods')

# =======================================================================================================

for _ in range(300):
    houses = models.House.objects.create(
        house_boss = fake.name_male(),
        house_number = round(random.uniform(1, 99)),
        a_b = choice(['A', 'B']),
        status = fake.random_element(['POORER', 'MIDDLE', 'RICH']),
        neighborhood = choice(models.Neighborhood.objects.all()),
        area_kv_m = round(random.uniform(200, 1900), 2),
        people = round(random.uniform(1, 12)),

    )
    houses.save()
models.House.objects.all()
print('Add Houses')

# =======================================================================================================

for _ in range(1000):
    
    status = fake.random_element(['Kindergarten', 'Schoolboy', 'Student', 'Worker'])
    
    if status in ['Kindergarten', 'Schoolboy', 'Student']:
        information = 'NO'
    else:
        information = fake.random_element(['NO', 'MIDDLE', 'HIGH'])

    humans = models.Human.objects.create(
        name = fake.name(),
        BIO = fake.text(),
        status=status,
        information=information,
        house = choice(models.House.objects.all()),
            

    )
    humans.save()
models.Human.objects.all()
print('Add Humans')



