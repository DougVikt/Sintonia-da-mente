# Generated by Django 5.1 on 2024-11-07 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Pacientes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("fone", models.CharField(max_length=15)),
                ("senha", models.CharField(max_length=128)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Profissionais",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("fone", models.CharField(max_length=15)),
                ("senha", models.CharField(max_length=128)),
                ("registro", models.CharField(max_length=80)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
