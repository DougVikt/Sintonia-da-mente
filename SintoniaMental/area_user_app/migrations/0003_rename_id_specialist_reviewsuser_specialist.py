# Generated by Django 5.0.7 on 2024-12-29 02:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('area_user_app', '0002_alter_reviewsuser_user_consultations'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviewsuser',
            old_name='id_specialist',
            new_name='specialist',
        ),
    ]