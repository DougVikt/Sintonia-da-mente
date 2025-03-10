# Generated by Django 5.0.7 on 2024-12-15 03:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register_app', '0003_remove_patients_auth_user_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patients',
            name='email',
        ),
        migrations.RemoveField(
            model_name='patients',
            name='password',
        ),
        migrations.RemoveField(
            model_name='professionals',
            name='email',
        ),
        migrations.RemoveField(
            model_name='professionals',
            name='password',
        ),
        migrations.AddField(
            model_name='patients',
            name='auth_user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='professionals',
            name='auth_user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='professionals',
            name='specialty',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
