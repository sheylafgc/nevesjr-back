# Generated by Django 5.1.4 on 2025-02-10 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OurService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True)),
                ('subtitle', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='ourServices/')),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
