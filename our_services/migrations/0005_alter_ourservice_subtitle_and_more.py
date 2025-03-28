# Generated by Django 5.1.6 on 2025-03-28 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('our_services', '0004_ourservice_description_en_ourservice_description_es_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourservice',
            name='subtitle',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='ourservice',
            name='subtitle_en',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='ourservice',
            name='subtitle_es',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='ourservice',
            name='subtitle_pt',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='ourservice',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='ourservice',
            name='title_en',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='ourservice',
            name='title_es',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='ourservice',
            name='title_pt',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
