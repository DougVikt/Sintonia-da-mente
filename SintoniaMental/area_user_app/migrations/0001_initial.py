# Generated by Django 5.0.7 on 2024-12-22 23:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('register_app', '0005_alter_patients_options_alter_professionals_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewsUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('rating', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('id_specialist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register_app.professionals')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ReviewsUser',
                'verbose_name_plural': 'ReviewsUsers',
                'db_table': 'reviews_user',
                'ordering': ['id'],
                'managed': True,
            },
        ),
    ]
