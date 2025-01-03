# Generated by Django 5.0.7 on 2024-12-08 03:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('fone', models.CharField(max_length=15)),
                ('date_birth', models.DateField()),
                ('password', models.CharField(max_length=128)),
                ('photo_perfil', models.ImageField(null=True, upload_to='photo_profile/')),
                ('auth_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Professionals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('fone', models.CharField(max_length=15)),
                ('date_birth', models.DateField()),
                ('password', models.CharField(max_length=128)),
                ('photo_perfil', models.ImageField(null=True, upload_to='photo_profile/')),
                ('register', models.CharField(max_length=80)),
                ('specialty', models.CharField(max_length=40)),
                ('verification', models.BooleanField(default=False)),
                ('auth_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Pacientes',
        ),
        migrations.DeleteModel(
            name='Profissionais',
        ),
    ]
