# Generated by Django 5.1.6 on 2025-03-29 22:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('feedback', '0005_rename_occupation_feedback_role'),
        ('frequently_questions', '0001_initial'),
        ('our_services', '0006_alter_ourservice_image'),
        ('vehicles', '0005_vehicle_car_amenities_en_vehicle_car_amenities_es_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section1_banner', models.ImageField(blank=True, null=True, upload_to='home_page/section1/banner')),
                ('section1_title', models.CharField(blank=True, max_length=255, null=True)),
                ('section1_title_en', models.CharField(blank=True, max_length=255, null=True)),
                ('section1_title_pt', models.CharField(blank=True, max_length=255, null=True)),
                ('section1_title_es', models.CharField(blank=True, max_length=255, null=True)),
                ('section2_title', models.CharField(blank=True, max_length=255, null=True)),
                ('section2_title_en', models.CharField(blank=True, max_length=255, null=True)),
                ('section2_title_pt', models.CharField(blank=True, max_length=255, null=True)),
                ('section2_title_es', models.CharField(blank=True, max_length=255, null=True)),
                ('section2_image', models.ImageField(blank=True, null=True, upload_to='home_page/section2/image')),
                ('section3_title', models.TextField(blank=True, null=True)),
                ('section3_title_en', models.TextField(blank=True, null=True)),
                ('section3_title_pt', models.TextField(blank=True, null=True)),
                ('section3_title_es', models.TextField(blank=True, null=True)),
                ('section3_image', models.ImageField(blank=True, null=True, upload_to='home_page/section3/image')),
                ('section4_image', models.ImageField(blank=True, null=True, upload_to='home_page/section4/image')),
                ('section4_title', models.CharField(blank=True, max_length=255, null=True)),
                ('section4_title_en', models.CharField(blank=True, max_length=255, null=True)),
                ('section4_title_pt', models.CharField(blank=True, max_length=255, null=True)),
                ('section4_title_es', models.CharField(blank=True, max_length=255, null=True)),
                ('section4_description', models.TextField(blank=True, null=True)),
                ('section4_description_en', models.TextField(blank=True, null=True)),
                ('section4_description_pt', models.TextField(blank=True, null=True)),
                ('section4_description_es', models.TextField(blank=True, null=True)),
                ('section5_title', models.CharField(blank=True, max_length=255, null=True)),
                ('section5_title_en', models.CharField(blank=True, max_length=255, null=True)),
                ('section5_title_pt', models.CharField(blank=True, max_length=255, null=True)),
                ('section5_title_es', models.CharField(blank=True, max_length=255, null=True)),
                ('section5_subtitle', models.TextField(blank=True, null=True)),
                ('section5_subtitle_en', models.TextField(blank=True, null=True)),
                ('section5_subtitle_pt', models.TextField(blank=True, null=True)),
                ('section5_subtitle_es', models.TextField(blank=True, null=True)),
                ('section6_title', models.CharField(blank=True, max_length=255, null=True)),
                ('section6_title_en', models.CharField(blank=True, max_length=255, null=True)),
                ('section6_title_pt', models.CharField(blank=True, max_length=255, null=True)),
                ('section6_title_es', models.CharField(blank=True, max_length=255, null=True)),
                ('section6_subtitle', models.TextField(blank=True, null=True)),
                ('section6_subtitle_en', models.TextField(blank=True, null=True)),
                ('section6_subtitle_pt', models.TextField(blank=True, null=True)),
                ('section6_subtitle_es', models.TextField(blank=True, null=True)),
                ('section7_title', models.CharField(blank=True, max_length=255, null=True)),
                ('section7_title_en', models.CharField(blank=True, max_length=255, null=True)),
                ('section7_title_pt', models.CharField(blank=True, max_length=255, null=True)),
                ('section7_title_es', models.CharField(blank=True, max_length=255, null=True)),
                ('section8_title', models.CharField(blank=True, max_length=255, null=True)),
                ('section8_title_en', models.CharField(blank=True, max_length=255, null=True)),
                ('section8_title_pt', models.CharField(blank=True, max_length=255, null=True)),
                ('section8_title_es', models.CharField(blank=True, max_length=255, null=True)),
                ('section8_banner', models.ImageField(blank=True, null=True, upload_to='home_page/section8/banner')),
                ('section2_services', models.ManyToManyField(blank=True, null=True, related_name='home_page_services', to='our_services.ourservice')),
                ('section5_feedbacks', models.ManyToManyField(blank=True, null=True, related_name='home_page_feedbacks', to='feedback.feedback')),
                ('section6_vehicles', models.ManyToManyField(blank=True, null=True, related_name='home_page_vehicles', to='vehicles.vehicle')),
                ('section7_frequently_questions', models.ManyToManyField(blank=True, null=True, related_name='home_page_frequently_questions', to='frequently_questions.frequentlyquestions')),
            ],
        ),
        migrations.CreateModel(
            name='HomePageDifferentials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('title_en', models.CharField(blank=True, max_length=255, null=True)),
                ('title_pt', models.CharField(blank=True, max_length=255, null=True)),
                ('title_es', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('description_en', models.TextField(blank=True, null=True)),
                ('description_pt', models.TextField(blank=True, null=True)),
                ('description_es', models.TextField(blank=True, null=True)),
                ('homepage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='differentials', to='home_page.homepage')),
            ],
        ),
    ]
