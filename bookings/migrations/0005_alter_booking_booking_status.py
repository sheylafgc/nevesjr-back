# Generated by Django 5.1.6 on 2025-04-25 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_booking_booking_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_status',
            field=models.CharField(blank=True, choices=[('pending', 'Pending'), ('upcoming', 'Upcoming'), ('past', 'Past'), ('Canceled', 'Pendente')], max_length=255, null=True),
        ),
    ]
