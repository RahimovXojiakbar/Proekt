# Generated by Django 5.1.4 on 2024-12-25 08:39

import django.db.models.deletion
import django_ckeditor_5.fields
import shortuuid.django_fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chairman',
            fields=[
                ('uuid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvwxz', editable=False, length=22, max_length=12, prefix='id-', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('BIO', django_ckeditor_5.fields.CKEditor5Field()),
                ('information', models.CharField(choices=[('MIDDLE', 'MIDDLE'), ('HIGH', 'HIGH')], max_length=200)),
                ('created', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-uuid'],
            },
        ),
        migrations.CreateModel(
            name='Governor_District',
            fields=[
                ('uuid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvwxz', editable=False, length=22, max_length=12, prefix='id-', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('information', models.CharField(choices=[('MIDDLE', 'MIDDLE'), ('HIGH', 'HIGH')], max_length=200)),
                ('BIO', django_ckeditor_5.fields.CKEditor5Field()),
                ('created', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-uuid'],
            },
        ),
        migrations.CreateModel(
            name='Governor_Region',
            fields=[
                ('uuid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvwxz', editable=False, length=22, max_length=12, prefix='id-', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('information', models.CharField(choices=[('MIDDLE', 'MIDDLE'), ('HIGH', 'HIGH')], max_length=200)),
                ('BIO', django_ckeditor_5.fields.CKEditor5Field()),
                ('created', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-uuid'],
            },
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('uuid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvwxz', editable=False, length=22, max_length=12, prefix='id-', primary_key=True, serialize=False)),
                ('house_boss', models.CharField(max_length=200)),
                ('house_number', models.PositiveIntegerField()),
                ('a_b', models.CharField(choices=[('A', 'A'), ('B', 'B')], max_length=200)),
                ('status', models.CharField(choices=[('POORER', 'POORER'), ('MIDDLE', 'MIDDLE'), ('RICH', 'RICH')], max_length=200)),
                ('people', models.PositiveIntegerField(blank=True)),
                ('area_kv_m', models.DecimalField(decimal_places=2, max_digits=15)),
                ('created', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ['house_number', 'a_b'],
            },
        ),
        migrations.CreateModel(
            name='President',
            fields=[
                ('uuid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvwxz', editable=False, length=22, max_length=12, prefix='id-', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('information', models.CharField(choices=[('MIDDLE', 'MIDDLE'), ('HIGH', 'HIGH')], max_length=200)),
                ('party', models.CharField(max_length=200)),
                ('BIO', django_ckeditor_5.fields.CKEditor5Field()),
                ('created', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-uuid'],
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('uuid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvwxz', editable=False, length=22, max_length=12, prefix='id-', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('about', django_ckeditor_5.fields.CKEditor5Field()),
                ('area_km_kv', models.DecimalField(decimal_places=2, max_digits=10)),
                ('MFY', models.PositiveIntegerField()),
                ('people', models.PositiveIntegerField()),
                ('created', models.DateField(auto_now_add=True)),
                ('governor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='district', to='main.governor_district')),
            ],
            options={
                'ordering': ['-uuid'],
            },
        ),
        migrations.CreateModel(
            name='Human',
            fields=[
                ('uuid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvwxz', editable=False, length=22, max_length=12, prefix='id-', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('BIO', django_ckeditor_5.fields.CKEditor5Field()),
                ('status', models.CharField(choices=[('Kindergarten', 'Kindergarten'), ('Schoolboy', 'Schoolboy'), ('Student', 'Student'), ('Worker', 'Worker')], max_length=200)),
                ('information', models.CharField(choices=[('NO', 'NO'), ('MIDDLE', 'MIDDLE'), ('HIGH', 'HIGH')], default='NO', max_length=200)),
                ('created', models.DateField(auto_now_add=True)),
                ('house', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='human', to='main.house')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MFY',
            fields=[
                ('uuid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvwxz', editable=False, length=22, max_length=12, prefix='id-', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('area_km_kv', models.DecimalField(decimal_places=2, max_digits=10)),
                ('neighborhoods', models.PositiveIntegerField()),
                ('people', models.PositiveIntegerField()),
                ('created', models.DateField(auto_now_add=True)),
                ('chairman', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='C_MFY', to='main.chairman')),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='d_MFY', to='main.district')),
            ],
            options={
                'ordering': ['-uuid'],
            },
        ),
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('uuid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvwxz', editable=False, length=22, max_length=12, prefix='id-', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('elder', models.CharField(max_length=250)),
                ('area_km_kv', models.DecimalField(decimal_places=2, max_digits=15)),
                ('houses', models.PositiveIntegerField()),
                ('people', models.PositiveIntegerField()),
                ('created', models.DateField(auto_now_add=True)),
                ('MFY', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.mfy')),
            ],
            options={
                'ordering': ['-uuid'],
            },
        ),
        migrations.AddField(
            model_name='house',
            name='neighborhood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='house', to='main.neighborhood'),
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('uuid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvwxz', editable=False, length=22, max_length=12, prefix='id-', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('about', django_ckeditor_5.fields.CKEditor5Field()),
                ('area_km_kv', models.DecimalField(decimal_places=2, max_digits=10)),
                ('districts', models.PositiveIntegerField()),
                ('people', models.PositiveIntegerField()),
                ('created', models.DateField(auto_now_add=True)),
                ('governor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='region', to='main.governor_region')),
            ],
            options={
                'ordering': ['-uuid'],
            },
        ),
        migrations.AddField(
            model_name='district',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='district', to='main.region'),
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('uuid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvwxz', editable=False, length=22, max_length=12, prefix='id-', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('about', django_ckeditor_5.fields.CKEditor5Field()),
                ('flag', models.ImageField(blank=True, upload_to='images')),
                ('anthem', models.TextField()),
                ('emblem', models.ImageField(blank=True, upload_to='images')),
                ('area_km_kv', models.DecimalField(decimal_places=2, max_digits=10)),
                ('regions', models.PositiveIntegerField()),
                ('people', models.PositiveIntegerField()),
                ('created', models.DateField(auto_now_add=True)),
                ('president', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='state', to='main.president')),
            ],
            options={
                'ordering': ['-uuid'],
            },
        ),
        migrations.AddField(
            model_name='region',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='region', to='main.state'),
        ),
    ]
