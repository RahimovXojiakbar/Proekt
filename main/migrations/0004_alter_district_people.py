# Generated by Django 5.1.4 on 2025-01-01 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_district_mfys'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='people',
            field=models.PositiveIntegerField(default=25000),
        ),
    ]