# Generated by Django 5.1.6 on 2025-03-28 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0004_rename_price_vehicle_price_hour_vehicle_price_km'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='car_amenities_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='car_amenities_es',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='car_amenities_pt',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='car_best_for_services_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='car_best_for_services_es',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='car_best_for_services_pt',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='car_name_en',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='car_name_es',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='car_name_pt',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='car_overview_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='car_overview_es',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='car_overview_pt',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='car_type_en',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='car_type_es',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='car_type_pt',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
