# Generated by Django 5.1.4 on 2025-02-10 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('occupation', models.CharField(blank=True, max_length=255, null=True)),
                ('user_image', models.ImageField(blank=True, null=True, upload_to='user_image/')),
                ('opinion', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
