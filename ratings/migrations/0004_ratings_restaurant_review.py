# Generated by Django 5.1.2 on 2024-10-23 21:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0003_ratings'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratings',
            name='restaurant_review',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ratings.restaurant'),
        ),
    ]