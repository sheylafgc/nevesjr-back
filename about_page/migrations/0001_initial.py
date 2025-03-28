# Generated by Django 5.1.6 on 2025-03-28 17:13

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section1_title', models.CharField(blank=True, max_length=255, null=True)),
                ('section1_title_en', models.CharField(blank=True, max_length=255, null=True)),
                ('section1_title_pt', models.CharField(blank=True, max_length=255, null=True)),
                ('section1_title_es', models.CharField(blank=True, max_length=255, null=True)),
                ('section1_subtitle', models.TextField(blank=True, null=True)),
                ('section1_subtitle_en', models.TextField(blank=True, null=True)),
                ('section1_subtitle_pt', models.TextField(blank=True, null=True)),
                ('section1_subtitle_es', models.TextField(blank=True, null=True)),
                ('section1_video', models.FileField(blank=True, null=True, upload_to='about_page/section1/video', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov', 'mkv'])])),
                ('section2_title', models.CharField(blank=True, max_length=255, null=True)),
                ('section2_title_en', models.CharField(blank=True, max_length=255, null=True)),
                ('section2_title_pt', models.CharField(blank=True, max_length=255, null=True)),
                ('section2_title_es', models.CharField(blank=True, max_length=255, null=True)),
                ('section2_description', models.TextField(blank=True, null=True)),
                ('section2_description_en', models.TextField(blank=True, null=True)),
                ('section2_description_pt', models.TextField(blank=True, null=True)),
                ('section2_description_es', models.TextField(blank=True, null=True)),
                ('section3_image', models.ImageField(blank=True, null=True, upload_to='about_page/section3/image')),
                ('section3_title', models.CharField(blank=True, max_length=255, null=True)),
                ('section3_title_en', models.CharField(blank=True, max_length=255, null=True)),
                ('section3_title_pt', models.CharField(blank=True, max_length=255, null=True)),
                ('section3_title_es', models.CharField(blank=True, max_length=255, null=True)),
                ('section3_description', models.TextField(blank=True, null=True)),
                ('section3_description_en', models.TextField(blank=True, null=True)),
                ('section3_description_pt', models.TextField(blank=True, null=True)),
                ('section3_description_es', models.TextField(blank=True, null=True)),
                ('section4_image', models.ImageField(blank=True, null=True, upload_to='about_page/section4/image')),
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
                ('section5_description', models.TextField(blank=True, null=True)),
                ('section5_description_en', models.TextField(blank=True, null=True)),
                ('section5_description_pt', models.TextField(blank=True, null=True)),
                ('section5_description_es', models.TextField(blank=True, null=True)),
                ('section6_title', models.CharField(blank=True, max_length=255, null=True)),
                ('section6_title_en', models.CharField(blank=True, max_length=255, null=True)),
                ('section6_title_pt', models.CharField(blank=True, max_length=255, null=True)),
                ('section6_title_es', models.CharField(blank=True, max_length=255, null=True)),
                ('section6_banner', models.ImageField(blank=True, null=True, upload_to='about_page/section6/banner')),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('role', models.CharField(blank=True, max_length=255, null=True)),
                ('role_en', models.CharField(blank=True, max_length=255, null=True)),
                ('role_pt', models.CharField(blank=True, max_length=255, null=True)),
                ('role_es', models.CharField(blank=True, max_length=255, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='about_page/section5/team_avatars')),
                ('about_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_members', to='about_page.aboutpage')),
            ],
        ),
    ]
