# Generated by Django 5.0.2 on 2024-03-01 18:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0003_blogindex_hero_image"),
        ("images", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogdetail",
            name="hero_image",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="images.customimage",
            ),
        ),
    ]