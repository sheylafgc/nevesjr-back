# Generated by Django 5.1.6 on 2025-03-30 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('our_fleet_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourfleetpage',
            name='section1_subtitle',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ourfleetpage',
            name='section1_subtitle_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ourfleetpage',
            name='section1_subtitle_es',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ourfleetpage',
            name='section1_subtitle_pt',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ourfleetpage',
            name='section1_title',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ourfleetpage',
            name='section1_title_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ourfleetpage',
            name='section1_title_es',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ourfleetpage',
            name='section1_title_pt',
            field=models.TextField(blank=True, null=True),
        ),
    ]
