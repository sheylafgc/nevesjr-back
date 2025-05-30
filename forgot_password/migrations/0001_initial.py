# Generated by Django 5.1.6 on 2025-03-13 15:05

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserResetPassword',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('generate_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('expiration_date', models.DateTimeField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_pass_code', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
