# Generated by Django 5.0.7 on 2024-12-28 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register_app', '0006_alter_patients_photo_perfil_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professionals',
            name='specialty',
            field=models.CharField(blank=True, default=None, max_length=50),
        ),
    ]
