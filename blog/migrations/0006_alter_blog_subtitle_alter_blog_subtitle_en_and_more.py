# Generated by Django 5.1.6 on 2025-03-30 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blog_subtitle_alter_blog_subtitle_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='subtitle',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='subtitle_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='subtitle_es',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='subtitle_pt',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title_es',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title_pt',
            field=models.TextField(blank=True, null=True),
        ),
    ]
