# Generated by Django 5.1.4 on 2024-12-28 06:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_human_house_alter_human_information_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='human',
            name='house',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='human', to='main.house'),
        ),
        migrations.AlterField(
            model_name='human',
            name='information',
            field=models.CharField(choices=[('NO', 'NO'), ('MIDDLE', 'MIDDLE'), ('HIGH', 'HIGH')], default='NO', max_length=200),
        ),
        migrations.AlterField(
            model_name='human',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='human',
            name='status',
            field=models.CharField(choices=[('Kindergarten', 'Kindergarten'), ('Schoolboy', 'Schoolboy'), ('Student', 'Student'), ('Worker', 'Worker')], max_length=200),
        ),
    ]